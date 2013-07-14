-- Generates necessary tables for Vertstack

drop table if exists events;
drop table if exists media_types;

create table events (
  id integer primary key autoincrement,
  happened_at timestamp not null,
  content text,
 	media_type text,
  media_resource text,

  foreign key(media_type) references media_types(type)
);

create table media_types (
	type text not null
);

insert into media_types(type) values ('youtube');
insert into media_types(type) values ('image');
insert into media_types(type) values ('hyperlink');