-- Create table for tracking visitors
create table if not exists public.capprep_visitors (
  id uuid primary key default gen_random_uuid(),
  visitor_id text not null,
  page_path text default '/',
  referrer text default '',
  created_at timestamp with time zone default timezone('utc'::text, now())
);

-- Enable RLS
alter table public.capprep_visitors enable row level security;

-- Policies
drop policy if exists "Allow public insert visitors" on public.capprep_visitors;
create policy "Allow public insert visitors" on public.capprep_visitors for insert with check (true);

drop policy if exists "Allow public select visitors" on public.capprep_visitors;
create policy "Allow public select visitors" on public.capprep_visitors for select using (true);
