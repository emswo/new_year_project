EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Amplifier_Audio:LM386 U?
U 1 1 60C9ECB1
P 3300 3050
F 0 "U?" H 3644 3096 50  0000 L CNN
F 1 "LM386" H 3644 3005 50  0000 L CNN
F 2 "" H 3400 3150 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm386.pdf" H 3500 3250 50  0001 C CNN
	1    3300 3050
	1    0    0    -1  
$EndComp
$Comp
L Transistor_BJT:2SC1815 Q?
U 1 1 60CA0AA1
P 4650 3350
F 0 "Q?" H 4840 3396 50  0000 L CNN
F 1 "2SC1815" H 4840 3305 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 4850 3275 50  0001 L CIN
F 3 "https://media.digikey.com/pdf/Data%20Sheets/Toshiba%20PDFs/2SC1815.pdf" H 4650 3350 50  0001 L CNN
	1    4650 3350
	1    0    0    -1  
$EndComp
$Comp
L Transistor_BJT:2SC1815 Q?
U 1 1 60CA2C66
P 4250 3050
F 0 "Q?" H 4440 3096 50  0000 L CNN
F 1 "2SC1815" H 4440 3005 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 4450 2975 50  0001 L CIN
F 3 "https://media.digikey.com/pdf/Data%20Sheets/Toshiba%20PDFs/2SC1815.pdf" H 4250 3050 50  0001 L CNN
	1    4250 3050
	1    0    0    -1  
$EndComp
Wire Wire Line
	3600 3050 4050 3050
Wire Wire Line
	4350 3250 4350 3350
Wire Wire Line
	4350 3350 4450 3350
$EndSCHEMATC
