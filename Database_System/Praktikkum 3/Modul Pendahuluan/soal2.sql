select A_ThnLulus, count(*) as Jumlah_Alumni
from alumni 
where A_ThnLulus in (2010, 2012)
group by A_ThnLulus;