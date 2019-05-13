# Bandit Level 12

```bash
Username: bandit12
Password: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
Server:   bandit.labs.overthewire.org
Port:     2220
```

Lets connect to the server:
```bash
ssh bandit12@bandit.labs.overthewire.org -p2220
```

First, lets take a look on the hexdump:
```bash
bandit12@bandit:~$ cat data.txt 
00000000: 1f8b 0808 d7d2 c55b 0203 6461 7461 322e  .......[..data2.
00000010: 6269 6e00 013c 02c3 fd42 5a68 3931 4159  bin..<...BZh91AY
00000020: 2653 591d aae5 9800 001b ffff de7f 7fff  &SY.............
00000030: bfb7 dfcf 9fff febf f5ad efbf bbdf 7fdb  ................
00000040: f2fd ffdf effa 7fff fbd7 bdff b001 398c  ..............9.
00000050: 1006 8000 0000 0d06 9900 0000 6834 000d  ............h4..
00000060: 01a1 a000 007a 8000 0d00 0006 9a00 d034  .....z.........4
00000070: 0d1a 3234 68d1 e536 a6d4 4000 341a 6200  ..24h..6..@.4.b.
00000080: 0069 a000 0000 0000 d003 d200 681a 0d00  .i..........h...
00000090: 0001 b51a 1a0c 201e a000 6d46 8068 069a  ...... ...mF.h..
000000a0: 6834 340c a7a8 3406 4000 0680 0001 ea06  h44...4.@.......
000000b0: 8190 03f5 4032 1a00 0343 4068 0000 0686  ....@2...C@h....
000000c0: 8000 0320 00d0 0d00 0610 0014 1844 0308  ... .........D..
000000d0: 04e1 c542 9ab8 2c30 f1be 0b93 763b fb13  ...B..,0....v;..
000000e0: 50c4 c101 e008 3b7a 92a7 9eba 8a73 8d21  P.....;z.....s.!
000000f0: 9219 9c17 052b fb66 a2c2 fccc 9719 b330  .....+.f.......0
00000100: 6068 8c65 e504 5ec0 ae02 fa6d 16bc 904b  `h.e..^....m...K
00000110: ba6c f692 356e c02b 0374 c394 6859 f5bb  .l..5n.+.t..hY..
00000120: 0f9f 528e 4272 22bb 103c 2848 d8aa 2409  ..R.Br"..<(H..$.
00000130: 24d0 d4c8 4b42 7388 ce25 6c1a 7ec1 5f17  $...KBs..%l.~._.
00000140: cc18 ddbf edc1 e3a4 67f1 7a4d 8277 c823  ........g.zM.w.#
00000150: 0450 2232 40e0 07f1 ca16 c6d6 ef0d ecc9  .P"2@...........
00000160: 8bc0 5e2d 4b12 8586 088e 8ca0 e67d a55c  ..^-K........}.\
00000170: 2ca0 18c7 bfb7 7d45 9346 ea5f 2172 01e4  ,.....}E.F._!r..
00000180: 5598 673f 45af 69b7 a739 7814 8706 04ed  U.g?E.i..9x.....
00000190: 5442 1240 0796 6cc8 b2f6 1ef9 8d13 421d  TB.@..l.......B.
000001a0: 461f 2e68 4d91 5343 34b5 56e7 46d0 0a0a  F..hM.SC4.V.F...
000001b0: 72b7 d873 71d9 6f09 c326 402d dbc0 7cef  r..sq.o..&@-..|.
000001c0: 53b1 df60 9ec7 f318 00df 3907 2e85 d85b  S..`......9....[
000001d0: 6a1a e105 0207 c580 e31d 82d5 8646 183c  j............F.<
000001e0: 6a04 4911 101a 5427 087c 1f94 47a2 270d  j.I...T'.|..G.'.
000001f0: ad12 fc5c 9ad2 5714 514f 34ba 701d fb69  ...\..W.QO4.p..i
00000200: 8eed 0183 e2a1 53ea 2300 26bb bd2f 13df  ......S.#.&../..
00000210: b703 08a3 2309 e43c 44bf 75d4 905e 5f96  ....#..<D.u..^_.
00000220: 481b 362e e82d 9093 7741 740c e65b c7f1  H.6..-..wAt..[..
00000230: 5550 f247 9043 5097 d626 3a16 da32 c213  UP.G.CP..&:..2..
00000240: 2acd 298a 5c8a f0c1 b99f e2ee 48a7 0a12  *.).\.......H...
00000250: 03b5 5cb3 0037 cece 773c 0200 00         ..\..7..w<...
```

