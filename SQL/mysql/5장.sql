SELECT * FROM naver_db.buy;

drop database if exists naver_db;

create database naver_db;
use naver_db;

create table member
(mem_id char(8) not null primary key,
mem_name varchar(10) not null,
mem_number tinyint not null,
addr char(2) not null,
phone1 char(3) null,
phone2 char(8) null,
height tinyint unsigned null,
debut_date date null);

create table buy
(num int not null primary key auto_increment,
mem_id char(8) not null,
prod_name char(8) not null,
group_name char(4) null,
price int unsigned not null,
amount smallint unsigned not null);

alter table buy
add constraint
foreign key(mem_id) references member(mem_id)
on update cascade
on delete cascade;

drop table if exists buy;

create table member
( mem_id char(8) not null,
mem_name varchar(10) not null,
height tinyint unsigned null
);

describe member;

alter table member
add constraint primary key(mem_id);


create table buy
(num int auto_increment not null primary key,
mem_id char(8) not null,
prod_name char(6) not null,
foreign key(mem_id) references member(mem_id));

describe buy;


insert into member values('blk', '블랙핑크', 163);
insert into buy values(null, 'blk', '지갑');
insert into buy values(null, 'blk', '맥북');

select m.mem_id, m.mem_name, b.prod_name
	from member m
    inner join buy b
    on m.mem_id=b.mem_id;
    
update member set mem_id='pink' where mem_id='blk';

alter table buy
	add constraint
    on update cascade
    on delete cascade;

describe buy;


drop table if exists buy, member;

create table member
( mem_id char(8) not null primary key,
mem_name varchar(10) not null,
height tinyint unsigned null,
email char(30) null unique);

insert into member values('blk', '블랙핑크', 163, 'pink@gmail.com');
insert into member values('twc', '트와이스', 167, null);
insert into member values('apn', '에이핑크', 164, 'pink@gmail.com');

select * from member;

create table member
( mem_id char(8) not null primary key,
mem_name varchar(10) not null,
height tinyint unsigned null check(height>=100),
phone1 char(3) null);

insert into member values('blk', '블랙핑크', 163, null);
insert into member values('twc', '트와이스', 166, null);

alter table member
add constraint
check(phone1 in('02', '031', '032', '054', '055', '061'));

insert into member values('twc', '트와이스', 167, '066');

create table member
(mem_id char(8) not null primary key,
mem_name varchar(10) not null,
height tinyint unsigned null default 160,
phone1 char(3) null
);

select * from member;

alter table member
	alter column phone1 set default '02';
    
insert into member values(' red', '레드벨벳', 161, '054');
insert into member values('spc', '우주소녀', default, default);
insert into member values('nnn', '신동길', null, null);

select * from member;


use market_db;

select mem_id, mem_name, addr from member;

create view v_member
as
	select mem_id, mem_name, addr from member;


select mem_name, addr from v_member
	where addr in('서울', '경기');

create view v_memberbuy
as
	select b.mem_id, m.mem_name, b.prod_name, m.addr,
		concat(m.phone1, m.phone2) '연락처'
	from buy b
		inner join member m
		on b.mem_id=m.mem_id;
        
select * from v_memberbuy;


create view v_viewtest1
as
	select b.mem_id 'member id', m.mem_name as 'member name', b.prod_name as 'product name', concat(m.phone1, m.phone2) as 'office phone'
    from buy b
    inner join member m
    on b.mem_id=m.mem_id;
    
    select * from v_viewtest1;
    
    select distinct `member id`, `member name` from v_viewtest1;

alter view v_viewtest1
as
	select b.mem_id '회원 아이디', m.mem_name as '회원 이름', b.prod_name '제품이름',
		concat(m.phone1, m.phone2) as '연락처'
	from buy b
    inner join member m
    on b.mem_id=m.mem_id;
    
select distinct `회원 아이디`, `회원 이름` from v_viewtest1;

describe v_viewtest1;

show create view v_viewtest1;

update v_member set addr='부산' where mem_id='blk';

 select * from v_member;
 
 select * from member;
 
 create or replace view v_height67
	as
		select * from member where height>=167;
        
        
alter view v_height67
as
	select * from member where height >= 167
		with check option;
        
insert into v_height67 values('tob', '텔레토비', 4, '영국', null, null, 140, '1995-01-01');
        
drop table if exists buy, member;

select * from v_height67;

check table v_height67;