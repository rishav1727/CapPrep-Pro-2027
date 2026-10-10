-- 1. Create capprep_users table
create table if not exists public.capprep_users (
  id uuid primary key default gen_random_uuid(),
  email text unique not null,
  name text,
  password text not null,
  phone text,
  college text,
  is_pro boolean default true,
  is_vip boolean default false,
  created_at timestamp with time zone default timezone('utc'::text, now())
);

-- 2. Create capprep_orders table
create table if not exists public.capprep_orders (
  id uuid primary key default gen_random_uuid(),
  order_id text unique,
  email text not null,
  name text,
  phone text,
  college text,
  amount numeric default 51,
  method text default 'UPI',
  utr text,
  status text default 'VERIFIED',
  created_at timestamp with time zone default timezone('utc'::text, now())
);

-- 3. Pre-seed our existing verified candidates
insert into public.capprep_users (email, name, password, phone, college, is_pro, is_vip)
values 
  ('rajneeshchaubey360@gmail.com', 'Rajneesh Chaubey', 'HpbFpxwD', '+91 98000 00000', 'Capgemini Candidate', true, true),
  ('pinea8888@gmail.com', 'Enrolled Pro Student', 'cap2027', '+91 98000 00000', 'Capgemini Candidate', true, true)
on conflict (email) do update 
set is_pro = true;

-- 4. Enable Row Level Security (RLS)
alter table public.capprep_users enable row level security;
alter table public.capprep_orders enable row level security;

-- 5. Policies: allow public anon read and write for seamless web app integration
drop policy if exists "Allow public read users" on public.capprep_users;
create policy "Allow public read users" on public.capprep_users for select using (true);

drop policy if exists "Allow public insert users" on public.capprep_users;
create policy "Allow public insert users" on public.capprep_users for insert with check (true);

drop policy if exists "Allow public update users" on public.capprep_users;
create policy "Allow public update users" on public.capprep_users for update using (true);

drop policy if exists "Allow public read orders" on public.capprep_orders;
create policy "Allow public read orders" on public.capprep_orders for select using (true);

drop policy if exists "Allow public insert orders" on public.capprep_orders;
create policy "Allow public insert orders" on public.capprep_orders for insert with check (true);

drop policy if exists "Allow public update orders" on public.capprep_orders;
create policy "Allow public update orders" on public.capprep_orders for update using (true);
