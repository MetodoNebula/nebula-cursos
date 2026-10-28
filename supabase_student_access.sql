-- Ejecutar en Supabase: Dashboard -> SQL Editor -> New query -> pega esto -> Run.
-- Crea la tabla donde se guarda, por alumno, a qué cursos tiene acceso.

create table if not exists public.student_access (
  user_id uuid primary key references auth.users(id) on delete cascade,
  allowed_courses text[] not null default '{}'
);

alter table public.student_access enable row level security;

-- Cada alumno solo puede leer su propia fila (nunca la de otro alumno).
drop policy if exists "cada alumno ve solo su fila" on public.student_access;
create policy "cada alumno ve solo su fila"
  on public.student_access for select
  using (auth.uid() = user_id);

-- No hay política de insert/update/delete a propósito: los alumnos no pueden
-- tocar esta tabla desde la web. Los cursos se asignan solo desde aquí (SQL
-- Editor) o desde Table Editor, con tu sesión de administrador.

-- Primer alumno: lucas_es01, solo GCSE (los "key" de curso están en
-- catalog.json / cifrado/catalog.bin, campo "key" de cada proyecto).
insert into public.student_access (user_id, allowed_courses)
values (
  'd97d2976-346f-4b1b-9ec2-d73aa561edb4', -- id de lucas_es01 en Authentication -> Users
  array['gcse_mates', 'gcse_ciencias_chem', 'gcse_ciencias_phys']
)
on conflict (user_id) do update set allowed_courses = excluded.allowed_courses;

-- Admin: adminnebula@nebulacursos.local, acceso a todos los cursos.
-- allowed_courses = ['*'] significa "sin restricción" (incluye cursos que se
-- añadan en el futuro, sin tener que volver a tocar esta fila).
insert into public.student_access (user_id, allowed_courses)
select id, array['*']
from auth.users
where email = 'adminnebula@nebulacursos.local'
on conflict (user_id) do update set allowed_courses = excluded.allowed_courses;

-- Para dar acceso a otro alumno más adelante: copia su "User UID" desde
-- Authentication -> Users (o usa el mismo truco de "select id ... where email = ...")
-- y repite el insert con los "key" que quieras, o con ['*'] para acceso total.
-- Keys disponibles ahora mismo:
--   ESO:          fq_completo, eso_matematicas
--   GCSE:         gcse_mates, gcse_ciencias_chem, gcse_ciencias_phys
--   Selectividad: selectividad_quimica, selectividad_fisica,
--                 selectividad_matematicas, selectividad_matematicas_ccss
