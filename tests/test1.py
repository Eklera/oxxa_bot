import re



'I �. ����. �������. �� ���.������� �.�.\nII �. ����. �������.  �� #���-8\n�-226#'



r = re.compile(r"\d+\-\d+")
searchResult = re.match(r, "4-15 �. ����������������")
if searchResult != None:
    rng = [int(x) for x in searchResult.group(0).split('-')]
    print([x for x in range(rng[0], rng[1]+1)])
