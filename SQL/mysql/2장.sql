select * from member;
select member_id from member;
select member_addr, member_id from member;

select member_name, member_addr from member where member_name = '아이유';

select * from member where member_name = '아이유';

create index inx_member_name on member(member_name);

create view member_view as select * from member;

select * from member_view;


delimiter //
create procedure myproc()
begin
	select * from member where member_name = '나훈아' ;
	select * from product where product_name = '삼각김밥' ;
end //
delimiter ;

call myproc();