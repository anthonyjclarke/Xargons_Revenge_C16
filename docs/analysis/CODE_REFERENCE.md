# Generated Code Reference

## Method and Limits

Generated from original normalized modules, linker symbols and listing PCs. Logical line numbers refer to the preserved module after CR/CRLF splitting, not the flattened assembly. Labels include branch points, data, equates and alternate entries; they are not all functions. Module allocations include embedded data. Direct transfers omit fall-through, indirect vectors, runtime patches and nonlocal stack control. Data spans stop at the next greater symbol address and retain raw byte order; their field semantics require reading the source.

---

## Assembly Order and Allocation

| Module             | Bytes | Lines | Origin |
| ------------------ | ----- | ----- | ------ |
| `REVENGE`          | 37    | 123   | 2026   |
| `MAIN-VARS`        | 0     | 63    | 2026   |
| `VARS`             | 0     | 179   | 2026   |
| `EXTRA-MEMORY`     | 0     | 41    | 2026   |
| `LEVEL-CODE`       | 820   | 321   | 2026   |
| `EXPLOSIONS`       | 83    | 94    | 2026   |
| `COMPLETED-SHEET`  | 384   | 320   | 1992   |
| `INIT-SHEET`       | 68    | 65    | 2026   |
| `SET-SHEET`        | 199   | 201   | 2026   |
| `ALIEN-CODE`       | 420   | 420   | 2026   |
| `RESET-CODE`       | 148   | 103   | 2026   |
| `FIZZLE`           | 87    | 82    | 2026   |
| `GAME-OVER`        | 105   | 93    | 2026   |
| `DEATH-CODE`       | 60    | 50    | 2026   |
| `CHAR-ANIM`        | 29    | 34    | 2026   |
| `DATA-LAND/CHARS`  | 64    | 20    | 1992   |
| `SOUND-EFFECTS`    | 379   | 408   | 2026   |
| `RASTER-ROUTINES`  | 240   | 205   | 1992   |
| `HIGH-SCORE`       | 106   | 86    | 2026   |
| `ALTERABLES`       | 245   | 167   | 2026   |
| `LAND-GO`          | 18    | 24    | 2026   |
| `STARTER`          | 170   | 152   | 2026   |
| `FUEL-CHAR/DATA`   | 48    | 15    | 2026   |
| `FUEL-CODE`        | 267   | 257   | 2026   |
| `PRINT-LIVES`      | 55    | 70    | 2026   |
| `PAUSE/ESCAPE`     | 150   | 148   | 2026   |
| `PULSATE`          | 30    | 29    | 2026   |
| `BANNER-DATA`      | 320   | 48    | 2026   |
| `TITLE-WORK`       | 212   | 238   | 2026   |
| `TITLE-LOOP`       | 98    | 87    | 2026   |
| `TITLE-GENERATE`   | 44    | 48    | 2026   |
| `TV-PICTURE`       | 117   | 106   | 2026   |
| `IRQ`              | 94    | 114   | 2026   |
| `JOYSTIK`          | 62    | 72    | 2026   |
| `KEY-SCAN`         | 46    | 67    | 2026   |
| `UTILS`            | 170   | 155   | 2026   |
| `PLAY-GAME`        | 121   | 103   | 2026   |
| `WHOOPPEE-MESSAGE` | 328   | 21    | 1992   |
| `MESSAGE-STUFF`    | 59    | 73    | 2026   |
| `STAR-CODE`        | 229   | 234   | 2026   |
| `TOPLAND-PIXEL`    | 110   | 118   | 2026   |
| `BOTLAND-PIXEL`    | 138   | 135   | 2026   |
| `MOVE-SHIP`        | 175   | 178   | 2026   |
| `SHIP-CALCS`       | 120   | 142   | 2026   |
| `TABLES`           | 99    | 56    | 2026   |
| `FIRING-MEGA/CODE` | 134   | 145   | 1992   |
| `SCREEN-SETUP`     | 261   | 266   | 2026   |
| `FUEL-GAUGE`       | 232   | 239   | 2026   |
| `SHTABLE`          | 128   | 220   | 2026   |
| `ALI-PRINT&CLEAR`  | 60    | 65    | 1992   |
| `SHIP-DEF`         | 64    | 17    | 2026   |
| `SCORE-ROUTINES`   | 152   | 153   | 2026   |
| `SHEET1`           | 12    | 21    | 2026   |
| `SHEET2`           | 12    | 21    | 2026   |
| `SHEET3`           | 22    | 23    | 2026   |
| `SHEET4`           | 17    | 22    | 2026   |
| `SHEET5`           | 33    | 24    | 2026   |
| `SHEET6`           | 22    | 22    | 2026   |
| `SHEET7`           | 21    | 23    | 2026   |
| `SHEET8`           | 18    | 22    | 2026   |
| `SHEET9`           | 17    | 22    | 2026   |
| `SHEETA`           | 22    | 22    | 2026   |
| `SHEETB`           | 18    | 22    | 2026   |
| `SHEETC`           | 19    | 22    | 2026   |
| `SHEETD`           | 18    | 22    | 2026   |
| `SHEETE`           | 25    | 22    | 2026   |
| `SHEETF`           | 21    | 22    | 2026   |
| `SHEETG`           | 12    | 21    | 2026   |

---

## Variables and Reserved Memory

