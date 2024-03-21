use market_db;
select * from member;
select * from member where mem_name = '블랙핑크';

use sys;

select * from market_db.member;

use market_db;

select addr 키, height 신장, debut_date "데뷔 일자" from member;

select * from member where mem_number<=4;

select * from member where height<=162;

select * from member where height>=162 or mem_number>6;

select * from member where height between 163 and 167;

select * from member where addr in('경기','전남','경남');

select * from member where mem_name like '__핑크';

select * from member order by(phone1);


select * from member;


select * from member mem_id, mem_name, debut_date;


select mem_id, mem_name, debut_date from member order by(phone1);


select distinct addr from member;

select mem_id "회원 아이디", sum(amount*price) "총 구매 가격" from buy group by mem_id;

select count(*) from member;

select count(phone1) from member;


create table hongong1 (toy_id int, toy_name char(4), age int);
insert into hongong1 values (1,'우디', 25);

create table hongon2 (toy_id int auto_increment primary key, toy_name char(4), age int);

insert into hongon2 values (null, '보핍', 25);
insert into hongon2 values  (null, '아무거나', 22);
insert into hongon2 values  (null, '으에에', 21);

select * from hongon2;

select toy_id from hongon2;


alter table hongon2 auto_increment=100;

select count(8) from world.city;

desc world.city;

select * from world.city limit 5,1;

insert into hongon2 values  (null, '으에에', 21);
select last_insert_id(); 

set @@auto_increment_increment=100;

create table city_popul (city_name char(35), population int);

insert into city_popul
	select name, population from world.city;
    
    use market_db;
    
update city_popul
	set city_name = '서울'
		where city_name = 'Seoul';
        
select * from city_popul where city_name='서울';

delete from city_popul where city_name like 'new%';