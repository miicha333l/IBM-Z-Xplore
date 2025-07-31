       IDENTIFICATION DIVISION.
       PROGRAM-ID. ADDAMT.
      *******************************************************
      *    This program accepts input and displays output    *
      *******************************************************
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  KEYED-INPUT.
           05  CUST-NO-IN                  PIC X(15).
           05  AMT1-IN                     PIC 9(5).
           05  AMT2-IN                     PIC 9(5).
           05  AMT3-IN                     PIC 9(5).
       01  DISPLAYED-OUTPUT.
           05  CUST-NO-OUT                 PIC X(15).
           05  TOTAL-OUT                   PIC 9(6).
       PROCEDURE DIVISION.
           MOVE CUST-NO-IN TO CUST-NO-OUT
           COMPUTE TOTAL-OUT = AMT1-IN + AMT2-IN + AMT3-IN
           DISPLAY "Client : " CUST-NO-OUT
           DISPLAY "Total   : " TOTAL-OUT
           STOP RUN.