| Symbol   | Address | Bytes | Line |
| -------- | ------- | ----- | ---- |
| `INTYPE` | `$0002` | 1     | 7    |
| `TOPLX`  | `$0003` | 1     | 9    |
| `BOTLX`  | `$0004` | 1     | 10   |
| `TOPWRK` | `$0005` | 1     | 12   |
| `BOTWRK` | `$0006` | 1     | 13   |
| `TOPCNT` | `$0007` | 1     | 15   |
| `BOTCNT` | `$0008` | 1     | 16   |
| `TOPCHR` | `$0009` | 1     | 17   |
| `BOTCHR` | `$000A` | 1     | 18   |
| `LANDAN` | `$000B` | 1     | 20   |
| `BAKCOL` | `$000C` | 1     | 22   |
| `MESL`   | `$000D` | 2     | 24   |
| `MESSX`  | `$000F` | 1     | 25   |
| `STOP`   | `$0010` | 1     | 27   |
| `STPSTR` | `$0011` | 1     | 28   |
| `DNTFIR` | `$0012` | 1     | 30   |
| `COLVAR` | `$0013` | 1     | 32   |
| `SCORCT` | `$0014` | 1     | 33   |
| `CTLFUL` | `$0015` | 1     | 35   |
| `MAGERS` | `$0016` | 1     | 36   |
| `MPGVAL` | `$0017` | 1     | 38   |
| `BONUS`  | `$0018` | 2     | 40   |
| `KILLCO` | `$001A` | 1     | 42   |
| `JUP`    | `$001B` | 1     | 44   |
| `JDOWN`  | `$001C` | 1     | 45   |
| `JFIRE`  | `$001D` | 1     | 46   |
| `JMOVE`  | `$001E` | 1     | 47   |
| `PAUSE`  | `$001F` | 1     | 49   |
| `DEAD`   | `$0020` | 1     | 51   |
| `WELLY`  | `$0021` | 1     | 53   |
| `TITLE`  | `$0022` | 1     | 55   |
| `SCRDIR` | `$0023` | 1     | 56   |
| `SHPINK` | `$0024` | 1     | 58   |
| `RND`    | `$0025` | 4     | 60   |
| `PULSE`  | `$0029` | 1     | 61   |
| `SCRADD` | `$002A` | 1     | 63   |
| `SL`     | `$002B` | 2     | 65   |
| `SCR`    | `$002D` | 2     | 66   |
| `CL`     | `$002F` | 2     | 67   |
| `COL`    | `$0031` | 2     | 68   |
| `IRQWRK` | `$0033` | 8     | 70   |
| `WORK`   | `$003B` | 10    | 71   |
| `LASTON` | `$0045` | 1     | 73   |
| `PICHIT` | `$0046` | 1     | 74   |
| `CLY`    | `$0047` | 1     | 76   |
| `LIVES`  | `$0048` | 1     | 78   |
| `TX`     | `$0049` | 1     | 80   |
| `TY`     | `$004A` | 1     | 81   |
| `SPEED`  | `$004B` | 1     | 82   |
| `NUMB`   | `$004C` | 1     | 83   |
| `STCOL`  | `$004D` | 1     | 84   |
| `YPIX`   | `$004E` | 1     | 86   |
| `SHIPY`  | `$004F` | 1     | 87   |
| `CHAR`   | `$0050` | 1     | 88   |
| `SHIPC1` | `$0051` | 1     | 89   |
| `SHIPC2` | `$0052` | 1     | 90   |
| `SHPSCR` | `$0053` | 2     | 91   |
| `SHPCOL` | `$0055` | 2     | 92   |
| `LASERS` | `$0057` | 1     | 94   |
| `LAS`    | `$0058` | 2     | 95   |
| `LAZX`   | `$005A` | 1     | 96   |
| `LAZY`   | `$005B` | 1     | 97   |
| `FIRCNT` | `$005C` | 1     | 98   |
| `OLDFIR` | `$005D` | 1     | 99   |
| `FUELX`  | `$005E` | 1     | 101  |
| `FUELY`  | `$005F` | 1     | 102  |
| `FUELON` | `$0060` | 1     | 103  |
| `FULDIR` | `$0061` | 1     | 104  |
| `FUELTM` | `$0062` | 1     | 105  |
| `FULINC` | `$0063` | 1     | 106  |
| `FULCOL` | `$0064` | 1     | 107  |
| `FULDWN` | `$0065` | 1     | 108  |
| `KILFUL` | `$0066` | 1     | 109  |
| `LANCL1` | `$0067` | 1     | 111  |
| `LANCL2` | `$0068` | 1     | 112  |
| `LANCL3` | `$0069` | 1     | 113  |
| `FUEL`   | `$006A` | 1     | 115  |
| `FUTEM`  | `$006B` | 1     | 116  |
| `DL`     | `$006C` | 2     | 118  |
| `PATD`   | `$006E` | 2     | 119  |
| `ALISPD` | `$0070` | 1     | 121  |
| `REGEN`  | `$0071` | 1     | 122  |
| `NUMALI` | `$0072` | 1     | 123  |
| `SHEET`  | `$0073` | 1     | 124  |
| `LEVEL`  | `$0074` | 1     | 125  |
| `ATTAK`  | `$0075` | 1     | 126  |
| `ALTEM`  | `$0076` | 1     | 128  |
| `NOBBO`  | `$0077` | 1     | 129  |
| `ALIPNT` | `$0078` | 1     | 130  |
| `ALIDIR` | `$0079` | 1     | 131  |
| `ALIHIT` | `$007A` | 1     | 132  |
| `ALX`    | `$007B` | 1     | 133  |
| `ALY`    | `$007C` | 1     | 134  |
| `ALCHR`  | `$007D` | 1     | 135  |
| `GNKCOL` | `$007E` | 1     | 136  |
| `HITIT`  | `$007F` | 1     | 138  |
| `TEMP1`  | `$0080` | 1     | 140  |
| `TEMP2`  | `$0081` | 1     | 141  |
| `TEMP3`  | `$0082` | 1     | 142  |
| `TEMP4`  | `$0083` | 1     | 143  |
| `MESSPD` | `$0084` | 1     | 145  |
| `TOPSPD` | `$0085` | 1     | 146  |
| `BOTSPD` | `$0086` | 1     | 147  |
| `SCRBUF` | `$0087` | 8     | 149  |
| `STSTOP` | `$008F` | 4     | 151  |
| `STFLAG` | `$0093` | 1     | 152  |
| `FXNUMB` | `$0094` | 1     | 154  |
| `FXCONT` | `$0095` | 1     | 155  |
| `FXTEMP` | `$0096` | 2     | 156  |
| `FXWORK` | `$0098` | 2     | 157  |
| `VOLCTL` | `$009A` | 1     | 158  |
| `XTEMP`  | `$009B` | 1     | 160  |
| `XTRA`   | `$009C` | 1     | 161  |
| `DTEMP`  | `$009D` | 1     | 163  |
| `ALIXPS` | `$009E` | 16    | 167  |
| `ALIYPS` | `$00AE` | 16    | 168  |
| `ALIIND` | `$00BE` | 16    | 169  |
| `ALSTAT` | `$00CE` | 16    | 170  |
| `STARXP` | `$00DE` | 16    | 172  |
| `STARYP` | `$00EE` | 16    | 173  |
| `ALICOL` | `$0200` | 16    | 14   |
| `STARSP` | `$0210` | 16    | 22   |
| `BIGBUF` | `$0220` | 160   | 30   |

---

## Symbols and Preserved Source Locations

### REVENGE

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/023_REVENGE.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind |
| -------- | ------- | ---- | ---- |
| `JOYSEL` | `$1824` | 49   | data |
| `SNDFLG` | `$1823` | 48   | data |

### MAIN-VARS

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/024_MAIN-VARS.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind   |
| -------- | ------- | ---- | ------ |
| `ALDATA` | `$0400` | 58   | equate |
| `ALINUM` | `$0010` | 46   | equate |
| `BACKGR` | `$FF15` | 13   | equate |
| `BORDER` | `$FF19` | 14   | equate |
| `COLSH1` | `$002A` | 42   | equate |
| `FULCHR` | `$3DA0` | 50   | equate |
| `IRQMSK` | `$FF0A` | 9    | equate |
| `IRQREG` | `$FF09` | 8    | equate |
| `JPORT`  | `$FF08` | 16   | equate |
| `LAZCHR` | `$39F8` | 34   | equate |
| `MULTI1` | `$FF16` | 18   | equate |
| `MULTI2` | `$FF17` | 19   | equate |
| `RASCOM` | `$FF0B` | 10   | equate |
| `RASTHI` | `$FF1C` | 11   | equate |
| `SCORPS` | `$0C06` | 38   | equate |
| `SHIPCH` | `$3BE0` | 30   | equate |
| `SOU1HI` | `$FF12` | 23   | equate |
| `SOU1LO` | `$FF0E` | 21   | equate |
| `SOU2HI` | `$FF10` | 24   | equate |
| `SOU2LO` | `$FF0F` | 22   | equate |
| `STARNM` | `$0010` | 48   | equate |
| `TED`    | `$FF00` | 6    | equate |
| `VOL`    | `$FF11` | 26   | equate |
| `WRIGHT` | `$0DEB` | 54   | equate |

