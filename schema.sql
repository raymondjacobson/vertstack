drop table if exists events;
create table events (
  id integer primary key autoincrement,
  happened_at timestamp not null,
  content text,
 	media_type text,
  media_resource text
);
