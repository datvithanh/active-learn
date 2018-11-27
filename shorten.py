import csv

with open('FaceImageCroppedWithAlignment.tsv') as input_tsv:
    reader = csv.reader(input_tsv, delimiter='\t')
    with open('shorten.tsv', 'wt') as output_tsv:
        writer = csv.writer(output_tsv, delimiter='\t')
        count = 0
        for row in reader:
            writer.writerow(row)
            count += 1
            if count % 10000 == 0:
                print(count)
            if count >= 400000:
                break