### VARS

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/068_VARS.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind     |
| -------- | ------- | ---- | -------- |
| `ALCHR`  | `$007D` | 135  | reserved |
| `ALIDIR` | `$0079` | 131  | reserved |
| `ALIHIT` | `$007A` | 132  | reserved |
| `ALIIND` | `$00BE` | 169  | reserved |
| `ALIPNT` | `$0078` | 130  | reserved |
| `ALISPD` | `$0070` | 121  | reserved |
| `ALIXPS` | `$009E` | 167  | reserved |
| `ALIYPS` | `$00AE` | 168  | reserved |
| `ALSTAT` | `$00CE` | 170  | reserved |
| `ALTEM`  | `$0076` | 128  | reserved |
| `ALX`    | `$007B` | 133  | reserved |
| `ALY`    | `$007C` | 134  | reserved |
| `ATTAK`  | `$0075` | 126  | reserved |
| `BAKCOL` | `$000C` | 22   | reserved |
| `BONUS`  | `$0018` | 40   | reserved |
| `BOTCHR` | `$000A` | 18   | reserved |
| `BOTCNT` | `$0008` | 16   | reserved |
| `BOTLX`  | `$0004` | 10   | reserved |
| `BOTSPD` | `$0086` | 147  | reserved |
| `BOTWRK` | `$0006` | 13   | reserved |
| `CHAR`   | `$0050` | 88   | reserved |
| `CL`     | `$002F` | 67   | reserved |
| `CLY`    | `$0047` | 76   | reserved |
| `COL`    | `$0031` | 68   | reserved |
| `COLVAR` | `$0013` | 32   | reserved |
| `CTLFUL` | `$0015` | 35   | reserved |
| `DEAD`   | `$0020` | 51   | reserved |
| `DL`     | `$006C` | 118  | reserved |
| `DNTFIR` | `$0012` | 30   | reserved |
| `DTEMP`  | `$009D` | 163  | reserved |
| `FIRCNT` | `$005C` | 98   | reserved |
| `FUEL`   | `$006A` | 115  | reserved |
| `FUELON` | `$0060` | 103  | reserved |
| `FUELTM` | `$0062` | 105  | reserved |
| `FUELX`  | `$005E` | 101  | reserved |
| `FUELY`  | `$005F` | 102  | reserved |
| `FULCOL` | `$0064` | 107  | reserved |
| `FULDIR` | `$0061` | 104  | reserved |
| `FULDWN` | `$0065` | 108  | reserved |
| `FULINC` | `$0063` | 106  | reserved |
| `FUTEM`  | `$006B` | 116  | reserved |
| `FXCONT` | `$0095` | 155  | reserved |
| `FXNUMB` | `$0094` | 154  | reserved |
| `FXTEMP` | `$0096` | 156  | reserved |
| `FXWORK` | `$0098` | 157  | reserved |
| `GNKCOL` | `$007E` | 136  | reserved |
| `HITIT`  | `$007F` | 138  | reserved |
| `INTYPE` | `$0002` | 7    | reserved |
| `IRQWRK` | `$0033` | 70   | reserved |
| `JDOWN`  | `$001C` | 45   | reserved |
| `JFIRE`  | `$001D` | 46   | reserved |
| `JMOVE`  | `$001E` | 47   | reserved |
| `JUP`    | `$001B` | 44   | reserved |
| `KILFUL` | `$0066` | 109  | reserved |
| `KILLCO` | `$001A` | 42   | reserved |
| `LANCL1` | `$0067` | 111  | reserved |
| `LANCL2` | `$0068` | 112  | reserved |
| `LANCL3` | `$0069` | 113  | reserved |
| `LANDAN` | `$000B` | 20   | reserved |
| `LAS`    | `$0058` | 95   | reserved |
| `LASERS` | `$0057` | 94   | reserved |
| `LASTON` | `$0045` | 73   | reserved |
| `LAZX`   | `$005A` | 96   | reserved |
| `LAZY`   | `$005B` | 97   | reserved |
| `LEVEL`  | `$0074` | 125  | reserved |
| `LIVES`  | `$0048` | 78   | reserved |
| `MAGERS` | `$0016` | 36   | reserved |
| `MESL`   | `$000D` | 24   | reserved |
| `MESSPD` | `$0084` | 145  | reserved |
| `MESSX`  | `$000F` | 25   | reserved |
| `MPGVAL` | `$0017` | 38   | reserved |
| `NOBBO`  | `$0077` | 129  | reserved |
| `NUMALI` | `$0072` | 123  | reserved |
| `NUMB`   | `$004C` | 83   | reserved |
| `OLDFIR` | `$005D` | 99   | reserved |
| `PATD`   | `$006E` | 119  | reserved |
| `PAUSE`  | `$001F` | 49   | reserved |
| `PICHIT` | `$0046` | 74   | reserved |
| `PULSE`  | `$0029` | 61   | reserved |
| `REGEN`  | `$0071` | 122  | reserved |
| `RND`    | `$0025` | 60   | reserved |
| `SCORCT` | `$0014` | 33   | reserved |
| `SCR`    | `$002D` | 66   | reserved |
| `SCRADD` | `$002A` | 63   | reserved |
| `SCRBUF` | `$0087` | 149  | reserved |
| `SCRDIR` | `$0023` | 56   | reserved |
| `SHEET`  | `$0073` | 124  | reserved |
| `SHIPC1` | `$0051` | 89   | reserved |
| `SHIPC2` | `$0052` | 90   | reserved |
| `SHIPY`  | `$004F` | 87   | reserved |
| `SHPCOL` | `$0055` | 92   | reserved |
| `SHPINK` | `$0024` | 58   | reserved |
| `SHPSCR` | `$0053` | 91   | reserved |
| `SL`     | `$002B` | 65   | reserved |
| `SPEED`  | `$004B` | 82   | reserved |
| `STARXP` | `$00DE` | 172  | reserved |
| `STARYP` | `$00EE` | 173  | reserved |
| `STCOL`  | `$004D` | 84   | reserved |
| `STFLAG` | `$0093` | 152  | reserved |
| `STOP`   | `$0010` | 27   | reserved |
| `STPSTR` | `$0011` | 28   | reserved |
| `STSTOP` | `$008F` | 151  | reserved |
| `TEMP1`  | `$0080` | 140  | reserved |
| `TEMP2`  | `$0081` | 141  | reserved |
| `TEMP3`  | `$0082` | 142  | reserved |
| `TEMP4`  | `$0083` | 143  | reserved |
| `TITLE`  | `$0022` | 55   | reserved |
| `TOPCHR` | `$0009` | 17   | reserved |
| `TOPCNT` | `$0007` | 15   | reserved |
| `TOPLX`  | `$0003` | 9    | reserved |
| `TOPSPD` | `$0085` | 146  | reserved |
| `TOPWRK` | `$0005` | 12   | reserved |
| `TX`     | `$0049` | 80   | reserved |
| `TY`     | `$004A` | 81   | reserved |
| `VOLCTL` | `$009A` | 158  | reserved |
| `WELLY`  | `$0021` | 53   | reserved |
| `WORK`   | `$003B` | 71   | reserved |
| `XTEMP`  | `$009B` | 160  | reserved |
| `XTRA`   | `$009C` | 161  | reserved |
| `YPIX`   | `$004E` | 86   | reserved |

### EXTRA-MEMORY

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/011_EXTRA-MEMORY.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind     |
| -------- | ------- | ---- | -------- |
| `ALICOL` | `$0200` | 14   | reserved |
| `BIGBUF` | `$0220` | 30   | reserved |
| `STARSP` | `$0210` | 22   | reserved |

### LEVEL-CODE

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/033_LEVEL-CODE.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `AGAINP` | `$18DE` | 150  | instruction-label |
| `DODO1`  | `$1889` | 83   | instruction-label |
| `ENDIT1` | `$18B0` | 117  | instruction-label |
| `ENDLVL` | `$1897` | 98   | instruction-label |
| `HATE1`  | `$183C` | 30   | instruction-label |
| `LEVCTL` | `$1825` | 7    | instruction-label |
| `LVL1`   | `$18FF` | 168  | data              |
| `LVL2`   | `$19DC` | 189  | data              |
| `MED1`   | `$1B3D` | 294  | instruction-label |
| `MEDAL`  | `$1B37` | 287  | instruction-label |
| `MESP1`  | `$1AE3` | 206  | instruction-label |
| `MESP2`  | `$1AF4` | 221  | instruction-label |
| `MESP3`  | `$1B0F` | 246  | instruction-label |
| `MESP4`  | `$1B15` | 253  | instruction-label |
| `NEWLIN` | `$1B18` | 257  | instruction-label |
| `NIWCOL` | `$1B2B` | 274  | instruction-label |
| `NOBBE1` | `$1940` | 174  | data              |
| `NOBBE2` | `$19B6` | 181  | data              |
| `NOTENL` | `$1835` | 22   | instruction-label |
| `PLANNM` | `$18E1` | 156  | data              |
| `PRTMES` | `$1AE0` | 202  | instruction-label |
| `TROKIT` | `$18CC` | 136  | instruction-label |

### EXPLOSIONS

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/072_EXPLOSIONS.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `CALEXP` | `$1B59` | 7    | instruction-label |
| `EXP1`   | `$1B67` | 25   | instruction-label |
| `EXP2`   | `$1B79` | 44   | instruction-label |
| `EXP3`   | `$1B7B` | 48   | instruction-label |
| `EXP4`   | `$1B97` | 73   | instruction-label |
| `EXPLOP` | `$1B5D` | 12   | instruction-label |

