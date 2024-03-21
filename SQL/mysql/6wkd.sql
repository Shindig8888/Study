use market_db;

create table table1(
	col1 int primary key,
    col2 int,
    col3 int);
    
show index from table1;
show index from buy;

create table table2(
	col1 int primary key,
    col2 int unique,
    col3 int unique);
    
show index from table2;


----;

create database market2;

use market2;

create table member(
	mem_id char(8),
    mem_name varchar(10),
    mem_number int,
    addr char(2));
    
insert into member values('twc', '트와이스', 9, '서울');
insert into member values('blk', '블랙핑크', 4, '경남');
insert into member values('wmn', '여자친구', 6, '경기');

select * from member;

alter table member
	add constraint
	primary key(mem_id);
    
alter table member drop primary key;

alter table member
	add constraint
    primary key(mem_name);

insert into member values('grl', '소녀시대', 8, '서울');

drop table if exists member;

create table member
(mem_id char(8),
mem_name varchar(10),
mem_number int,
addr char(2));

insert into member values('twc', '트와이스', 9, '서울');
insert into member values('blk', '블랙핑크', 4, '경남');
insert into member values('wmn', '여자친구', 6, '경기');
insert into member values('omy', '오마이걸', 7, '서울');

alter table member
	add constraint
    unique(mem_id);
    
select * from member;

alter table member
	add constraint
    unique(mem_name);

insert into member values('grl', '소녀시대', 8, '서울');

use market_db;

create table cluster
(mem_id char(8),
mem_name varchar(10));

insert into cluster values('twc', '트와이스');
insert into cluster values('blk', '블랙핑크');
insert into cluster values('wmn', '여자친구');
insert into cluster values('omy', '오마이걸');
insert into cluster values('grl', '소녀시대');
insert into cluster values('itz', '잇지');
insert into cluster values('red', '레드벨벳');
insert into cluster values('apn', '에이핑크');
insert into cluster values('spc', '우주소녀');
insert into cluster values('mmu', '마마무');

select * from cluster;

alter table cluster
	add constraint
    primary key(mem_id);
    
alter table cluster drop primary key;

use market_db;

select * from member;

show index from member;

show table status like 'member';

create index idx_member_addr
	on member(addr);
    
    analyze table member;
    
show table status like 'member';

create unique index idx_mem_name
	on member(mem_name);
    
analyze table member;

insert into member values('ㅡㅐㅐ', '마마무', 2, '태국', '001', '12341234', 155, '2020.10.10');

show index from member;

select * from member;

select mem_id, mem_name, addr from member;

select mem_id, mem_name, addr from member where mem_name='에이핑크';

create index idx_member_mem_number
	on member(mem_number);
    
    analyze table member;
    
select mem_name, mem_number
	from member
	where mem_number >=7;

select mem_name, mem_number
	from member
	where mem_number >=1;

select mem_name, mem_number
	from member
	where mem_number*2 >=14;
    
    select mem_name, mem_number
	from member
	where mem_number>=14/2;
    
select table_name, constraint_name
	from information_schema.referential_constraints
    where constraint_schema = 'market_db';