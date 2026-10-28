-- Ejecutar en Supabase: Dashboard -> SQL Editor -> New query -> pega esto -> Run.
-- Guarda la contraseña de cifrado del contenido (la de cifrar.js) en Supabase,
-- para que la web la obtenga sola tras el login (ya no hay que pedirla a mano).
-- Solo la pueden leer usuarios con sesión iniciada (login de Supabase), nunca
-- un visitante anónimo.

create table if not exists public.app_secrets (
  id text primary key,
  value text not null
);

alter table public.app_secrets enable row level security;

drop policy if exists "usuarios logueados leen los secretos de la app" on public.app_secrets;
create policy "usuarios logueados leen los secretos de la app"
  on public.app_secrets for select
  to authenticated
  using (true);

-- No hay política de insert/update/delete a propósito: esto se edita solo
-- desde aquí (SQL Editor) o Table Editor, nunca desde la web.

-- IMPORTANTE: pon aquí la contraseña ACTUAL de cifrado (la que usaste en
-- node cifrar.js para generar lo que hay en cifrado/ ahora mismo). Si cambias
-- la contraseña de cifrado más adelante (node cifrar.js --nueva-clave), tienes
-- que volver a ejecutar este mismo insert con la contraseña nueva.
insert into public.app_secrets (id, value)
values ('content_key', 'PON_AQUI_LA_CONTRASEÑA_DE_CIFRADO_ACTUAL')
on conflict (id) do update set value = excluded.value;