### COMPLETED-SHEET

[Preserved input](../../Original%20Source%20Recovered/1992/DISK9/COMPLETE.TXT). Logical lines use this module; origin: 1992 fallback.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `BONTEN` | `$1D26` | 314  | data              |
| `BONUNT` | `$1D20` | 310  | data              |
| `COMMES` | `$1D08` | 306  | data              |
| `COMPL1` | `$1C5D` | 159  | instruction-label |
| `COMPL2` | `$1C35` | 122  | instruction-label |
| `COMPL3` | `$1C68` | 168  | instruction-label |
| `COMPL4` | `$1C6A` | 172  | instruction-label |
| `COMPL8` | `$1CAA` | 216  | instruction-label |
| `COMPL9` | `$1CAF` | 221  | instruction-label |
| `COMPLE` | `$1BAC` | 7    | instruction-label |
| `COPL2`  | `$1CB9` | 230  | instruction-label |
| `DINTHS` | `$1C5B` | 155  | instruction-label |
| `DIO`    | `$1BF9` | 70   | instruction-label |
| `DONTHS` | `$1C57` | 150  | instruction-label |
| `FEELIN` | `$1CCE` | 252  | instruction-label |
| `GLP1`   | `$1CD7` | 265  | instruction-label |
| `GLP2`   | `$1CF4` | 288  | instruction-label |
| `GLPBOX` | `$1CD1` | 258  | instruction-label |
| `NTRONF` | `$1BE9` | 50   | instruction-label |

### INIT-SHEET

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/038_INIT-SHEET.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `ALIDEF` | `$1D2C` | 11   | instruction-label |
| `CONVTB` | `$1D60` | 58   | data              |
| `DIF1`   | `$1D54` | 46   | instruction-label |

### SET-SHEET

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/037_SET-SHEET.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `ALRNDP` | `$1E00` | 144  | instruction-label |
| `BENORM` | `$1DD0` | 105  | instruction-label |
| `BJH`    | `$1D72` | 11   | instruction-label |
| `DOCTOR` | `$1E02` | 157  | instruction-label |
| `FLTB`   | `$1DA2` | 68   | instruction-label |
| `GOBAK`  | `$1E12` | 171  | instruction-label |
| `MPGVIL` | `$1DFA` | 140  | data              |
| `SETSHT` | `$1D70` | 7    | instruction-label |
| `TOKILL` | `$1DF4` | 138  | data              |

### ALIEN-CODE

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/001_ALIEN-CODE.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `ALDEAD` | `$1F1F` | 210  | instruction-label |
| `ALDO`   | `$1F3D` | 262  | instruction-label |
| `ALIEND` | `$1F2A` | 220  | instruction-label |
| `ALIENS` | `$1E37` | 6    | instruction-label |
| `ALILOP` | `$1E4C` | 29   | instruction-label |
| `ALLE`   | `$1F47` | 282  | instruction-label |
| `ALRI`   | `$1F33` | 244  | instruction-label |
| `ALSC1`  | `$1FC3` | 406  | data              |
| `ALSC2`  | `$1FCB` | 410  | data              |
| `ALSC3`  | `$1FD3` | 414  | data              |
| `ALUP`   | `$1F2B` | 227  | instruction-label |
| `ALXOK1` | `$1F3A` | 254  | instruction-label |
| `ALXOK2` | `$1F4E` | 290  | instruction-label |
| `ALYOK1` | `$1F30` | 236  | instruction-label |
| `ALYOK2` | `$1F44` | 272  | instruction-label |
| `ARMAT`  | `$1EA4` | 116  | instruction-label |
| `BRAINS` | `$1EF8` | 186  | instruction-label |
| `DRNO`   | `$1E96` | 100  | instruction-label |
| `EXPCHR` | `$1F8F` | 354  | data              |
| `EXPLOK` | `$1F72` | 328  | instruction-label |
| `M10`    | `$1ED2` | 159  | instruction-label |
| `MVEALL` | `$1E46` | 20   | instruction-label |
| `NEWALI` | `$1F97` | 361  | instruction-label |
| `NOALDO` | `$1EBF` | 140  | instruction-label |
| `NOALLE` | `$1EC8` | 148  | instruction-label |
| `NOALRI` | `$1EB6` | 132  | instruction-label |
| `NOALUP` | `$1EAD` | 124  | instruction-label |
| `NOMORE` | `$1F9B` | 370  | instruction-label |
| `NOTEXP` | `$1E69` | 53   | instruction-label |
| `NOTGON` | `$1E5F` | 45   | instruction-label |
| `NTENDA` | `$1E93` | 95   | instruction-label |
| `NTOVB`  | `$1F6D` | 321  | instruction-label |
| `STARMZ` | `$1FA0` | 377  | instruction-label |
| `STTDIR` | `$1F8B` | 350  | data              |
| `UPEXPL` | `$1F51` | 298  | instruction-label |

### RESET-CODE

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/032_RESET-CODE.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `RESET`  | `$1FDB` | 4    | instruction-label |
| `RESMES` | `$2047` | 97   | data              |
| `RESS1`  | `$1FFC` | 39   | instruction-label |
| `RESS1A` | `$1FEF` | 26   | instruction-label |
| `RESS2`  | `$201F` | 60   | instruction-label |
| `RESS4`  | `$202F` | 72   | instruction-label |
| `RESS5`  | `$2034` | 78   | instruction-label |
| `RESS6`  | `$2041` | 88   | instruction-label |

### FIZZLE

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/012_FIZZLE.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `FIZ1`   | `$207E` | 18   | instruction-label |
| `FIZ2`   | `$208B` | 33   | instruction-label |
| `FIZ3`   | `$208D` | 37   | instruction-label |
| `FIZ4`   | `$20AB` | 58   | instruction-label |
| `FIZ5`   | `$20AD` | 62   | instruction-label |
| `FIZZLE` | `$206F` | 6    | instruction-label |

### GAME-OVER

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/016_GAME-OVER.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `ERIC`   | `$20F6` | 42   | instruction-label |
| `GAMOVR` | `$20C6` | 6    | instruction-label |
| `OVR1`   | `$20CC` | 13   | instruction-label |
| `OVR2`   | `$2107` | 56   | instruction-label |
| `OVR3`   | `$211F` | 76   | instruction-label |
| `OVR4`   | `$2125` | 83   | instruction-label |

### DEATH-CODE

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/010_DEATH-CODE.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `ALLOVR` | `$2165` | 41   | instruction-label |
| `DEATH`  | `$212F` | 4    | instruction-label |

### CHAR-ANIM

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/009_CHAR-ANIM.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `LANAN1` | `$2175` | 18   | instruction-label |
| `LANANI` | `$216B` | 6    | instruction-label |

### DATA-LAND/CHARS

[Preserved input](../../Original%20Source%20Recovered/1992/DISK9/DATALAND.TXT). Logical lines use this module; origin: 1992 fallback.

| Symbol  | Address | Line | Kind |
| ------- | ------- | ---- | ---- |
| `CHR87` | `$2188` | 4    | data |
| `CHR91` | `$21A8` | 11   | data |

