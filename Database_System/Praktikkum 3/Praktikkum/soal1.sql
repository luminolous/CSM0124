select nama_resepsionis, usia, alamat
from resepsionis
where jenis_kelamin = 'L' and usia = (select min(usia) from resepsionis);