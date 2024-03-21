use market_db;

create table hongong4 (tinyint_col tinyint, smallint_col smallint, int_col int, bigint_col bigint);

insert into hongong4 values(127,32767, 2147483647, 900000000000000);

insert into hongong4 values(128,32768, 2147483648, 900000000000001);

drop table big_table;
create table big_table (data1 char(255));
create table big_table (data2 varchar(16383));

create database netflix_db;
use netflix_db

create table movie
	(movie_id	int,
    movie_title varchar(30),
    movie_director varchar(30),
    movie_star varchar(30),
    movie_script longtext,
    movie_film longblob
);
    
use market_db;
set @myvar1=5;
set @myvar2=4.25;

select @myvar1;
select @myvar2;

select @myvar1*@myvar2;

set @txt='가수이름==>';

set @count = 3;
select mem_name, height from member order by height limit @count;

prepare mysql from 'select mem_name, height from member order by height limit ?';
execute mysql using @count;

select avg(price) "평균 가격" from buy;

select cast(avg(price) as signed) "vudrbsrkur" from buy;

select num, concat(cast(price as char), 'x', cast(amount as char),'=') '가격 * 수량', price*amount '결과' from buy;

select '100'+'200';
select concat(100,200);

select 1 > '2mega';
select 3 > '2mega';
select 0 = 'mega2';

use market_db;

select * 
	from buy
    inner join member
    on buy.mem_id = member.mem_id;

    

    select buy.mem_id, mem_name, prod_name, addr, concat(phone1, phone2) '연락처'
    from buy
    inner join member
    on buy.mem_id = member.mem_id;
    
	from member
    inner join buy
    on buy.mem_id = member.mem_id
    where buy.mem_id = 'grl';


select m.mem_id, m.mem_name, b.prod_name, m.addr
from member m
left outer join buy b
on m.mem_id=b.mem_id
order by m.mem_id;

select *
from buy
cross join member;

create table cross_table
select count(*)
from sakila.actor
cross join world.country;



use market_db;

create table emp_table (emp char(4), manager char(4), phone varchar(8));

insert into emp_table values('대표', null, '0000');
insert into emp_table values('영업이사', '대표', '1111');
insert into emp_table values('관리이사', '대표', '2222');
insert into emp_table values('정보이사', '대표', '3333');
insert into emp_table values('영업과장', '영업이사', '1111-1');
insert into emp_table values('경리부장', '영업이사', '2222-1');
insert into emp_table values('인사부장', '관리이사', '2222-2');
insert into emp_table values('개발팀장', '정보이사', '3333-1');
insert into emp_table values('개발주임', '정보이사', '3333-1-1');

select a.emp "직원", b.emp "직속상관", b.phone "직속상관연락처"
from emp_table a
inner join emp_table b
on a.manager = b.emp;


drop procedure if exists ifproc1;

delimiter $$
create procedure ifproc1()
begin
	if 100=20 then
		select '100은 100과 같습니다';
	end if;
end $$
delimiter ;

call ifproc1();

drop procedure if exists ifproc2;

delimiter $$
create procedure ifproc2()
begin
	declare mynum int;
    set mynum =100;
	if mynum=100 then
		select '100입니다';
	else
		select '100이 아닙니다';
	end if;
end $$
delimiter ;

call ifproc2();


drop procedure if exists ifproc3;

delimiter $$
create procedure ifproc3()
begin
	declare debutdate date;
    declare curdate date;
    declare days int;
    
    select debut_date into debutdate
		from market_db.member
        where mem_id = 'blk';
        
    set curdate = current_date();
    set days = datediff(curdate, debutdate)/365;
    
    if (days) >= 10 then
		select concat('데뷔한지', days, '년이나 지났습니다. 축하합니다!');
	else
		select concat('데뷔한지', days , '년밖에 안되었네요. 화이팅!');
	end if;
end $$
delimiter ;

call ifproc3();

drop procedure if exists caseproc;

delimiter $$
create procedure caseproc()
begin
	declare point int;
    declare credit char(3);
    set point=88;
	case
		when point >= 90 then
			set credit ='A';
		when point >= 80 then
			set credit = 'B';
		when point >= 70 then
			set credit = 'C';
		when point >= 60 then
			set credit = 'D';
		else
			set credit = 'F';
	end case;
    select concat('취득점수==>', point), concat('학점==>', credit);
end $$
delimiter ;

    
            


call caseproc();


select mem_id, sum(price*amount) "총 구매액"
	from buy
    group by mem_id
    order by sum(price*amount) desc;
	
select b.mem_id, m.mem_name, sum(price*amount)
	from buy b
    inner join member m
    on b.mem_id=m.mem_id
    group by mem_id
    order by sum(price*amount) desc;
    
	create table ddd 
    select b.mem_id, m.mem_name, sum(price*amount) "총구매액",
		case
			when (sum(price*amount) > 1500) then '최우수고객'
          	when (sum(price*amount) > 1000) then '우수고객'  
			when (sum(price*amount) > 1) then '일반고객'
            else '유령고객'
		end '회원등급'
	from buy b
    right outer join member m
    on b.mem_id=m.mem_id
    group by m.mem_id
    order by sum(price*amount) desc;
    
drop procedure if exists whileproc;

delimiter $$
create procedure whileproc()
begin
	declare i int;
    declare hap int;
    set i=1;
    set hap=0;
    
    while(i<=100) do
		set hap = hap+i;
        set i = i+1;
	end while;
    
    select '1부터 100까지의 합 ==>', hap;
end $$
delimiter ;

call whileproc();
 
 drop procedure if exists whileproc2;

delimiter $$
create procedure whileproc2()
begin
	declare i int;
    declare hap int;
    set i=1;
    set hap=0;
    
    mywhile:
    while(i<=100) do
		if(i%4=0) then
        set i = i+1;
        iterate mywhile;
	end if;
    set hap = hap+i;
    if (hap>1000) then
		leave mywhile;
	end if;
    set i = i+1;
    end while;
    
    select '1부터 100까지의 합(4의 배수 제외), 1000넘으면 종료 ==>', hap;
end $$
delimiter ;

call whileproc2();
 
 
 drop table if exists gate_table;
 
 create table gate_table (id int auto_increment primary key, entry_time datetime);
 
 set @curdate = current_timestamp();
 
 prepare myq from 'insert into gate_table values(null, ?)';
 execute myq using @curdate;
 select * from gate_table;