### SOUND-EFFECTS

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/058_SOUND-EFFECTS.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `ENDN1`  | `$2334` | 386  | instruction-label |
| `ENDN2`  | `$2325` | 366  | instruction-label |
| `GENSIS` | `$21D9` | 39   | instruction-label |
| `GOFX`   | `$21CE` | 25   | instruction-label |
| `NISND`  | `$2246` | 162  | instruction-label |
| `NOISE`  | `$2269` | 201  | instruction-label |
| `NOSND`  | `$223D` | 154  | instruction-label |
| `REFRSH` | `$2238` | 147  | instruction-label |
| `RIGT`   | `$22B0` | 264  | instruction-label |
| `ROPE`   | `$22B4` | 269  | instruction-label |
| `S1`     | `$2261` | 192  | instruction-label |
| `SAMEB4` | `$22A5` | 254  | instruction-label |
| `SF1`    | `$21F4` | 69   | instruction-label |
| `SF2`    | `$2205` | 87   | instruction-label |
| `SF3`    | `$221D` | 107  | instruction-label |
| `SF4`    | `$222E` | 125  | instruction-label |
| `SF5`    | `$2237` | 139  | instruction-label |
| `SFX`    | `$21C8` | 8    | instruction-label |
| `SFX1ON` | `$225B` | 186  | instruction-label |
| `SFX2ON` | `$2288` | 227  | instruction-label |
| `SFX4ON` | `$22D2` | 292  | instruction-label |
| `SFX5ON` | `$22FA` | 321  | instruction-label |
| `SIX4`   | `$2304` | 331  | instruction-label |
| `SNDON`  | `$2247` | 166  | instruction-label |
| `SOU2`   | `$2276` | 213  | instruction-label |
| `SOU3`   | `$2293` | 237  | instruction-label |
| `SOU4`   | `$22C0` | 279  | instruction-label |
| `SOU5`   | `$22E8` | 308  | instruction-label |
| `SOU6`   | `$2315` | 343  | instruction-label |
| `STCH2`  | `$2316` | 350  | instruction-label |

### RASTER-ROUTINES

[Preserved input](../../Original%20Source%20Recovered/1992/DISK9/RASTERRO.TXT). Logical lines use this module; origin: 1992 fallback.

| Symbol  | Address | Line | Kind              |
| ------- | ------- | ---- | ----------------- |
| `R5L`   | `$23EB` | 147  | instruction-label |
| `RAST1` | `$2343` | 7    | instruction-label |
| `RAST2` | `$236A` | 41   | instruction-label |
| `RAST3` | `$23B8` | 99   | instruction-label |
| `RAST4` | `$23E9` | 140  | instruction-label |
| `RAST5` | `$240A` | 170  | instruction-label |
| `RS5D`  | `$240C` | 176  | instruction-label |
| `SHITY` | `$2346` | 15   | instruction-label |
| `SRP`   | `$236C` | 47   | instruction-label |
| `STP1`  | `$23A9` | 82   | instruction-label |
| `STP2`  | `$23E4` | 132  | instruction-label |
| `STP3`  | `$242B` | 196  | instruction-label |
| `STP4`  | `$23DD` | 125  | instruction-label |
| `STP5`  | `$23B0` | 89   | instruction-label |

### HIGH-SCORE

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/017_HIGH-SCORE.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `CONGRA` | `$2477` | 81   | data              |
| `HIGH`   | `$2433` | 7    | instruction-label |
| `HLP1`   | `$2444` | 27   | instruction-label |
| `HLP1A`  | `$2435` | 11   | instruction-label |
| `HLP2`   | `$2456` | 51   | instruction-label |
| `HLP3`   | `$2462` | 62   | instruction-label |
| `ITSIN`  | `$2454` | 45   | instruction-label |

### ALTERABLES

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/002_ALTERABLES.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `ALTER`  | `$249D` | 10   | instruction-label |
| `CTLTOG` | `$2580` | 159  | data              |
| `FRAK1`  | `$2590` | 163  | data              |
| `NOJ`    | `$24AB` | 23   | instruction-label |
| `NOK`    | `$24B9` | 36   | instruction-label |
| `NOQ`    | `$24D5` | 62   | instruction-label |
| `NOS`    | `$24C7` | 49   | instruction-label |
| `SNDTOG` | `$2578` | 155  | data              |
| `TPBUFF` | `$2528` | 143  | data              |
| `TPCOLS` | `$2550` | 147  | data              |
| `TRACE`  | `$24E4` | 79   | instruction-label |
| `TRECE`  | `$2516` | 127  | instruction-label |
| `TRICE`  | `$2503` | 106  | instruction-label |

### LAND-GO

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/022_LAND-GO.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `LANDGO` | `$2592` | 4    | instruction-label |
| `LNDGO`  | `$2596` | 11   | instruction-label |

### STARTER

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/060_STARTER.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `ESC1`   | `$260F` | 94   | instruction-label |
| `ESC2`   | `$2616` | 101  | instruction-label |
| `ESC3`   | `$2628` | 120  | instruction-label |
| `ESC4`   | `$261E` | 110  | instruction-label |
| `FATSE`  | `$25D8` | 52   | instruction-label |
| `KANSAS` | `$25DB` | 56   | instruction-label |
| `PRE1`   | `$25A8` | 12   | instruction-label |
| `PRTESC` | `$2608` | 87   | instruction-label |
| `SHAME`  | `$25BA` | 30   | instruction-label |
| `SPDBOT` | `$264A` | 149  | data              |
| `SPDTOP` | `$2646` | 147  | data              |
| `STARCL` | `$2642` | 145  | data              |
| `STARLP` | `$25B3` | 23   | instruction-label |
| `STARTE` | `$25A4` | 7    | instruction-label |
| `TESCO`  | `$25E4` | 67   | data              |

### FUEL-CHAR/DATA

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/013_FUEL-CHAR~2FDATA.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind |
| -------- | ------- | ---- | ---- |
| `FUELDA` | `$264E` | 4    | data |

### FUEL-CODE

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/014_FUEL-CODE.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `CALCFL` | `$275D` | 203  | instruction-label |
| `CLSFUL` | `$277E` | 237  | instruction-label |
| `FUL1`   | `$2782` | 244  | instruction-label |
| `FUL2`   | `$2730` | 163  | instruction-label |
| `FUL3`   | `$274D` | 186  | instruction-label |
| `FUL4`   | `$26BE` | 62   | instruction-label |
| `FULCOD` | `$267E` | 4    | instruction-label |
| `FULUP`  | `$26E4` | 98   | instruction-label |
| `FUOK`   | `$271E` | 145  | instruction-label |
| `FUOUT`  | `$26F5` | 112  | instruction-label |
| `GETFLY` | `$269F` | 35   | instruction-label |
| `ITOONF` | `$26B7` | 55   | instruction-label |
| `NOFULP` | `$268A` | 17   | instruction-label |
| `STFUEL` | `$268B` | 21   | instruction-label |
| `STIPIT` | `$26FB` | 118  | instruction-label |
| `STPFUL` | `$2700` | 125  | instruction-label |

### PRINT-LIVES

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/030_PRINT-LIVES.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `CLLIV`  | `$279C` | 32   | instruction-label |
| `LIVLP1` | `$278D` | 11   | instruction-label |
| `LIVLP2` | `$27A0` | 37   | instruction-label |
| `NOTALL` | `$2794` | 20   | instruction-label |
| `PRLIVE` | `$2789` | 6    | instruction-label |
| `PRTLIV` | `$27AA` | 51   | instruction-label |

### PAUSE/ESCAPE

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/027_PAUSE~2FESCAPE.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `CHKESC` | `$27C0` | 6    | instruction-label |
| `CHKPAS` | `$27C7` | 16   | instruction-label |
| `FLID1`  | `$2852` | 143  | data              |
| `FLID2`  | `$2854` | 144  | data              |
| `LA`     | `$27CD` | 25   | instruction-label |
| `NOBB1`  | `$2842` | 130  | instruction-label |
| `NOBBLY` | `$2835` | 115  | instruction-label |
| `NYC1`   | `$2801` | 65   | instruction-label |
| `NYC2A`  | `$281D` | 85   | instruction-label |
| `SCANG`  | `$282E` | 107  | instruction-label |
| `SCANP`  | `$2827` | 99   | instruction-label |
| `WIND1`  | `$27E6` | 44   | instruction-label |

### PULSATE

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/031_PULSATE.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `LUMINX` | `$2864` | 22   | data              |
| `PULSAT` | `$2856` | 4    | instruction-label |

### BANNER-DATA

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/004_BANNER-DATA.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind |
| -------- | ------- | ---- | ---- |
| `BANNER` | `$2874` | 4    | data |