We can revert it bach using ```xxd```:
```bash
bandit12@bandit:~$ mktemp -d
/tmp/tmp.6ZBnLKOc7R
bandit12@bandit:~$ xxd -r data.txt > /tmp/tmp.6ZBnLKOc7R/data
bandit12@bandit:~$ file /tmp/tmp.6ZBnLKOc7R/data
/tmp/tmp.6ZBnLKOc7R/data: gzip compressed data, was "data2.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
```

Now we need to repeatedly uncompress the file using the appropriate tool:
```bash
bandit12@bandit:/tmp/tmp.6ZBnLKOc7R$ xxd -r ~/data.txt > ./data
bandit12@bandit:/tmp/tmp.6ZBnLKOc7R$ file *
data: gzip compressed data, was "data2.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
bandit12@bandit:/tmp/tmp.6ZBnLKOc7R$ mv data data.gz; gunzip data.gz; file *
data: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/tmp.6ZBnLKOc7R$ mv data data.bz2; bunzip2 data.bz2; file *
data: gzip compressed data, was "data4.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
bandit12@bandit:/tmp/tmp.6ZBnLKOc7R$ mv data data.gz; gunzip data.gz; file *
data: POSIX tar archive (GNU)
bandit12@bandit:/tmp/tmp.6ZBnLKOc7R$ mv data data.tar; tar -xf data.tar; file *
data5.bin: POSIX tar archive (GNU)
data.tar:  POSIX tar archive (GNU)
bandit12@bandit:/tmp/tmp.6ZBnLKOc7R$ mv data5.bin data.tar; tar -xf data.tar; file *
data6.bin: bzip2 compressed data, block size = 900k
data.tar:  POSIX tar archive (GNU)
bandit12@bandit:/tmp/tmp.6ZBnLKOc7R$ mv data6.bin data.bz2; bunzip2 data.bz2; file *
data:     POSIX tar archive (GNU)
data.tar: POSIX tar archive (GNU)
bandit12@bandit:/tmp/tmp.6ZBnLKOc7R$ mv data data.tar; tar -xf data.tar; file *
data8.bin: gzip compressed data, was "data9.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
data.tar:  POSIX tar archive (GNU)
bandit12@bandit:/tmp/tmp.6ZBnLKOc7R$ mv data8.bin data.gz; gunzip data.gz; file *
data:     ASCII text
data.tar: POSIX tar archive (GNU)
bandit12@bandit:/tmp/tmp.6ZBnLKOc7R$ cat data
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```

We got the password for the next level: **8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL**

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *
import tempfile


def main():
    shell = ssh(host='bandit.labs.overthewire.org',
                user='bandit12',
                password='5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu',
                port=2220
           )

    org = tempfile.NamedTemporaryFile()
    org.write(shell['cat data.txt'])
    org.seek(0)

    unhexified = tempfile.NamedTemporaryFile()
    proc = subprocess.Popen(['xxd', '-r', org.name], stdout=subprocess.PIPE)
    unhexified.write(proc.stdout.read())
    unhexified.seek(0)

    proc = subprocess.Popen(['file', unhexified.name], stdout=subprocess.PIPE)
    file_prop = proc.stdout.read()
    i = 0
    print "File %d\t%s" % (i, file_prop.replace('\n', ''))
    i += 1

    files_to_delete = []
    ext0 = unhexified
    ext0.seek(0)
    while True:
        if 'gzip compressed data' in file_prop:
            ext1 = tempfile.NamedTemporaryFile(suffix = '.gz')
            ext1.write(ext0.read())
            ext1.flush()
            subprocess.call(['gunzip', '-k', ext1.name])
            new_file = ext1.name.split('.')[0]
            files_to_delete.append(new_file)
        elif 'bzip2 compressed data' in file_prop:
            ext1 = tempfile.NamedTemporaryFile(suffix = '.bz2')
            ext1.write(ext0.read())
            ext1.flush()
            subprocess.call(['bunzip2', '-k', ext1.name])
            new_file = ext1.name.split('.')[0]
            files_to_delete.append(new_file)
        elif 'POSIX tar archive' in file_prop:
            ext1 = tempfile.NamedTemporaryFile(suffix = '.tar')
            ext1.write(ext0.read())
            ext1.flush()
            proc = subprocess.Popen(['tar', '-tf', ext1.name], stdout=subprocess.PIPE)
            new_file = proc.stdout.read().replace('\n','')
            subprocess.call(['tar', '-xf', ext1.name])
            files_to_delete.append(new_file)
        else:
            subprocess.call(['cat', ext0.name])
            break

        proc = subprocess.Popen(['file', new_file], stdout=subprocess.PIPE)
        file_prop = proc.stdout.read()
        print "File %d\t%s" % (i, file_prop.replace('\n', ''))
        i += 1

        ext0 = open(new_file, 'r')
        ext0.seek(0)

    for f in files_to_delete:
        os.remove(f)

if __name__ == "__main__":
    main()
```