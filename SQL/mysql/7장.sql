 delimiter $$
 create procedure user_proc3(
	in txtvalue char(10),
    out outvalue int	)
begin
	insert into notable values(null, txtvalue);
	select max(id) into outvalue from notable;
end $$
delimiter ;

desc notable;

call user_proc3 ('테스트1' , @myvalue);

select * from notable;

select concat('입력된 id값', @myvalue);

drop procedure if exists ifelse_proc;
delimiter $$
create procedure ifelse_proc(
	in memname varchar(10))
begin
	declare debutyear int;
    select year(debut_date) into debutyear from member
		where mem_name=memname;
	if (debutyear >= 2015) then
		select '신인가수네요, 화이팅!' as '메시지';
	else
		select '고참가수네요, 수고하셨어요' as '메시지';
	end if;
end $$
delimiter ;

call ifelse_proc('소녀시대');

drop procedure if exists while_proc;
use market_db;

drop procedure if exists user_proc;

delimiter $$
create procedure user_proc()
begin
	select * from member;
end $$
delimiter ;

call user_proc();


drop procedure if exists user_proc1;
delimiter $$
create procedure user_proc1(in username varchar(10))
begin
	select * from member where mem_name=username;
end $$
delimiter ;

 call user_proc1('블랙핑크');

drop procedure if exists user_proc2;
delimiter $$
create procedure user_proc2(
in usernumber int,
in userheight int)
begin
	select * from member 
		where mem_number > usernumber and height > userheight;
end $$
delimiter ;
 
 call user_proc2(6, 163);
 
 drop procedure if exists user_proc3;

create table if not exists notable(
id int auto_increment primary key,
txt char(10));

 create procedure user_proc3(
	in txtvalue char(10),
    out outvalue int	)
begin
	insert into notable values(null,txtvalue);
	select max(id) into outvalue from notable;
end $$
delimiter ;


    
delimiter $$
create procedure while_proc(
	in startnum int)
begin
	declare hap int;
    declare num int;
    set hap =0;
    set num =startnum;
    
    while(num<=100) do
		set hap=hap+num;
        set num=num+1;
	end while;
    select hap as '1~100 합계';
end $$
delimiter ;

call while_proc(2);
call while_proc(98);

drop procedure if exists dynamic_proc;

delimiter $$
create procedure dynamic_proc(
	in tablename varchar(20))
    begin
		set @sqlq=concat('select * from ', tablename);
        prepare myquery from @sqlq;
        execute myquery;
		deallocate prepare myquery;
	end $$
    delimiter ;
    
call dynamic_proc ('buy');

DROP PROCEDURE IF EXISTS dynamic_proc;
DELIMITER $$
CREATE PROCEDURE dynamic_proc(
    IN tableName VARCHAR(20)
)
BEGIN
  SET @sqlQuery = CONCAT('SELECT * FROM ', tableName);
  PREPARE myQuery FROM @sqlQuery;
  EXECUTE myQuery;
  DEALLOCATE PREPARE myQuery;
END $$
DELIMITER ;

CALL dynamic_proc ('member');

--==;

set global log_bin_trust_function_creators = 1;

use market_db;

drop function if exists sumfunc;

delimiter $$

create function sumfunc(number1 int, number2 int)
	returns int
begin
	return number1 + number2;
end $$
delimiter ;

select sumfunc(100,200) as '합계';
select sum(100+200) as '합계';

drop function if exists calcyearfunc;
delimiter $$
create function calcyearfunc(dyear int)
	returns int
begin
	declare runyear int;
    set runyear =year(curdate())-dyear;
    return runyear;
end $$
delimiter ;

select calcyearfunc(2010) as '활동햇수';
   
drop procedure if exists runy;
delimiter $$
create procedure runy(name1 char(8))
begin
	declare dd int;
	select year(debut_date) into dd from member where name1=mem_name;
    select calcyearfunc(dd) as 활동햇수;
end $$
delimiter ;

call runy('블랙핑크');

select mem_id, mem_name, calcyearfunc(year(debut_date)) as '활동 햇수' from member;

--==;

drop procedure if exists cursor_proc;
delimiter $$
create procedure cursor_proc()
begin
	declare memnumber int;
    declare cnt int default 0;
    declare totnumber int default 0;
    declare endofrow boolean default false;
	
    declare membercursor cursor for
		select mem_number from member;
	
    declare continue handler for
		not found set endofrow = true;
	
    open membercursor;
    
    cursor_loop: loop
		fetch membercursor into memnumber;
        
        if endofrow then
			leave cursor_loop;
		end if;
        
		set cnt = cnt+1;
        set totnumber = totnumber + memnumber;
	end loop cursor_loop;
    
    select (totnumber/cnt) as '회원의 평균 인원 수';
    
    close membercursor;
    
end $$
delimiter ;
        
    call cursor_proc();


--==;

create table if not exists trigger_table (id int, txt varchar(10));
insert into trigger_table values(1, '레드벨벳');
insert into trigger_table values(2, '잇지');
insert into trigger_table values(3, '블랙핑크');

drop trigger if exists mytrigger;
delimiter $$
create trigger mytrigger
	after delete
	on trigger_table
    for each row
    
begin
	set @msg = '가수 그룹이 삭제됨';
end $$
delimiter ;

set @msg = '';

insert into trigger_table values(4,'마마무');

delete from trigger_table where id=4;
select @msg;

create table singer (select mem_id, mem_name, mem_number, addr from member);

drop table if exists backup_singer;
create table if not exists backup_singer
(mem_id char(8) not null,
mem_name varchar(10) not null,
mem_number int not null,
addr char(2) not null,
modtype char(2),
moddate date,
moduser varchar(30));

drop trigger if exists singer_updatetrg
delimiter $$
create trigger singer_updatetrg
	after update
    on singer
    for each row
begin
	insert into backup_singer values(old.mem_id, old.mem_name, old.mem_number, old.addr, '수정', curdate(), current_user());
end $$
delimiter ;

update singer set addr='영국' where mem_id='blk';

select * from backup_singer;

drop trigger if exists singer_updeletetrg
delimiter $$
create trigger singer_updeletetrg
	after delete
    on singer
    for each row
begin
	insert into backup_singer values(old.mem_id, old.mem_name, old.mem_number, old.addr, '삭제', curdate(), current_user());
end $$
delimiter ;

delete from singer where mem_number >=7;

select * from backup_singer;

truncate table singer;
select * from singer;