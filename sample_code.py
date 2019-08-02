import csv

with open(r'C:\Users\n98196\Downloads\Obul_task-master\VM-PP-AUTO-20190723-051641.txt.rex', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #csv_reader.next() skips the headers 
    csv_reader.next()
    csv_reader.next()
    header = csv_reader.next()
    h_list = header[0].split()


    csv_reader.next()
    csv_reader.next()
    csv_reader.next()

    lines = list(csv_reader)
    print(len(lines))
    #Extracting the date from the csv file
    dt=lines[0][6][:lines[0][6].index(" ")]
    # Getting required headder columns
    s = (h_list[3] + "," + h_list[5] + "," + h_list[7]+"_"+dt).split(",")
    print(s)

with open('output_file.csv', mode='wb') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(s)
    for row in lines:
        csv_writer.writerow((row[2], row[4], row[6][:row[6].index(" ")]))