### TITLE-WORK

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/064_TITLE-WORK.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `BRIN1`  | `$2A38` | 152  | instruction-label |
| `BRIN2`  | `$2A44` | 167  | instruction-label |
| `BRIN3`  | `$2A2F` | 140  | instruction-label |
| `BRING`  | `$2A28` | 131  | instruction-label |
| `CALCBY` | `$2A02` | 82   | instruction-label |
| `DIREST` | `$29DE` | 45   | instruction-label |
| `FAD1`   | `$2A50` | 186  | instruction-label |
| `FAD2`   | `$2A5A` | 195  | instruction-label |
| `FAD3`   | `$2A65` | 204  | instruction-label |
| `FAD4`   | `$2A6B` | 211  | instruction-label |
| `FAD5`   | `$2A72` | 218  | instruction-label |
| `FADOFF` | `$2A4C` | 179  | instruction-label |
| `JOURNY` | `$29FD` | 72   | instruction-label |
| `KIDS`   | `$2A1C` | 113  | instruction-label |
| `SAME1`  | `$29F1` | 61   | instruction-label |
| `SAME2`  | `$2A0B` | 91   | instruction-label |
| `SAME3`  | `$2A42` | 163  | instruction-label |
| `SCRLIT` | `$29B4` | 4    | instruction-label |
| `ZZTOP`  | `$2A27` | 125  | instruction-label |

### TITLE-LOOP

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/061_TITLE-LOOP.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `READY`  | `$2AE0` | 74   | instruction-label |
| `TITLOP` | `$2A88` | 4    | instruction-label |
| `TITLP`  | `$2AA2` | 26   | instruction-label |
| `TITTER` | `$2ACA` | 53   | instruction-label |
| `TUTTER` | `$2AD1` | 60   | instruction-label |

### TITLE-GENERATE

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/062_TITLE-GENERATE.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `REVER`  | `$2AF0` | 13   | instruction-label |
| `REVLP`  | `$2AF5` | 20   | instruction-label |
| `REVTIT` | `$2AEA` | 6    | instruction-label |

### TV-PICTURE

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/066_TV-PICTURE.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `HITTBL` | `$2B77` | 101  | data              |
| `SCLPCL` | `$2B65` | 80   | instruction-label |
| `SCRTVP` | `$2B51` | 57   | instruction-label |
| `TV1`    | `$2B55` | 65   | instruction-label |
| `TV2`    | `$2B67` | 86   | instruction-label |
| `TV3`    | `$2B3C` | 35   | instruction-label |
| `TVPIC`  | `$2B16` | 6    | instruction-label |

### IRQ

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/019_IRQ.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `BRAN`   | `$2BCF` | 82   | instruction-label |
| `IRQEND` | `$2BE0` | 98   | instruction-label |
| `NOLAST` | `$2BC5` | 64   | instruction-label |
| `SERV`   | `$2BB1` | 41   | instruction-label |
| `SETIRQ` | `$2B8B` | 10   | instruction-label |

### JOYSTIK

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/020_JOYSTIK.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `NAYE`   | `$2C16` | 47   | instruction-label |
| `OKYAK`  | `$2BEE` | 17   | instruction-label |
| `READDK` | `$2BF6` | 24   | instruction-label |
| `REDJOS` | `$2BE9` | 10   | instruction-label |
| `XTRCDE` | `$2C23` | 63   | instruction-label |

### KEY-SCAN

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/021_KEY-SCAN.seq). Logical lines use this module; origin: 2026 disk.

| Symbol  | Address | Line | Kind              |
| ------- | ------- | ---- | ----------------- |
| `BTD`   | `$2C4F` | 58   | data              |
| `KEY`   | `$2C27` | 12   | instruction-label |
| `KEYIT` | `$2C3C` | 37   | instruction-label |
| `RTTY`  | `$2C4D` | 51   | instruction-label |
| `RWD`   | `$2C52` | 63   | data              |
| `SCAN1` | `$2C2D` | 19   | instruction-label |

### UTILS

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/067_UTILS.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `CLLOP`  | `$2C89` | 68   | instruction-label |
| `CLVARS` | `$2C85` | 63   | instruction-label |
| `DELAY`  | `$2C77` | 41   | instruction-label |
| `DELLOP` | `$2C7B` | 47   | instruction-label |
| `LOOKUP` | `$2CEF` | 149  | data              |
| `NUM1T7` | `$2CDF` | 132  | instruction-label |
| `RANDOM` | `$2C55` | 10   | instruction-label |
| `RANLOP` | `$2C6C` | 28   | instruction-label |
| `RUSRAS` | `$2CD0` | 116  | instruction-label |
| `RUSSER` | `$2CD7` | 122  | instruction-label |
| `SCRPOS` | `$2CB0` | 106  | data              |
| `XY`     | `$2C8F` | 79   | instruction-label |

### PLAY-GAME

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/029_PLAY-GAME.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `FLEETW` | `$2D6E` | 92   | instruction-label |
| `LOOP`   | `$2D63` | 83   | instruction-label |
| `REPLAY` | `$2D33` | 50   | instruction-label |
| `START`  | `$2CFF` | 6    | instruction-label |
| `STLOOP` | `$2D3B` | 57   | instruction-label |

### WHOOPPEE-MESSAGE

[Preserved input](../../Original%20Source%20Recovered/1992/DISK9/WHOOPPEE.TXT). Logical lines use this module; origin: 1992 fallback.

| Symbol  | Address | Line | Kind |
| ------- | ------- | ---- | ---- |
| `MESST` | `$2D78` | 5    | data |

### MESSAGE-STUFF

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/025_MESSAGE-STUFF.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `MESHIL` | `$2ED0` | 22   | instruction-label |
| `MESSVE` | `$2EC0` | 4    | instruction-label |
| `MSL1`   | `$2ED2` | 26   | instruction-label |
| `MSL2`   | `$2EE3` | 42   | instruction-label |
| `NTMSED` | `$2EF5` | 60   | instruction-label |
| `RUPERT` | `$2EE3` | 44   | instruction-label |

### STAR-CODE

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/059_STAR-CODE.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `DNTPRT` | `$2FC1` | 199  | instruction-label |
| `FUKOFF` | `$2F68` | 124  | instruction-label |
| `GOSTAR` | `$2F2D` | 73   | instruction-label |
| `INSTAR` | `$2EFB` | 22   | instruction-label |
| `MVEEND` | `$2FCC` | 208  | instruction-label |
| `MVESTR` | `$2F31` | 78   | instruction-label |
| `PANA`   | `$2F09` | 36   | instruction-label |
| `PRTIT`  | `$2FAD` | 183  | instruction-label |
| `ST1`    | `$2EFF` | 27   | instruction-label |
| `STARS`  | `$2F28` | 66   | instruction-label |
| `STARXY` | `$2FCD` | 214  | instruction-label |
| `STATNW` | `$2F8D` | 154  | instruction-label |
| `STCOLS` | `$2FDC` | 230  | data              |

### TOPLAND-PIXEL

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/065_TOPLAND-PIXEL.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `BLINK1` | `$3028` | 76   | instruction-label |
| `BTL1`   | `$3010` | 57   | instruction-label |
| `HARTOP` | `$300E` | 53   | instruction-label |
| `TOP1`   | `$2FF9` | 29   | instruction-label |
| `TOP2`   | `$2FFE` | 35   | instruction-label |
| `TOP4`   | `$2FEA` | 15   | instruction-label |
| `TOPMVE` | `$2FE0` | 4    | instruction-label |
| `TOPNEW` | `$3035` | 89   | instruction-label |

### BOTLAND-PIXEL

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/006_BOTLAND-PIXEL.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `BLINK2` | `$30A2` | 83   | instruction-label |
| `BLINK3` | `$30A4` | 87   | instruction-label |
| `BLINK4` | `$30B6` | 107  | instruction-label |
| `BOT1`   | `$3067` | 30   | instruction-label |
| `BOT2`   | `$306C` | 36   | instruction-label |
| `BOT4`   | `$3058` | 16   | instruction-label |
| `BOTMVE` | `$304E` | 5    | instruction-label |
| `BOTNEW` | `$30B2` | 100  | instruction-label |
| `BOTST`  | `$30CE` | 131  | data              |
| `BTL2`   | `$307E` | 58   | instruction-label |
| `HARBOT` | `$307C` | 54   | instruction-label |
| `YHIL`   | `$30D4` | 133  | data              |

