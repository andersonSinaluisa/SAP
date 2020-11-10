


select * from public.account_voucher;

select * from public.account_voucher_line;

select * from public.account_invoice;

select * from public.account_move;

select * from public.account_move_line;


select vl.amount_unreconciled from public.account_voucher_line as vl join public.account_move_line as ml 
on vl.move_line_id = ml.id join public.account_invoice as ai on ai.move_id = ml.move_id where ai.id = 142 group by vl.amount_unreconciled;
