# Compare your discrete ROC curves with other methods
# At terminal: gnuplot contROC.p
set terminal png size 1280, 960 enhanced font 'Verdana,18'
set key font ",12"
set size 1,1
set xtics 500
set ytics 0.1
set grid
set ylabel "True positive rate"
set xlabel "False positive"
set xr [0:2000]
set yr [0:1.0]
# Compare your discrete ROC curves with other methods
# At terminal: gnuplot discROC.p
set key below
set output "tempContROC-MTCNN.png"
plot  "tempContROC.txt" using 2:1 title 'MTCNN' with lines lw 2 , \


 