### MOVE-SHIP

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/026_MOVE-SHIP.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `DOWOK`  | `$315E` | 136  | instruction-label |
| `FIROUT` | `$30FA` | 37   | instruction-label |
| `NFIRE`  | `$3104` | 49   | instruction-label |
| `NODOWN` | `$3183` | 168  | instruction-label |
| `NOUP`   | `$314A` | 117  | instruction-label |
| `SHIP`   | `$30D8` | 4    | instruction-label |
| `SHIPMT` | `$30DF` | 13   | instruction-label |
| `SHP1`   | `$3109` | 55   | instruction-label |
| `UPOK`   | `$3125` | 85   | instruction-label |

### SHIP-CALCS

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/055_SHIP-CALCS.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `CHKSHP` | `$31C1` | 66   | instruction-label |
| `CLRSHP` | `$31F4` | 124  | instruction-label |
| `PRS1`   | `$31F8` | 129  | instruction-label |
| `PRS2`   | `$318E` | 14   | instruction-label |
| `PRS3`   | `$31B1` | 41   | instruction-label |
| `PRSHIP` | `$3187` | 7    | instruction-label |
| `SHIPON` | `$31AC` | 35   | instruction-label |
| `SHOP1`  | `$31CB` | 76   | instruction-label |
| `SHOP2`  | `$31D1` | 83   | instruction-label |
| `SHOP3`  | `$31EE` | 112  | instruction-label |
| `SHOP4`  | `$31D3` | 87   | instruction-label |
| `SHOP5`  | `$31EA` | 107  | instruction-label |
| `SHOP6`  | `$31F3` | 118  | instruction-label |

### TABLES

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/018_TABLES.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind |
| -------- | ------- | ---- | ---- |
| `FUELCH` | `$3243` | 32   | data |
| `FUELYP` | `$3249` | 36   | data |
| `SHPCHR` | `$320B` | 12   | data |
| `TIM20`  | `$321F` | 22   | data |
| `TIM24`  | `$3241` | 28   | data |
| `TIM32`  | `$3258` | 48   | data |
| `TIM5`   | `$3253` | 44   | data |
| `TIM6`   | `$325C` | 52   | data |
| `TIM9`   | `$324F` | 40   | data |
| `YSHIP`  | `$31FF` | 6    | data |
| `YVAL1`  | `$3217` | 18   | data |

### FIRING-MEGA/CODE

[Preserved input](../../Original%20Source%20Recovered/1992/DISK9/FIRINGME.TXT). Logical lines use this module; origin: 1992 fallback.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `CLRLAZ` | `$32E1` | 132  | instruction-label |
| `DGODWN` | `$329E` | 54   | instruction-label |
| `FIRE`   | `$326A` | 7    | instruction-label |
| `FLOYD`  | `$3266` | 5    | data              |
| `GFIT`   | `$32A8` | 72   | instruction-label |
| `LAZATL` | `$32C0` | 97   | instruction-label |
| `LAZCLR` | `$32DD` | 127  | instruction-label |
| `MVELAZ` | `$32A3` | 63   | instruction-label |
| `NEWLAZ` | `$326F` | 18   | instruction-label |
| `NOWDED` | `$32BF` | 93   | instruction-label |
| `PINK`   | `$3262` | 4    | data              |
| `SHINE`  | `$326E` | 14   | instruction-label |

### SCREEN-SETUP

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/035_SCREEN-SETUP.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `BTCL1`  | `$3341` | 93   | instruction-label |
| `CLSTOP` | `$33D5` | 244  | instruction-label |
| `FLSTOP` | `$33C4` | 222  | instruction-label |
| `LANCOL` | `$3335` | 73   | instruction-label |
| `PRSSTR` | `$3384` | 164  | data              |
| `RACIAL` | `$335A` | 121  | instruction-label |
| `SCREEN` | `$32E8` | 6    | instruction-label |
| `SCRIL`  | `$33D7` | 248  | instruction-label |
| `SCRL1`  | `$32F3` | 17   | instruction-label |
| `SCRL1A` | `$3325` | 52   | instruction-label |
| `SCRL3`  | `$339E` | 181  | instruction-label |
| `SCRL3A` | `$33BD` | 209  | instruction-label |
| `SCRL4`  | `$33B2` | 197  | instruction-label |
| `SCRL5`  | `$33CE` | 233  | instruction-label |
| `TITCLS` | `$334A` | 105  | instruction-label |
| `TITER2` | `$334E` | 112  | instruction-label |
| `TITR1A` | `$3367` | 135  | instruction-label |
| `TITR1B` | `$3378` | 151  | instruction-label |
| `TITTOP` | `$3397` | 171  | instruction-label |
| `TPCL1`  | `$3339` | 82   | instruction-label |

### FUEL-GAUGE

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/015_FUEL-GAUGE.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `ADDE1`  | `$349A` | 187  | instruction-label |
| `ADFUEL` | `$3491` | 175  | instruction-label |
| `ADOKY`  | `$34AC` | 203  | instruction-label |
| `BYESND` | `$347D` | 153  | instruction-label |
| `DAY`    | `$3490` | 169  | instruction-label |
| `DOITYA` | `$3459` | 119  | instruction-label |
| `ENDBIT` | `$34CD` | 226  | data              |
| `FUELDO` | `$3450` | 107  | instruction-label |
| `HIWIRE` | `$3419` | 50   | instruction-label |
| `HMMM`   | `$346E` | 139  | instruction-label |
| `MOON`   | `$3458` | 115  | instruction-label |
| `MORG1`  | `$3439` | 78   | instruction-label |
| `MORG2`  | `$3447` | 94   | instruction-label |
| `MORGAN` | `$341D` | 56   | instruction-label |
| `NIGHT`  | `$3489` | 162  | instruction-label |
| `PREN2`  | `$33EF` | 14   | instruction-label |
| `PRTFUL` | `$33ED` | 10   | instruction-label |
| `ROSS1`  | `$34B1` | 215  | data              |
| `ROSS2`  | `$34BF` | 221  | data              |
| `SHOTFL` | `$3465` | 130  | instruction-label |
| `UPFUEL` | `$3409` | 35   | instruction-label |
| `WANNA`  | `$3499` | 183  | instruction-label |

### SHTABLE

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/057_SHTABLE.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind |
| -------- | ------- | ---- | ---- |
| `SHTABL` | `$34D5` | 7    | data |

### ALI-PRINT&CLEAR

[Preserved input](../../Original%20Source%20Recovered/1992/DISK9/ALIPRINT.TXT). Logical lines use this module; origin: 1992 fallback.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `ALICLR` | `$3560` | 13   | instruction-label |
| `ALIPRT` | `$3576` | 36   | instruction-label |
| `NTHIT`  | `$3583` | 47   | instruction-label |
| `PRTALI` | `$3569` | 25   | instruction-label |
| `RUBALI` | `$3555` | 4    | instruction-label |

### SHIP-DEF

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/056_SHIP-DEF.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind |
| -------- | ------- | ---- | ---- |
| `SHPDT1` | `$3591` | 4    | data |

### SCORE-ROUTINES

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/034_SCORE-ROUTINES.seq). Logical lines use this module; origin: 2026 disk.

| Symbol   | Address | Line | Kind              |
| -------- | ------- | ---- | ----------------- |
| `ADDLOP` | `$35D5` | 12   | instruction-label |
| `BONLIF` | `$35FB` | 47   | instruction-label |
| `MADONA` | `$35D7` | 16   | instruction-label |
| `NOBONS` | `$3664` | 143  | instruction-label |
| `NOLIFE` | `$360D` | 62   | instruction-label |
| `PUSLIF` | `$35F9` | 43   | instruction-label |
| `SCORCL` | `$3665` | 149  | data              |
| `SCORE`  | `$35D1` | 4    | instruction-label |
| `SCOREL` | `$35EA` | 31   | instruction-label |
| `SCORPT` | `$3616` | 78   | instruction-label |
| `SCRPRT` | `$3629` | 96   | instruction-label |
| `STPBON` | `$3660` | 138  | instruction-label |
| `XTR1`   | `$360E` | 66   | instruction-label |

