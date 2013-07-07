drop table if exists events;
create table events (
  id integer primary key autoincrement,
  title text not null,
  happened_at timestamp not null,
  content text,
  media_resource text
);
