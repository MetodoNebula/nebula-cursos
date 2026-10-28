-- Ejecutar en Supabase: Dashboard -> SQL Editor -> New query -> pega esto -> Run.
-- Tabla y política de acceso. Las filas (las claves de cada curso) se
-- insertan aparte, con el SQL que genera cifrar.js (ver README/LEEME.txt).

create table if not exists public.course_secrets (
  course_key text primary key,
  value text not null
);

alter table public.course_secrets enable row level security;

drop policy if exists "solo los cursos permitidos al alumno" on public.course_secrets;
create policy "solo los cursos permitidos al alumno"
  on public.course_secrets for select
  to authenticated
  using (
    exists (
      select 1 from public.student_access sa
      where sa.user_id = auth.uid()
        and (course_key = any(sa.allowed_courses) or '*' = any(sa.allowed_courses))
    )
  );

-- No hay política de insert/update/delete a propósito: esta tabla se rellena
-- solo desde aquí (SQL Editor) con el resultado de cifrar.js, nunca desde la web.