### SHEET1

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/039_SHEET1.seq). Logical lines use this module; origin: 2026 disk.

| Symbol  | Address | Line | Kind   |
| ------- | ------- | ---- | ------ |
| `B1B`   | `$0031` | 19   | equate |
| `L1A`   | `$003C` | 13   | equate |
| `L1B`   | `$0070` | 14   | equate |
| `L1C`   | `$0056` | 15   | equate |
| `PATD1` | `$3669` | 6    | data   |

### SHEET2

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/040_SHEET2.seq). Logical lines use this module; origin: 2026 disk.

| Symbol  | Address | Line | Kind   |
| ------- | ------- | ---- | ------ |
| `B2B`   | `$0031` | 19   | equate |
| `L2A`   | `$006F` | 13   | equate |
| `L2B`   | `$0000` | 14   | equate |
| `L2C`   | `$00B5` | 15   | equate |
| `PATD2` | `$3675` | 6    | data   |

### SHEET3

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/041_SHEET3.seq). Logical lines use this module; origin: 2026 disk.

| Symbol  | Address | Line | Kind   |
| ------- | ------- | ---- | ------ |
| `B3B`   | `$0031` | 21   | equate |
| `L3A`   | `$006A` | 15   | equate |
| `L3B`   | `$00A0` | 16   | equate |
| `L3C`   | `$00B2` | 17   | equate |
| `PATD3` | `$3681` | 6    | data   |

### SHEET4

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/042_SHEET4.seq). Logical lines use this module; origin: 2026 disk.

| Symbol  | Address | Line | Kind   |
| ------- | ------- | ---- | ------ |
| `B4B`   | `$0031` | 20   | equate |
| `L4A`   | `$0049` | 14   | equate |
| `L4B`   | `$00E1` | 15   | equate |
| `L4C`   | `$00D0` | 16   | equate |
| `PATD4` | `$3697` | 6    | data   |

### SHEET5

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/044_SHEET5.seq). Logical lines use this module; origin: 2026 disk.

| Symbol  | Address | Line | Kind   |
| ------- | ------- | ---- | ------ |
| `B5B`   | `$0031` | 22   | equate |
| `L5A`   | `$0029` | 16   | equate |
| `L5B`   | `$00F0` | 17   | equate |
| `L5C`   | `$00C8` | 18   | equate |
| `PATD5` | `$36A8` | 6    | data   |

### SHEET6

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/043_SHEET6.seq). Logical lines use this module; origin: 2026 disk.

| Symbol  | Address | Line | Kind   |
| ------- | ------- | ---- | ------ |
| `B6B`   | `$0031` | 20   | equate |
| `L6A`   | `$004C` | 14   | equate |
| `L6B`   | `$00F1` | 15   | equate |
| `L6C`   | `$00BB` | 16   | equate |
| `PATD6` | `$36C9` | 6    | data   |

### SHEET7

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/045_SHEET7.seq). Logical lines use this module; origin: 2026 disk.

| Symbol  | Address | Line | Kind   |
| ------- | ------- | ---- | ------ |
| `B7B`   | `$0031` | 21   | equate |
| `L7A`   | `$005F` | 15   | equate |
| `L7B`   | `$00F0` | 16   | equate |
| `L7C`   | `$009C` | 17   | equate |
| `PATD7` | `$36DF` | 6    | data   |

### SHEET8

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/046_SHEET8.seq). Logical lines use this module; origin: 2026 disk.

| Symbol  | Address | Line | Kind   |
| ------- | ------- | ---- | ------ |
| `B8B`   | `$0031` | 20   | equate |
| `L8A`   | `$0019` | 14   | equate |
| `L8B`   | `$0071` | 15   | equate |
| `L8C`   | `$00C7` | 16   | equate |
| `PATD8` | `$36F4` | 6    | data   |

### SHEET9

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/047_SHEET9.seq). Logical lines use this module; origin: 2026 disk.

| Symbol  | Address | Line | Kind   |
| ------- | ------- | ---- | ------ |
| `B9B`   | `$0000` | 20   | equate |
| `L9A`   | `$0029` | 14   | equate |
| `L9B`   | `$00F1` | 15   | equate |
| `L9C`   | `$00C1` | 16   | equate |
| `PATD9` | `$3706` | 6    | data   |

### SHEETA

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/048_SHEETA.seq). Logical lines use this module; origin: 2026 disk.

| Symbol  | Address | Line | Kind   |
| ------- | ------- | ---- | ------ |
| `BAB`   | `$0000` | 20   | equate |
| `LAA`   | `$004D` | 14   | equate |
| `LAB`   | `$00F1` | 15   | equate |
| `LAC`   | `$00C7` | 16   | equate |
| `PATDA` | `$3717` | 6    | data   |

### SHEETB

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/049_SHEETB.seq). Logical lines use this module; origin: 2026 disk.

| Symbol  | Address | Line | Kind   |
| ------- | ------- | ---- | ------ |
| `BBB`   | `$0000` | 20   | equate |
| `LBA`   | `$004A` | 14   | equate |
| `LBB`   | `$00E1` | 15   | equate |
| `LBC`   | `$00B8` | 16   | equate |
| `PATDB` | `$372D` | 6    | data   |

### SHEETC

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/050_SHEETC.seq). Logical lines use this module; origin: 2026 disk.

| Symbol  | Address | Line | Kind   |
| ------- | ------- | ---- | ------ |
| `BCB`   | `$0000` | 20   | equate |
| `LCA`   | `$003F` | 14   | equate |
| `LCB`   | `$00E1` | 15   | equate |
| `LCC`   | `$00C8` | 16   | equate |
| `PATDC` | `$373F` | 6    | data   |

### SHEETD

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/051_SHEETD.seq). Logical lines use this module; origin: 2026 disk.

| Symbol  | Address | Line | Kind   |
| ------- | ------- | ---- | ------ |
| `BDB`   | `$0000` | 20   | equate |
| `LDB`   | `$00F1` | 15   | equate |
| `LDC`   | `$00B2` | 16   | equate |
| `LZA`   | `$0039` | 14   | equate |
| `PATDD` | `$3752` | 6    | data   |

### SHEETE

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/052_SHEETE.seq). Logical lines use this module; origin: 2026 disk.

| Symbol  | Address | Line | Kind   |
| ------- | ------- | ---- | ------ |
| `BEB`   | `$0000` | 20   | equate |
| `LEA`   | `$005F` | 14   | equate |
| `LEB`   | `$00F1` | 15   | equate |
| `LEC`   | `$00C8` | 16   | equate |
| `PATDE` | `$3764` | 6    | data   |

### SHEETF

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/053_SHEETF.seq). Logical lines use this module; origin: 2026 disk.

| Symbol  | Address | Line | Kind   |
| ------- | ------- | ---- | ------ |
| `BFB`   | `$0000` | 20   | equate |
| `LFA`   | `$003A` | 14   | equate |
| `LFB`   | `$00F1` | 15   | equate |
| `LFC`   | `$00CB` | 16   | equate |
| `PATDF` | `$377D` | 6    | data   |

### SHEETG

[Preserved input](../../Original%20Source%20Recovered/2026/Xargons-Revenge-C16-Side2/054_SHEETG.seq). Logical lines use this module; origin: 2026 disk.

| Symbol  | Address | Line | Kind   |
| ------- | ------- | ---- | ------ |
| `BGB`   | `$0000` | 19   | equate |
| `LGA`   | `$003C` | 13   | equate |
| `LGB`   | `$00F1` | 14   | equate |
| `LGC`   | `$00C7` | 15   | equate |
| `PATDG` | `$3792` | 6    | data   |

---

## Direct Transfers

The complete machine-readable transfer list is in [codebase-index.json](codebase-index.json). Resolved targets include constant offsets such as `SCORE+2`; they do not imply normal subroutine calling conventions. [Analysis](../../CODEBASE_ANALYSIS.md), [reference guide](README.md).
