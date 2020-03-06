import csv

# bench execute vet_care.scripts.filter_from_history.execute --args "['./data/new_history.csv', './data/filtered.csv']"
def execute(input, output):
    filters = ['10339', '8347', '10545', '10395', '10421', '10428', '10527', '10544', '10594', '10308', '10442', '10497', '10398', '10360', '10383', '10574', '10573', '6412', '10198', '10500', '10612', '10389', '10534', '10377', '10495', '5467', '10280', '10590', '10439', '10307', '10349', '10482', '10490', '10508', '10208', '6743', '4684', '6200', '6462', '6166', '10529', '10240', '10609', '10524', '10419', '6171', '10394', '10509','10546', '9449', '10445', '10272', '10352', '10418', '10449', '10481', '10229', '10523', '10564', '10581', '8691', '10521', '10579', '10532', '10364', '10399', '10446', '10311', '10355', '10384', '10200', '10402', '10353', '10553', '10405', '10366', '10344', '10380', '10557', '10197', '10302', '9993', '10491', '10560', '1362', '10518', '10417', '10576', '10561', '10358', '10605', '10347', '10456', '10567', '10345', '10241', '10212', '10512', '10541', '10578', '10484', '10453', '10370', '10531', '10327', '9200', '6978', '10463', '10516', '10464', '10479', '10589', '10404', '10415', '10451', '10469', '10407', '10457', '10489', '10336', '10412', '10494', '10305', '10357', '10361', '10539', '6461', '10362', '4900', '10461', '1683', '10354', '1530', '10492', '7255', '10288', '10519', '10458', '10477', '10601', '10375', '10416', '10247', '10599', '10540', '10435', '10562', '10350', '10317', '10450', '9432', '10409', '10237', '10422', '10365', '10517', '6606', '10502', '10606', '10283', '10207', '10485', '10533', '10452', '10447', '10568', '10255', '10499', '10569', '10572', '10410', '10386', '10455', '10543', '10535', '10218', '10228', '10520', '10387','10379', '8385', '10429', '10341', '10329', '10299', '10507', '10513', '10585', '10401', '10514', '10356', '10199', '10382', '10397', '10608', '10420', '10231', '10454', '10448', '10475', '10511', '10551', '10423', '10467', '10570', '10433', '10434', '10369', '10501', '10462', '10525', '10367', '4947', '10459', '10338', '10542', '10571', '18', '10530', '10483', '10390', '10476', '10330', '10411', '10337', '10351', '10465', '10496', '10371', '10372', '10265', '10406', '10259', '10413', '9762', '10558', '10460', '10333', '10374', '10488', '6834', '10480', '10378', '10522', '10468', '10385', '10431', '10505', '10408', '10432', '10393', '10444', '10340', '10528', '938', '10515', '10196', '10575', '10216', '10388', '10582', '10396', '10440', '10506', '10607', '10441', '10611', '4806', '10586', '10595', '7315', '10343', '10310', '10342', '10335', '10436', '5201', '10430', '10584', '10588', '10591', '10427', '10373', '10437', '9594', '10610', '10376', '10236', '10392', '10587', '10603', '10493', '10604', '10583', '10478', '10169', '10163']
    filtered_items = []
    fieldnames = []
    with open(input, 'r') as inputfile:
        reader = csv.DictReader(inputfile)
        fieldnames = reader.fieldnames
        for row in reader:
            id = row.get('AnimalID')
            if id in filters:
                filtered_items.append(dict(row))

    with open(output, 'w') as outputfile:
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in filtered_items:
            writer.writerow(item)
