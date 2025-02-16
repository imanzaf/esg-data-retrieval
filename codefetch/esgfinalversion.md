Project Structure:
├── LICENSE
├── README.md
├── codefetch
│   └── codebase.md
├── data
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── company_names_tickers.csv
│   ├── company_names_tickers_news.csv
│   ├── diagram.md
│   ├── emissimap3.csv
│   ├── main.py
└── tests
    ├── __init__.py


.pre-commit-config.yaml
```
1 | repos:
2 |   - repo: local
3 |     hooks:
4 |       - id: black
5 |         name: black
6 |         entry: black
7 |         language: system
8 |         types: [python]
9 |       - id: flake8
10 |         name: flake8
11 |         entry: flake8
12 |         args: ["--ignore=E501,W503"]
13 |         language: system
14 |         types: [python]
15 |       - id: isort
16 |         name: isort
17 |         entry: isort
18 |         language: system
19 |         args: ["--profile", "black"]
20 |         types: [python]
```

requirements.txt
```
1 | # project requirements
2 | pandas
3 | numpy==1.26.4
4 | python-dotenv
5 | loguru
6 | pydantic
7 | requests
8 | flask
9 | docling
10 | PyPDF2
11 | openai
12 | docling
13 | google-search-results  # serpapi
14 | yfinance
15 | llama_parse
16 | tabula-py
17 | 
18 | # dev requirements
19 | pre-commit
20 | black
21 | flake8
22 | isort
23 | pytest
24 | 
25 | Flask-SocketIO
26 | folium
27 | 
28 | # The main LangChain library
29 | langchain
30 | langchain_community
31 | langchain_core
32 | pymupdf4llm
33 | langchain_openai
```

.github/pull_request_template.md
```
1 | ### Title
2 | ---
3 | 
4 | 
5 | ### Key Changes
6 | ---
```

tests/__init__.py
```
```

src/__init__.py
```
```

src/company_names_tickers.csv
```
1 | ﻿Symbol,Company Name,Industry,Country,Sector,ISIN Number
2 | AAPL,Apple Inc.,Consumer Electronics,United States,Technology,US0378331005
3 | MSFT,Microsoft Corporation,Software - Infrastructure,United States,Technology,US5949181045
4 | NVDA,NVIDIA Corporation,Semiconductors,United States,Technology,US67066G1040
5 | AMZN,"Amazon.com, Inc.",Internet Retail,United States,Consumer Discretionary,US0231351067
6 | GOOG,Alphabet Inc.,Internet Content & Information,United States,Communication Services,US02079K1079
7 | GOOGL,Alphabet Inc.,Internet Content & Information,United States,Communication Services,US02079K3059
8 | META,"Meta Platforms, Inc.",Internet Content & Information,United States,Communication Services,US30303M1027
9 | TSLA,"Tesla, Inc.",Auto Manufacturers,United States,Consumer Discretionary,US88160R1014
10 | BRK.A,Berkshire Hathaway Inc.,Insurance - Diversified,United States,Financials,US0846701086
11 | BRK.B,Berkshire Hathaway Inc.,Insurance - Diversified,United States,Financials,US0846707026
12 | AVGO,Broadcom Inc.,Semiconductors,United States,Technology,US11135F1012
13 | TSM,Taiwan Semiconductor Manufacturing Company Limited,Semiconductors,Taiwan,Technology,US8740391003
14 | WMT,Walmart Inc.,Discount Stores,United States,Consumer Staples,US9311421039
15 | JPM,JPMorgan Chase & Co.,Banks - Diversified,United States,Financials,US46625H1005
16 | LLY,Eli Lilly and Company,Drug Manufacturers - General,United States,Healthcare,US5324571083
17 | V,Visa Inc.,Credit Services,United States,Financials,US92826C8394
18 | MA,Mastercard Incorporated,Credit Services,United States,Financials,US57636Q1040
19 | UNH,UnitedHealth Group Incorporated,Healthcare Plans,United States,Healthcare,US91324P1021
20 | XOM,Exxon Mobil Corporation,Oil & Gas Integrated,United States,Energy,US30231G1022
21 | ORCL,Oracle Corporation,Software - Infrastructure,United States,Technology,US68389X1054
22 | COST,Costco Wholesale Corporation,Discount Stores,United States,Consumer Staples,US22160K1051
23 | HD,"The Home Depot, Inc.",Home Improvement Retail,United States,Consumer Discretionary,US4370761029
24 | NFLX,"Netflix, Inc.",Entertainment,United States,Communication Services,US64110L1061
25 | PG,The Procter & Gamble Company,Household & Personal Products,United States,Consumer Staples,US7427181091
26 | NVO,Novo Nordisk A/S,Drug Manufacturers - General,Denmark,Healthcare,US6701002056
27 | JNJ,Johnson & Johnson,Drug Manufacturers - General,United States,Healthcare,US4781601046
28 | BAC,Bank of America Corporation,Banks - Diversified,United States,Financials,US0605051046
29 | CRM,"Salesforce, Inc.",Software - Application,United States,Technology,US79466L3024
30 | SAP,SAP SE,Software - Application,Germany,Technology,US8030542042
31 | ABBV,AbbVie Inc.,Drug Manufacturers - General,United States,Healthcare,US00287Y1091
32 | CVX,Chevron Corporation,Oil & Gas Integrated,United States,Energy,US1667641005
33 | KO,The Coca-Cola Company,Beverages - Non-Alcoholic,United States,Consumer Staples,US1912161007
34 | ASML,ASML Holding N.V.,Semiconductor Equipment & Materials,Netherlands,Technology,USN070592100
35 | TMUS,"T-Mobile US, Inc.",Telecom Services,United States,Communication Services,US8725901040
36 | WFC,Wells Fargo & Company,Banks - Diversified,United States,Financials,US9497461015
37 | TM,Toyota Motor Corporation,Auto Manufacturers,Japan,Consumer Discretionary,US8923313071
38 | MRK,"Merck & Co., Inc.",Drug Manufacturers - General,United States,Healthcare,US58933Y1055
39 | NOW,"ServiceNow, Inc.",Software - Application,United States,Technology,US81762P1021
40 | CSCO,"Cisco Systems, Inc.",Communication Equipment,United States,Technology,US17275R1023
41 | ACN,Accenture plc,Information Technology Services,Ireland,Technology,IE00B4BNMY34
42 | BX,Blackstone Inc.,Asset Management,United States,Financials,US09260D1072
43 | TMO,Thermo Fisher Scientific Inc.,Diagnostics & Research,United States,Healthcare,US8835561023
44 | MS,Morgan Stanley,Capital Markets,United States,Financials,US6174464486
45 | AXP,American Express Company,Credit Services,United States,Financials,US0258161092
46 | ABT,Abbott Laboratories,Medical Devices,United States,Healthcare,US0028241000
47 | BABA,Alibaba Group Holding Limited,Internet Retail,China,Consumer Discretionary,US01609W1027
48 | GS,"The Goldman Sachs Group, Inc.",Capital Markets,United States,Financials,US38141G1040
49 | AZN,AstraZeneca PLC,Drug Manufacturers - General,United Kingdom,Healthcare,US0463531089
50 | GE,General Electric Company,Aerospace & Defense,United States,Industrials,US3696043013
51 | IBM,International Business Machines Corporation,Information Technology Services,United States,Technology,US4592001014
52 | MCD,McDonald's Corporation,Restaurants,United States,Consumer Discretionary,US5801351017
53 | PEP,"PepsiCo, Inc.",Beverages - Non-Alcoholic,United States,Consumer Staples,US7134481081
54 | LIN,Linde plc,Specialty Chemicals,United Kingdom,Materials,IE000S9YS762
55 | ISRG,"Intuitive Surgical, Inc.",Medical Instruments & Supplies,United States,Healthcare,US46120E6023
56 | NVS,Novartis AG,Drug Manufacturers - General,Switzerland,Healthcare,US66987V1098
57 | DIS,The Walt Disney Company,Entertainment,United States,Communication Services,US2546871060
58 | PM,Philip Morris International Inc.,Tobacco,United States,Consumer Staples,US7181721090
59 | SHEL,Shell plc,Oil & Gas Integrated,United Kingdom,Energy,US7802593050
60 | ADBE,Adobe Inc.,Software - Infrastructure,United States,Technology,US00724F1012
61 | QCOM,QUALCOMM Incorporated,Semiconductors,United States,Technology,US7475251036
62 | CAT,Caterpillar Inc.,Farm & Heavy Construction Machinery,United States,Industrials,US1491231015
63 | AMD,"Advanced Micro Devices, Inc.",Semiconductors,United States,Technology,US0079031078
64 | PLTR,Palantir Technologies Inc.,Software - Infrastructure,United States,Technology,US69608A1088
65 | HSBC,HSBC Holdings plc,Banks - Diversified,United Kingdom,Financials,US4042804066
66 | DHR,Danaher Corporation,Diagnostics & Research,United States,Healthcare,US2358511028
67 | T,AT&T Inc.,Telecom Services,United States,Communication Services,US00206R1023
68 | RY,Royal Bank of Canada,Banks - Diversified,Canada,Financials,CA7800871021
69 | RTX,RTX Corporation,Aerospace & Defense,United States,Industrials,US75513E1010
70 | VZ,Verizon Communications Inc.,Telecom Services,United States,Communication Services,US92343V1044
71 | INTU,Intuit Inc.,Software - Application,United States,Technology,US4612021034
72 | TXN,Texas Instruments Incorporated,Semiconductors,United States,Technology,US8825081040
73 | BLK,"BlackRock, Inc.",Asset Management,United States,Financials,US09247X1019
74 | SPGI,S&P Global Inc.,Financial Data & Stock Exchanges,United States,Financials,US78409V1044
75 | ARM,Arm Holdings plc,Semiconductors,United Kingdom,Technology,US0420682058
76 | PDD,PDD Holdings Inc.,Internet Retail,Ireland,Consumer Discretionary,US7223041028
77 | BKNG,Booking Holdings Inc.,Travel Services,United States,Consumer Discretionary,US09857L1089
78 | SHOP,Shopify Inc.,Software - Application,Canada,Technology,CA82509L1076
79 | PFE,Pfizer Inc.,Drug Manufacturers - General,United States,Healthcare,US7170811035
80 | UNP,Union Pacific Corporation,Railroads,United States,Industrials,US9078181081
81 | BSX,Boston Scientific Corporation,Medical Devices,United States,Healthcare,US1011371077
82 | AMGN,Amgen Inc.,Drug Manufacturers - General,United States,Healthcare,US0311621009
83 | SYK,Stryker Corporation,Medical Devices,United States,Healthcare,US8636671013
84 | C,Citigroup Inc.,Banks - Diversified,United States,Financials,US1729674242
85 | UL,Unilever PLC,Household & Personal Products,United Kingdom,Consumer Staples,US9047677045
86 | SCHW,The Charles Schwab Corporation,Capital Markets,United States,Financials,US8085131055
87 | LOW,"Lowe's Companies, Inc.",Home Improvement Retail,United States,Consumer Discretionary,US5486611073
88 | KKR,KKR & Co. Inc.,Asset Management,United States,Financials,US48251W1045
89 | HDB,HDFC Bank Limited,Banks - Regional,India,Financials,US40415F1012
90 | MUFG,"Mitsubishi UFJ Financial Group, Inc.",Banks - Diversified,Japan,Financials,US6068221042
91 | NEE,"NextEra Energy, Inc.",Utilities - Regulated Electric,United States,Utilities,US65339F1012
92 | CMCSA,Comcast Corporation,Telecom Services,United States,Communication Services,US20030N1019
93 | PGR,The Progressive Corporation,Insurance - Property & Casualty,United States,Financials,US7433151039
94 | HON,Honeywell International Inc.,Conglomerates,United States,Industrials,US4385161066
95 | UBER,"Uber Technologies, Inc.",Software - Application,United States,Technology,US90353T1007
96 | AMAT,"Applied Materials, Inc.",Semiconductor Equipment & Materials,United States,Technology,US0382221051
97 | TJX,"The TJX Companies, Inc.",Apparel Retail,United States,Consumer Discretionary,US8725401090
98 | SONY,Sony Group Corporation,Consumer Electronics,Japan,Technology,US8356993076
99 | ANET,Arista Networks Inc,Computer Hardware,United States,Technology,US0404131064
100 | BA,The Boeing Company,Aerospace & Defense,United States,Industrials,US0970231058
101 | SNY,Sanofi,Drug Manufacturers - General,France,Healthcare,US80105N1054
102 | COP,ConocoPhillips,Oil & Gas Exploration & Production,United States,Energy,US20825C1045
103 | TTE,TotalEnergies SE,Oil & Gas Integrated,France,Energy,US89151E1091
104 | DE,Deere & Company,Farm & Heavy Construction Machinery,United States,Industrials,US2441991054
105 | PANW,"Palo Alto Networks, Inc.",Software - Infrastructure,United States,Technology,US6974351057
106 | BHP,BHP Group Limited,Other Industrial Metals & Mining,Australia,Materials,US0886061086
107 | ETN,Eaton Corporation plc,Specialty Industrial Machinery,Ireland,Industrials,IE00B8KQN827
108 | ADP,"Automatic Data Processing, Inc.",Software - Application,United States,Technology,US0530151036
109 | APP,AppLovin Corporation,Software - Application,United States,Technology,US03831W1080
110 | FI,"Fiserv, Inc.",Information Technology Services,United States,Technology,US3377381088
111 | BMY,Bristol-Myers Squibb Company,Drug Manufacturers - General,United States,Healthcare,US1101221083
112 | MDT,Medtronic plc,Medical Devices,Ireland,Healthcare,IE00BTN1Y115
113 | GILD,"Gilead Sciences, Inc.",Drug Manufacturers - General,United States,Healthcare,US3755581036
114 | UPS,"United Parcel Service, Inc.",Integrated Freight & Logistics,United States,Industrials,US9113121068
115 | SBUX,Starbucks Corporation,Restaurants,United States,Consumer Discretionary,US8552441094
116 | VRTX,Vertex Pharmaceuticals Incorporated,Biotechnology,United States,Healthcare,US92532F1003
117 | PLD,"Prologis, Inc.",REIT - Industrial,United States,Real Estate,US74340W1036
118 | UBS,UBS Group AG,Banks - Diversified,Switzerland,Financials,CH0244767585
119 | NKE,"NIKE, Inc.",Footwear & Accessories,United States,Consumer Discretionary,US6541061031
120 | CB,Chubb Limited,Insurance - Property & Casualty,Switzerland,Financials,CH0044328745
121 | MMC,"Marsh & McLennan Companies, Inc.",Insurance Brokers,United States,Financials,US5717481023
122 | LMT,Lockheed Martin Corporation,Aerospace & Defense,United States,Industrials,US5398301094
123 | SPOT,Spotify Technology S.A.,Internet Content & Information,Luxembourg,Communication Services,LU1778762911
124 | ADI,"Analog Devices, Inc.",Semiconductors,United States,Technology,US0326541051
125 | RIO,Rio Tinto Group,Other Industrial Metals & Mining,United Kingdom,Materials,US7672041008
126 | IBN,ICICI Bank Limited,Banks - Regional,India,Financials,US45104G1040
127 | CRWD,"CrowdStrike Holdings, Inc.",Software - Infrastructure,United States,Technology,US22788C1053
128 | TD,The Toronto-Dominion Bank,Banks - Diversified,Canada,Financials,CA8911605092
129 | MU,"Micron Technology, Inc.",Semiconductors,United States,Technology,US5951121038
130 | GEV,GE Vernova Inc.,Utilities - Renewable,United States,Utilities,US36828A1016
131 | BUD,Anheuser-Busch InBev SA/NV,Beverages - Brewers,Belgium,Consumer Staples,US03524A1088
132 | SMFG,"Sumitomo Mitsui Financial Group, Inc.",Banks - Diversified,Japan,Financials,US86562M2098
133 | ENB,Enbridge Inc.,Oil & Gas Midstream,Canada,Energy,CA29250N1050
134 | MELI,"MercadoLibre, Inc.",Internet Retail,Uruguay,Consumer Discretionary,US58733R1023
135 | LRCX,Lam Research Corporation,Semiconductor Equipment & Materials,United States,Technology,US5128071082
136 | APO,"Apollo Global Management, Inc.",Asset Management,United States,Financials,US03769M1062
137 | KLAC,KLA Corporation,Semiconductor Equipment & Materials,United States,Technology,US4824801009
138 | ELV,"Elevance Health, Inc.",Healthcare Plans,United States,Healthcare,US0367521038
139 | SO,The Southern Company,Utilities - Regulated Electric,United States,Utilities,US8425871071
140 | SHW,The Sherwin-Williams Company,Specialty Chemicals,United States,Materials,US8243481061
141 | RELX,RELX PLC,Specialty Business Services,United Kingdom,Industrials,US7595301083
142 | ICE,"Intercontinental Exchange, Inc.",Financial Data & Stock Exchanges,United States,Financials,US45866F1049
143 | BN,Brookfield Corporation,Asset Management,Canada,Financials,CA11271J1075
144 | MRVL,"Marvell Technology, Inc.",Semiconductors,United States,Technology,US5738741041
145 | MCO,Moody's Corporation,Financial Data & Stock Exchanges,United States,Financials,US6153691059
146 | MO,"Altria Group, Inc.",Tobacco,United States,Consumer Staples,US02209S1033
147 | PYPL,"PayPal Holdings, Inc.",Credit Services,United States,Financials,US70450Y1038
148 | INFY,Infosys Limited,Information Technology Services,India,Technology,US4567881085
149 | EQIX,"Equinix, Inc.",REIT - Specialty,United States,Real Estate,US29444U7000
150 | AMT,American Tower Corporation,REIT - Specialty,United States,Real Estate,US03027X1000
151 | CEG,Constellation Energy Corporation,Utilities - Renewable,United States,Utilities,US21037T1097
152 | BTI,British American Tobacco p.l.c.,Tobacco,United Kingdom,Consumer Staples,US1104481072
153 | PBR,Petróleo Brasileiro S.A. - Petrobras,Oil & Gas Integrated,Brazil,Energy,US71654V4086
154 | PBR.A,Petróleo Brasileiro S.A. - Petrobras,Oil & Gas Integrated,Brazil,Energy,US71654V1017
155 | DUK,Duke Energy Corporation,Utilities - Regulated Electric,United States,Utilities,US26441C2044
156 | PH,Parker-Hannifin Corporation,Specialty Industrial Machinery,United States,Industrials,US7010941042
157 | WM,"Waste Management, Inc.",Waste Management,United States,Industrials,US94106L1098
158 | WELL,Welltower Inc.,REIT - Healthcare Facilities,United States,Real Estate,US95040Q1040
159 | INTC,Intel Corporation,Semiconductors,United States,Technology,US4581401001
160 | CME,CME Group Inc.,Financial Data & Stock Exchanges,United States,Financials,US12572Q1058
161 | CI,The Cigna Group,Healthcare Plans,United States,Healthcare,US1255231003
162 | MSTR,MicroStrategy Incorporated,Software - Application,United States,Technology,US5949724083
163 | HCA,"HCA Healthcare, Inc.",Medical Care Facilities,United States,Healthcare,US40412C1018
164 | APH,Amphenol Corporation,Electronic Components,United States,Technology,US0320951017
165 | TT,Trane Technologies plc,Building Products & Equipment,Ireland,Industrials,IE00BK9ZQ967
166 | CDNS,"Cadence Design Systems, Inc.",Software - Application,United States,Technology,US1273871087
167 | ABNB,"Airbnb, Inc.",Travel Services,United States,Consumer Discretionary,US0090661010
168 | BP,BP p.l.c.,Oil & Gas Integrated,United Kingdom,Energy,US0556221044
169 | MMM,3M Company,Conglomerates,United States,Industrials,US88579Y1010
170 | SNPS,"Synopsys, Inc.",Software - Infrastructure,United States,Technology,US8716071076
171 | CTAS,Cintas Corporation,Specialty Business Services,United States,Industrials,US1729081059
172 | AON,Aon plc,Insurance Brokers,Ireland,Financials,IE00BLP1HW54
173 | MAR,"Marriott International, Inc.",Lodging,United States,Consumer Discretionary,US5719032022
174 | PNC,"The PNC Financial Services Group, Inc.",Banks - Regional,United States,Financials,US6934751057
175 | CMG,"Chipotle Mexican Grill, Inc.",Restaurants,United States,Consumer Discretionary,US1696561059
176 | MSI,"Motorola Solutions, Inc.",Communication Equipment,United States,Technology,US6200763075
177 | SAN,"Banco Santander, S.A.",Banks - Diversified,Spain,Financials,US05964H1059
178 | COF,Capital One Financial Corporation,Credit Services,United States,Financials,US14040H1059
179 | RACE,Ferrari N.V.,Auto Manufacturers,Italy,Consumer Discretionary,NL0011585146
180 | ZTS,Zoetis Inc.,Drug Manufacturers - Specialty & Generic,United States,Healthcare,US98978V1035
181 | DASH,"DoorDash, Inc.",Internet Content & Information,United States,Communication Services,US25809K1051
182 | MCK,McKesson Corporation,Medical Distribution,United States,Healthcare,US58155Q1031
183 | FTNT,"Fortinet, Inc.",Software - Infrastructure,United States,Technology,US34959E1091
184 | ITW,Illinois Tool Works Inc.,Specialty Industrial Machinery,United States,Industrials,US4523081093
185 | MDLZ,"Mondelez International, Inc.",Confectioners,United States,Consumer Staples,US6092071058
186 | USB,U.S. Bancorp,Banks - Regional,United States,Financials,US9029733048
187 | TRI,Thomson Reuters Corporation,Specialty Business Services,Canada,Industrials,CA8849038085
188 | TDG,TransDigm Group Incorporated,Aerospace & Defense,United States,Industrials,US8936411003
189 | EMR,Emerson Electric Co.,Specialty Industrial Machinery,United States,Industrials,US2910111044
190 | CP,Canadian Pacific Kansas City Limited,Railroads,Canada,Industrials,CA13646K1084
191 | REGN,"Regeneron Pharmaceuticals, Inc.",Biotechnology,United States,Healthcare,US75886F1075
192 | ORLY,"O'Reilly Automotive, Inc.",Specialty Retail,United States,Consumer Discretionary,US67103H1077
193 | CL,Colgate-Palmolive Company,Household & Personal Products,United States,Consumer Staples,US1941621039
194 | BMO,Bank of Montreal,Banks - Diversified,Canada,Financials,CA0636711016
195 | AJG,Arthur J. Gallagher & Co.,Insurance Brokers,United States,Financials,US3635761097
196 | EPD,Enterprise Products Partners L.P.,Oil & Gas Midstream,United States,Energy,US2937921078
197 | EOG,"EOG Resources, Inc.",Oil & Gas Exploration & Production,United States,Energy,US26875P1012
198 | APD,"Air Products and Chemicals, Inc.",Specialty Chemicals,United States,Materials,US0091581068
199 | BDX,"Becton, Dickinson and Company",Medical Instruments & Supplies,United States,Healthcare,US0758871091
200 | CVS,CVS Health Corporation,Healthcare Plans,United States,Healthcare,US1266501006
201 | GD,General Dynamics Corporation,Aerospace & Defense,United States,Industrials,US3695501086
202 | WDAY,"Workday, Inc.",Software - Application,United States,Technology,US98138H1014
203 | SCCO,Southern Copper Corporation,Copper,United States,Materials,US84265V1052
204 | TEAM,Atlassian Corporation,Software - Application,Australia,Technology,US0494681010
205 | RCL,Royal Caribbean Cruises Ltd.,Travel Services,United States,Consumer Discretionary,LR0008862868
206 | NOC,Northrop Grumman Corporation,Aerospace & Defense,United States,Industrials,US6668071029
207 | DELL,Dell Technologies Inc.,Computer Hardware,United States,Technology,US24703L2025
208 | ECL,Ecolab Inc.,Specialty Chemicals,United States,Materials,US2788651006
209 | COIN,"Coinbase Global, Inc.",Financial Data & Stock Exchanges,United States,Financials,US19260Q1076
210 | GSK,GSK plc,Drug Manufacturers - General,United Kingdom,Healthcare,US37733W2044
211 | ET,Energy Transfer LP,Oil & Gas Midstream,United States,Energy,US29273V1008
212 | DEO,Diageo plc,Beverages - Wineries & Distilleries,United Kingdom,Consumer Staples,US25243Q2057
213 | MFG,"Mizuho Financial Group, Inc.",Banks - Regional,Japan,Financials,US60687Y1091
214 | SE,Sea Limited,Internet Retail,Singapore,Consumer Discretionary,US81141R1005
215 | RSG,"Republic Services, Inc.",Waste Management,United States,Industrials,US7607591002
216 | WMB,"The Williams Companies, Inc.",Oil & Gas Midstream,United States,Energy,US9694571004
217 | FDX,FedEx Corporation,Integrated Freight & Logistics,United States,Industrials,US31428X1063
218 | CRH,CRH plc,Building Materials,Ireland,Materials,IE0001827041
219 | NTES,"NetEase, Inc.",Electronic Gaming & Multimedia,China,Communication Services,US64110W1027
220 | ADSK,"Autodesk, Inc.",Software - Application,United States,Technology,US0527691069
221 | CNI,Canadian National Railway Company,Railroads,Canada,Industrials,CA1363751027
222 | SPG,"Simon Property Group, Inc.",REIT - Retail,United States,Real Estate,US8288061091
223 | TGT,Target Corporation,Discount Stores,United States,Consumer Staples,US87612E1064
224 | CNQ,Canadian Natural Resources Limited,Oil & Gas Exploration & Production,Canada,Energy,CA1363851017
225 | BNS,The Bank of Nova Scotia,Banks - Diversified,Canada,Financials,CA0641491075
226 | EQNR,Equinor ASA,Oil & Gas Integrated,Norway,Energy,US29446M1027
227 | CSX,CSX Corporation,Railroads,United States,Industrials,US1264081035
228 | TFC,Truist Financial Corporation,Banks - Regional,United States,Financials,US89832Q1094
229 | SNOW,Snowflake Inc.,Software - Application,United States,Technology,US8334451098
230 | BK,The Bank of New York Mellon Corporation,Banks - Diversified,United States,Financials,US0640581007
231 | HLT,Hilton Worldwide Holdings Inc.,Lodging,United States,Consumer Discretionary,US43300A2033
232 | BBVA,"Banco Bilbao Vizcaya Argentaria, S.A.",Banks - Diversified,Spain,Financials,US05946K1016
233 | KMI,"Kinder Morgan, Inc.",Oil & Gas Midstream,United States,Energy,US49456B1017
234 | CM,Canadian Imperial Bank of Commerce,Banks - Diversified,Canada,Financials,CA1360691010
235 | NU,Nu Holdings Ltd.,Banks - Regional,Brazil,Financials,KYG6683N1034
236 | ARES,Ares Management Corporation,Asset Management,United States,Financials,US03990B1017
237 | CARR,Carrier Global Corporation,Building Products & Equipment,United States,Industrials,US14448C1045
238 | AFL,Aflac Incorporated,Insurance - Life,United States,Financials,US0010551028
239 | JD,"JD.com, Inc.",Internet Retail,China,Consumer Discretionary,US47215P1066
240 | TTD,"The Trade Desk, Inc.",Software - Application,United States,Technology,US88339J1051
241 | MET,"MetLife, Inc.",Insurance - Life,United States,Financials,US59156R1086
242 | NGG,National Grid plc,Utilities - Regulated Electric,United Kingdom,Utilities,US6362744095
243 | ROP,"Roper Technologies, Inc.",Software - Application,United States,Technology,US7766961061
244 | OKE,"ONEOK, Inc.",Oil & Gas Midstream,United States,Energy,US6826801036
245 | CHTR,"Charter Communications, Inc.",Telecom Services,United States,Communication Services,US16119P1084
246 | SLB,Schlumberger Limited,Oil & Gas Equipment & Services,United States,Energy,AN8068571086
247 | NSC,Norfolk Southern Corporation,Railroads,United States,Industrials,US6558441084
248 | TRV,"The Travelers Companies, Inc.",Insurance - Property & Casualty,United States,Financials,US89417E1091
249 | PCAR,PACCAR Inc,Farm & Heavy Construction Machinery,United States,Industrials,US6937181088
250 | AZO,"AutoZone, Inc.",Specialty Retail,United States,Consumer Discretionary,US0533321024
251 | AMP,"Ameriprise Financial, Inc.",Asset Management,United States,Financials,US03076C1062
252 | CPRT,"Copart, Inc.",Specialty Business Services,United States,Industrials,US2172041061
253 | GWW,"W.W. Grainger, Inc.",Industrial Distribution,United States,Industrials,US3848021040
254 | GM,General Motors Company,Auto Manufacturers,United States,Consumer Discretionary,US37045V1008
255 | XYZ,"Block, Inc.",Software - Infrastructure,United States,Technology,US8522341036
256 | DLR,"Digital Realty Trust, Inc.",REIT - Specialty,United States,Real Estate,US2538681030
257 | NXPI,NXP Semiconductors N.V.,Semiconductors,Netherlands,Technology,NL0009538784
258 | AEP,"American Electric Power Company, Inc.",Utilities - Regulated Electric,United States,Utilities,US0255371017
259 | PAYX,"Paychex, Inc.",Software - Application,United States,Technology,US7043261079
260 | MPLX,MPLX LP,Oil & Gas Midstream,United States,Energy,US55336V1008
261 | PSA,Public Storage,REIT - Industrial,United States,Real Estate,US74460D1090
262 | MFC,Manulife Financial Corporation,Insurance - Life,Canada,Financials,CA56501R1064
263 | ITUB,Itaú Unibanco Holding S.A.,Banks - Regional,Brazil,Financials,US4655621062
264 | SRE,Sempra,Utilities - Diversified,United States,Utilities,US8168511090
265 | BCS,Barclays PLC,Banks - Diversified,United Kingdom,Financials,US06738E2046
266 | CVNA,Carvana Co.,Auto & Truck Dealerships,United States,Consumer Discretionary,US1468691027
267 | DDOG,"Datadog, Inc.",Software - Application,United States,Technology,US23804L1035
268 | FCX,Freeport-McMoRan Inc.,Copper,United States,Materials,US35671D8570
269 | ING,ING Groep N.V.,Banks - Diversified,Netherlands,Financials,US4568371037
270 | HWM,Howmet Aerospace Inc.,Aerospace & Defense,United States,Industrials,US4432011082
271 | VST,Vistra Corp.,Utilities - Independent Power Producers,United States,Utilities,US92840M1027
272 | LNG,"Cheniere Energy, Inc.",Oil & Gas Midstream,United States,Energy,US16411R2085
273 | ALL,The Allstate Corporation,Insurance - Property & Casualty,United States,Financials,US0200021014
274 | URI,"United Rentals, Inc.",Rental & Leasing Services,United States,Industrials,US9113631090
275 | JCI,Johnson Controls International plc,Building Products & Equipment,Ireland,Industrials,IE00BY7QL619
276 | DFS,Discover Financial Services,Credit Services,United States,Financials,US2547091080
277 | PSX,Phillips 66,Oil & Gas Refining & Marketing,United States,Energy,US7185461040
278 | LULU,Lululemon Athletica Inc.,Apparel Retail,Canada,Consumer Discretionary,US5500211090
279 | COR,"Cencora, Inc.",Medical Distribution,United States,Healthcare,US03073E1055
280 | FANG,"Diamondback Energy, Inc.",Oil & Gas Exploration & Production,United States,Energy,US25278X1090
281 | MSCI,MSCI Inc.,Financial Data & Stock Exchanges,United States,Financials,US55354G1004
282 | ROST,"Ross Stores, Inc.",Apparel Retail,United States,Consumer Discretionary,US7782961038
283 | AXON,"Axon Enterprise, Inc.",Aerospace & Defense,United States,Industrials,US05464C1018
284 | MPC,Marathon Petroleum Corporation,Oil & Gas Refining & Marketing,United States,Energy,US56585A1025
285 | VG,"Venture Global, Inc.",Oil & Gas Exploration & Production,,Energy,
286 | O,Realty Income Corporation,REIT - Retail,United States,Real Estate,US7561091049
287 | SU,Suncor Energy Inc.,Oil & Gas Integrated,Canada,Energy,CA8672241079
288 | CMI,Cummins Inc.,Specialty Industrial Machinery,United States,Industrials,US2310211063
289 | NET,"Cloudflare, Inc.",Software - Infrastructure,United States,Technology,US18915M1071
290 | FLUT,Flutter Entertainment plc,Gambling,Ireland,Consumer Discretionary,IE00BWT6H894
291 | MNST,Monster Beverage Corporation,Beverages - Non-Alcoholic,United States,Consumer Staples,US61174X1090
292 | WCN,"Waste Connections, Inc.",Waste Management,Canada,Industrials,CA94106B1013
293 | TRP,TC Energy Corporation,Oil & Gas Midstream,Canada,Energy,CA87807B1076
294 | AIG,"American International Group, Inc.",Insurance - Diversified,United States,Financials,US0268747849
295 | NDAQ,"Nasdaq, Inc.",Financial Data & Stock Exchanges,United States,Financials,US6311031081
296 | NEM,Newmont Corporation,Gold,United States,Materials,US6516391066
297 | TCOM,Trip.com Group Limited,Travel Services,Singapore,Consumer Discretionary,US89677Q1076
298 | D,"Dominion Energy, Inc.",Utilities - Regulated Electric,United States,Utilities,US25746U1097
299 | LYG,Lloyds Banking Group plc,Banks - Regional,United Kingdom,Financials,US5394391099
300 | OXY,Occidental Petroleum Corporation,Oil & Gas Exploration & Production,United States,Energy,US6745991058
301 | DHI,"D.R. Horton, Inc.",Residential Construction,United States,Consumer Discretionary,US23331A1097
302 | ALC,Alcon Inc.,Medical Instruments & Supplies,Switzerland,Healthcare,CH0432492467
303 | FICO,Fair Isaac Corporation,Software - Application,United States,Technology,US3032501047
304 | AEM,Agnico Eagle Mines Limited,Gold,Canada,Materials,CA0084741085
305 | RBLX,Roblox Corporation,Electronic Gaming & Multimedia,United States,Communication Services,US7710491033
306 | HES,Hess Corporation,Oil & Gas Exploration & Production,United States,Energy,US42809H1077
307 | HMC,"Honda Motor Co., Ltd.",Auto Manufacturers,Japan,Consumer Discretionary,US4381283088
308 | TEL,TE Connectivity plc,Electronic Components,Ireland,Technology,CH0102993182
309 | CTVA,"Corteva, Inc.",Agricultural Inputs,United States,Materials,US22052L1044
310 | TRGP,Targa Resources Corp.,Oil & Gas Midstream,United States,Energy,US87612G1013
311 | GLW,Corning Incorporated,Electronic Components,United States,Technology,US2193501051
312 | VLO,Valero Energy Corporation,Oil & Gas Refining & Marketing,United States,Energy,US91913Y1001
313 | KR,The Kroger Co.,Grocery Stores,United States,Consumer Staples,US5010441013
314 | HOOD,"Robinhood Markets, Inc.",Capital Markets,United States,Financials,US7707001027
315 | PWR,"Quanta Services, Inc.",Engineering & Construction,United States,Industrials,US74762E1029
316 | DAL,"Delta Air Lines, Inc.",Airlines,United States,Industrials,US2473617023
317 | FIS,"Fidelity National Information Services, Inc.",Information Technology Services,United States,Technology,US31620M1062
318 | AMX,"América Móvil, S.A.B. de C.V.",Telecom Services,Mexico,Communication Services,US02390A1016
319 | KMB,Kimberly-Clark Corporation,Household & Personal Products,United States,Consumer Staples,US4943681035
320 | E,Eni S.p.A.,Oil & Gas Integrated,Italy,Energy,US26874R1086
321 | PRU,"Prudential Financial, Inc.",Insurance - Life,United States,Financials,US7443201022
322 | A,"Agilent Technologies, Inc.",Diagnostics & Research,United States,Healthcare,US00846U1016
323 | CBRE,"CBRE Group, Inc.",Real Estate Services,United States,Real Estate,US12504L1098
324 | FAST,Fastenal Company,Industrial Distribution,United States,Industrials,US3119001044
325 | BKR,Baker Hughes Company,Oil & Gas Equipment & Services,United States,Energy,US05722G1004
326 | EW,Edwards Lifesciences Corporation,Medical Devices,United States,Healthcare,US28176E1082
327 | NWG,NatWest Group plc,Banks - Regional,United Kingdom,Financials,US6390572070
328 | HLN,Haleon plc,Drug Manufacturers - Specialty & Generic,United Kingdom,Healthcare,US4055521003
329 | KDP,Keurig Dr Pepper Inc.,Beverages - Non-Alcoholic,United States,Consumer Staples,US49271V1008
330 | TAK,Takeda Pharmaceutical Company Limited,Drug Manufacturers - Specialty & Generic,Japan,Healthcare,US8740602052
331 | AME,"AMETEK, Inc.",Specialty Industrial Machinery,United States,Industrials,US0311001004
332 | IT,"Gartner, Inc.",Information Technology Services,United States,Technology,US3666511072
333 | GRMN,Garmin Ltd.,Scientific & Technical Instruments,Switzerland,Technology,CH0114405324
334 | CPNG,"Coupang, Inc.",Internet Retail,United States,Consumer Discretionary,US22266T1097
335 | HUBS,"HubSpot, Inc.",Software - Application,United States,Technology,US4435731009
336 | KVUE,Kenvue Inc.,Household & Personal Products,United States,Consumer Staples,US49177J1025
337 | PEG,Public Service Enterprise Group Incorporated,Utilities - Regulated Electric,United States,Utilities,US7445731067
338 | ODFL,"Old Dominion Freight Line, Inc.",Trucking,United States,Industrials,US6795801009
339 | LHX,"L3Harris Technologies, Inc.",Aerospace & Defense,United States,Industrials,US5024311095
340 | ATE,Advantest Corporation,Other,,,
341 | CTSH,Cognizant Technology Solutions Corporation,Information Technology Services,United States,Technology,US1924461023
342 | GEHC,GE HealthCare Technologies Inc.,Health Information Services,United States,Healthcare,US36266G1076
343 | F,Ford Motor Company,Auto Manufacturers,United States,Consumer Discretionary,US3453708600
344 | EXC,Exelon Corporation,Utilities - Regulated Electric,United States,Utilities,US30161N1019
345 | VRT,Vertiv Holdings Co,Electrical Equipment & Parts,United States,Industrials,US92537N1081
346 | VRSK,"Verisk Analytics, Inc.",Consulting Services,United States,Industrials,US92345Y1064
347 | ARGX,argenx SE,Biotechnology,Netherlands,Healthcare,NL0010832176
348 | DB,Deutsche Bank Aktiengesellschaft,Banks - Regional,Germany,Financials,DE0005140008
349 | CCI,Crown Castle Inc.,REIT - Specialty,United States,Real Estate,US22822V1017
350 | OWL,Blue Owl Capital Inc.,Asset Management,United States,Financials,US09581B1035
351 | VALE,Vale S.A.,Other Industrial Metals & Mining,Brazil,Materials,US91912E1055
352 | OTIS,Otis Worldwide Corporation,Specialty Industrial Machinery,United States,Industrials,US68902V1070
353 | XEL,Xcel Energy Inc.,Utilities - Regulated Electric,United States,Utilities,US98389B1008
354 | WIT,Wipro Limited,Information Technology Services,India,Technology,US97651M1099
355 | VEEV,Veeva Systems Inc.,Health Information Services,United States,Healthcare,US9224751084
356 | IQV,IQVIA Holdings Inc.,Diagnostics & Research,United States,Healthcare,US46266C1053
357 | RMD,ResMed Inc.,Medical Instruments & Supplies,United States,Healthcare,US7611521078
358 | STLA,Stellantis N.V.,Auto Manufacturers,Netherlands,Consumer Discretionary,NL00150001Q9
359 | IR,Ingersoll Rand Inc.,Specialty Industrial Machinery,United States,Industrials,US45687V1061
360 | FERG,Ferguson Enterprises Inc.,Industrial Distribution,United States,Industrials,JE00BJVNSS43
361 | HUM,Humana Inc.,Healthcare Plans,United States,Healthcare,US4448591028
362 | IMO,Imperial Oil Limited,Oil & Gas Integrated,Canada,Energy,CA4530384086
363 | CCL,Carnival Corporation & plc,Travel Services,United States,Consumer Discretionary,GB0031215220
364 | VMC,Vulcan Materials Company,Building Materials,United States,Materials,US9291601097
365 | LEN,Lennar Corporation,Residential Construction,United States,Consumer Discretionary,US5260571048
366 | YUM,"Yum! Brands, Inc.",Restaurants,United States,Consumer Discretionary,US9884981013
367 | ALNY,"Alnylam Pharmaceuticals, Inc.",Biotechnology,United States,Healthcare,US02043Q1076
368 | CUK,Carnival Corporation & plc,Leisure,United States,Consumer Discretionary,US14365C1036
369 | CCEP,Coca-Cola Europacific Partners PLC,Beverages - Non-Alcoholic,United Kingdom,Consumer Staples,GB00BDCPN049
370 | LEN.B,Lennar Corporation,Residential Construction,United States,Consumer Discretionary,US5260573028
371 | KHC,The Kraft Heinz Company,Packaged Foods,United States,Consumer Staples,US5007541064
372 | ACGL,Arch Capital Group Ltd.,Insurance - Diversified,Bermuda,Financials,BMG0450A1053
373 | SYY,Sysco Corporation,Food Distribution,United States,Consumer Staples,US8718291078
374 | WAB,Westinghouse Air Brake Technologies Corporation,Railroads,United States,Industrials,US9297401088
375 | RJF,"Raymond James Financial, Inc.",Asset Management,United States,Financials,US7547301090
376 | UAL,"United Airlines Holdings, Inc.",Airlines,United States,Industrials,US9100471096
377 | PCG,PG&E Corporation,Utilities - Regulated Electric,United States,Utilities,US69331C1080
378 | DXCM,"DexCom, Inc.",Medical Devices,United States,Healthcare,US2521311074
379 | IDXX,"IDEXX Laboratories, Inc.",Diagnostics & Research,United States,Healthcare,US45168D1046
380 | RDDT,"Reddit, Inc.",Internet Content & Information,United States,Communication Services,US75734B1008
381 | EXR,Extra Space Storage Inc.,REIT - Industrial,United States,Real Estate,US30225T1025
382 | EFX,Equifax Inc.,Consulting Services,United States,Industrials,US2944291051
383 | SLF,Sun Life Financial Inc.,Insurance - Diversified,Canada,Financials,CA8667961053
384 | ETR,Entergy Corporation,Utilities - Regulated Electric,United States,Utilities,US29364G1031
385 | MLM,"Martin Marietta Materials, Inc.",Building Materials,United States,Materials,US5732841060
386 | STZ,"Constellation Brands, Inc.",Beverages - Brewers,United States,Consumer Staples,US21036P1084
387 | MTB,M&T Bank Corporation,Banks - Regional,United States,Financials,US55261F1049
388 | GIS,"General Mills, Inc.",Packaged Foods,United States,Consumer Staples,US3703341046
389 | HIG,"The Hartford Financial Services Group, Inc.",Insurance - Property & Casualty,United States,Financials,US4165151048
390 | TTWO,"Take-Two Interactive Software, Inc.",Electronic Gaming & Multimedia,United States,Communication Services,US8740541094
391 | LYV,"Live Nation Entertainment, Inc.",Entertainment,United States,Communication Services,US5380341090
392 | WTW,Willis Towers Watson Public Limited Company,Insurance Brokers,United Kingdom,Financials,IE00BDB6Q211
393 | DECK,Deckers Outdoor Corporation,Footwear & Accessories,United States,Consumer Discretionary,US2435371073
394 | CNC,Centene Corporation,Healthcare Plans,United States,Healthcare,US15135B1017
395 | HEI,HEICO Corporation,Aerospace & Defense,United States,Industrials,US4228061093
396 | ED,"Consolidated Edison, Inc.",Utilities - Regulated Electric,United States,Utilities,US2091151041
397 | EBAY,eBay Inc.,Internet Retail,United States,Consumer Discretionary,US2786421030
398 | BIDU,"Baidu, Inc.",Internet Content & Information,China,Communication Services,US0567521085
399 | FER,Ferrovial SE,Infrastructure Operations,Netherlands,Industrials,NL0015001FS8
400 | DD,"DuPont de Nemours, Inc.",Specialty Chemicals,United States,Materials,US26614N1028
401 | ROK,"Rockwell Automation, Inc.",Specialty Industrial Machinery,United States,Industrials,US7739031091
402 | VICI,VICI Properties Inc.,REIT - Diversified,United States,Real Estate,US9256521090
403 | ZS,"Zscaler, Inc.",Software - Infrastructure,United States,Technology,US98980G1022
404 | LVS,Las Vegas Sands Corp.,Resorts & Casinos,United States,Consumer Discretionary,US5178341070
405 | WEC,"WEC Energy Group, Inc.",Utilities - Regulated Electric,United States,Utilities,US92939U1060
406 | CSGP,"CoStar Group, Inc.",Real Estate Services,United States,Real Estate,US22160N1090
407 | AVB,"AvalonBay Communities, Inc.",REIT - Residential,United States,Real Estate,US0534841012
408 | CAH,"Cardinal Health, Inc.",Medical Distribution,United States,Healthcare,US14149Y1082
409 | HPQ,HP Inc.,Computer Hardware,United States,Technology,US40434L1052
410 | TSCO,Tractor Supply Company,Specialty Retail,United States,Consumer Discretionary,US8923561067
411 | ANSS,"ANSYS, Inc.",Software - Application,United States,Technology,US03662Q1058
412 | EA,Electronic Arts Inc.,Electronic Gaming & Multimedia,United States,Communication Services,US2855121099
413 | TW,Tradeweb Markets Inc.,Capital Markets,United States,Financials,US8926721064
414 | HSY,The Hershey Company,Confectioners,United States,Consumer Staples,US4278661081
415 | MCHP,Microchip Technology Incorporated,Semiconductors,United States,Technology,US5950171042
416 | MPWR,"Monolithic Power Systems, Inc.",Semiconductors,United States,Technology,US6098391054
417 | GDDY,GoDaddy Inc.,Software - Infrastructure,United States,Technology,US3802371076
418 | BRO,"Brown & Brown, Inc.",Insurance Brokers,United States,Financials,US1152361010
419 | FITB,Fifth Third Bancorp,Banks - Regional,United States,Financials,US3167731005
420 | CQP,"Cheniere Energy Partners, L.P.",Oil & Gas Midstream,United States,Energy,US16411Q1013
421 | FCNCA,"First Citizens BancShares, Inc.",Banks - Regional,United States,Financials,US31946M1036
422 | BNTX,BioNTech SE,Biotechnology,Germany,Healthcare,US09075V1026
423 | EL,The Estée Lauder Companies Inc.,Household & Personal Products,United States,Consumer Staples,US5184391044
424 | ABEV,Ambev S.A.,Beverages - Brewers,Brazil,Consumer Staples,US02319V1035
425 | EQT,EQT Corporation,Oil & Gas Exploration & Production,United States,Energy,US26884L1098
426 | NUE,Nucor Corporation,Steel,United States,Materials,US6703461052
427 | CHT,"Chunghwa Telecom Co., Ltd.",Telecom Services,Taiwan,Communication Services,US17133Q5027
428 | XYL,Xylem Inc.,Specialty Industrial Machinery,United States,Industrials,US98419M1009
429 | FCNCO,"First Citizens BancShares, Inc.",Banks - Regional,United States,Financials,US31959X2027
430 | TPL,Texas Pacific Land Corporation,Oil & Gas Exploration & Production,United States,Energy,US88262P1021
431 | WDS,Woodside Energy Group Ltd,Oil & Gas Exploration & Production,Australia,Energy,US9802283088
432 | DOW,Dow Inc.,Chemicals,United States,Materials,US2605571031
433 | IOT,Samsara Inc.,Software - Infrastructure,United States,Technology,US79589L1061
434 | KEYS,"Keysight Technologies, Inc.",Scientific & Technical Instruments,United States,Technology,US49338L1035
435 | STT,State Street Corporation,Asset Management,United States,Financials,US8574771031
436 | IRM,Iron Mountain Incorporated,REIT - Specialty,United States,Real Estate,US46284V1017
437 | FMX,"Fomento Económico Mexicano, S.A.B. de C.V.",Beverages - Brewers,Mexico,Consumer Staples,US3444191064
438 | HEI.A,HEICO Corporation,Aerospace & Defense,United States,Industrials,US4228062083
439 | MTD,Mettler-Toledo International Inc.,Diagnostics & Research,United States,Healthcare,US5926881054
440 | PPG,"PPG Industries, Inc.",Specialty Chemicals,United States,Materials,US6935061076
441 | HPE,Hewlett Packard Enterprise Company,Communication Equipment,United States,Technology,US42824C1099
442 | K,Kellanova,Packaged Foods,United States,Consumer Staples,US4878361082
443 | SW,Smurfit Westrock Plc,Packaging & Containers,Ireland,Consumer Discretionary,IE00028FXN24
444 | QSR,Restaurant Brands International Inc.,Restaurants,Canada,Consumer Discretionary,CA76131D1033
445 | GPN,Global Payments Inc.,Specialty Business Services,United States,Industrials,US37940X1028
446 | GOLD,Barrick Gold Corporation,Gold,Canada,Materials,CA0679011084
447 | FTV,Fortive Corporation,Scientific & Technical Instruments,United States,Technology,US34959J1088
448 | BR,"Broadridge Financial Solutions, Inc.",Information Technology Services,United States,Technology,US11133T1034
449 | WPM,Wheaton Precious Metals Corp.,Gold,Canada,Materials,CA9628791027
450 | DOV,Dover Corporation,Specialty Industrial Machinery,United States,Industrials,US2600031080
451 | ZM,Zoom Communications Inc.,Software - Application,United States,Technology,US98980L1017
452 | EQR,Equity Residential,REIT - Residential,United States,Real Estate,US29476L1070
453 | TKO,"TKO Group Holdings, Inc.",Entertainment,United States,Communication Services,US87256C1018
454 | LPLA,LPL Financial Holdings Inc.,Capital Markets,United States,Financials,US50212V1008
455 | CVE,Cenovus Energy Inc.,Oil & Gas Integrated,Canada,Energy,CA15135U1093
456 | TYL,"Tyler Technologies, Inc.",Software - Application,United States,Technology,US9022521051
457 | WSM,"Williams-Sonoma, Inc.",Specialty Retail,United States,Consumer Discretionary,US9699041011
458 | CPAY,"Corpay, Inc.",Software - Infrastructure,United States,Technology,US2199481068
459 | CHD,"Church & Dwight Co., Inc.",Household & Personal Products,United States,Consumer Staples,US1713401024
460 | RKT,"Rocket Companies, Inc.",Mortgage Finance,United States,Financials,US77311W1018
461 | CDW,CDW Corporation,Information Technology Services,United States,Technology,US12514G1085
462 | NTR,Nutrien Ltd.,Agricultural Inputs,Canada,Materials,CA67077M1086
463 | SYF,Synchrony Financial,Credit Services,United States,Financials,US87165B1035
464 | ERIC,Telefonaktiebolaget LM Ericsson (publ),Communication Equipment,Sweden,Technology,US2948216088
465 | GIB,CGI Inc.,Information Technology Services,Canada,Technology,CA12532H1047
466 | VTR,"Ventas, Inc.",REIT - Healthcare Facilities,United States,Real Estate,US92276F1003
467 | TROW,"T. Rowe Price Group, Inc.",Asset Management,United States,Financials,US74144T1088
468 | BAM,Brookfield Asset Management Ltd.,Asset Management,Canada,Financials,CA1130041058
469 | VLTO,Veralto Corporation,Pollution & Treatment Controls,United States,Industrials,US92338C1036
470 | PHG,Koninklijke Philips N.V.,Medical Devices,Netherlands,Healthcare,US5004723038
471 | LYB,LyondellBasell Industries N.V.,Specialty Chemicals,United States,Materials,NL0009434992
472 | FNV,Franco-Nevada Corporation,Gold,Canada,Materials,CA3518581051
473 | WBD,"Warner Bros. Discovery, Inc.",Entertainment,United States,Communication Services,US9344231041
474 | HBAN,Huntington Bancshares Incorporated,Banks - Regional,United States,Financials,US4461501045
475 | AEE,Ameren Corporation,Utilities - Regulated Electric,United States,Utilities,US0236081024
476 | WST,"West Pharmaceutical Services, Inc.",Medical Instruments & Supplies,United States,Healthcare,US9553061055
477 | AWK,"American Water Works Company, Inc.",Utilities - Regulated Water,United States,Utilities,US0304201033
478 | DTE,DTE Energy Company,Utilities - Regulated Electric,United States,Utilities,US2333311072
479 | WAT,Waters Corporation,Diagnostics & Research,United States,Healthcare,US9418481035
480 | TEVA,Teva Pharmaceutical Industries Limited,Drug Manufacturers - Specialty & Generic,Israel,Healthcare,US8816242098
481 | TPG,TPG Inc.,Asset Management,United States,Financials,US8726571016
482 | NTAP,"NetApp, Inc.",Computer Hardware,United States,Technology,US64110D1046
483 | NVR,"NVR, Inc.",Residential Construction,United States,Consumer Discretionary,US62944T1051
484 | PPL,PPL Corporation,Utilities - Regulated Electric,United States,Utilities,US69351T1060
485 | ADM,Archer-Daniels-Midland Company,Farm Products,United States,Consumer Staples,US0394831020
486 | ONC,"BeiGene, Ltd.",Biotechnology,Cayman Islands,Healthcare,
487 | IX,ORIX Corporation,Financial Conglomerates,Japan,Financials,US6863301015
488 | UI,Ubiquiti Inc.,Communication Equipment,United States,Technology,US90353W1036
489 | NOK,Nokia Oyj,Communication Equipment,Finland,Technology,US6549022043
490 | ROL,"Rollins, Inc.",Personal Services,United States,Consumer Discretionary,US7757111049
491 | TDY,Teledyne Technologies Incorporated,Scientific & Technical Instruments,United States,Technology,US8793601050
492 | FWONK,Formula One Group,Entertainment,United States,Communication Services,US5312297550
493 | LII,Lennox International Inc.,Building Products & Equipment,United States,Industrials,US5261071071
494 | EXE,Expand Energy Corporation,Oil & Gas Exploration & Production,United States,Energy,US1651677353
495 | PHM,"PulteGroup, Inc.",Residential Construction,United States,Consumer Discretionary,US7458671010
496 | MKL,Markel Group Inc.,Insurance - Property & Casualty,United States,Financials,US5705351048
497 | ASX,"ASE Technology Holding Co., Ltd.",Semiconductors,Taiwan,Technology,US00215W1009
498 | FWONA,Formula One Group,Entertainment,United States,Communication Services,US5312297717
499 | HAL,Halliburton Company,Oil & Gas Equipment & Services,United States,Energy,US4062161017
500 | KB,KB Financial Group Inc.,Banks - Regional,South Korea,Financials,US48241A1051
501 | LI,Li Auto Inc.,Auto Manufacturers,China,Consumer Discretionary,US50202M1027
502 | FE,FirstEnergy Corp.,Utilities - Regulated Electric,United States,Utilities,US3379321074
503 | RYAAY,Ryanair Holdings plc,Airlines,Ireland,Industrials,US7835132033
504 | TEF,"Telefónica, S.A.",Telecom Services,Spain,Communication Services,US8793822086
505 | PTC,PTC Inc.,Software - Application,United States,Technology,US69370C1009
506 | ON,ON Semiconductor Corporation,Semiconductors,United States,Technology,US6821891057
507 | DVN,Devon Energy Corporation,Oil & Gas Exploration & Production,United States,Energy,US25179M1036
508 | FOXA,Fox Corporation,Entertainment,United States,Communication Services,US35137L1052
509 | GFS,GlobalFoundries Inc.,Semiconductors,United States,Technology,KYG393871085
510 | TOST,"Toast, Inc.",Software - Infrastructure,United States,Technology,US8887871080
511 | IBKR,"Interactive Brokers Group, Inc.",Capital Markets,United States,Financials,US45841N1072
512 | WRB,W. R. Berkley Corporation,Insurance - Property & Casualty,United States,Financials,US0844231029
513 | TWLO,Twilio Inc.,Software - Infrastructure,United States,Technology,US90138F1021
514 | DRI,"Darden Restaurants, Inc.",Restaurants,United States,Consumer Discretionary,US2371941053
515 | RF,Regions Financial Corporation,Banks - Regional,United States,Financials,US7591EP1005
516 | WY,Weyerhaeuser Company,REIT - Specialty,United States,Real Estate,US9621661043
517 | CHKP,Check Point Software Technologies Ltd.,Software - Infrastructure,Israel,Technology,IL0010824113
518 | FOX,Fox Corporation,Entertainment,United States,Communication Services,US35137L2043
519 | ZBH,"Zimmer Biomet Holdings, Inc.",Medical Devices,United States,Healthcare,US98956P1021
520 | PINS,"Pinterest, Inc.",Internet Content & Information,United States,Communication Services,US72352L1061
521 | NTRA,"Natera, Inc.",Diagnostics & Research,United States,Healthcare,US6323071042
522 | HUBB,Hubbell Incorporated,Electrical Equipment & Parts,United States,Industrials,US4435106079
523 | IFF,International Flavors & Fragrances Inc.,Specialty Chemicals,United States,Materials,US4595061015
524 | STM,STMicroelectronics N.V.,Semiconductors,Netherlands,Technology,US8610121027
525 | EXPE,"Expedia Group, Inc.",Travel Services,United States,Consumer Discretionary,US30212P3038
526 | TU,TELUS Corporation,Telecom Services,Canada,Communication Services,CA87971M1032
527 | NTRS,Northern Trust Corporation,Asset Management,United States,Financials,US6658591044
528 | ATO,Atmos Energy Corporation,Utilities - Regulated Gas,United States,Utilities,US0495601058
529 | STE,STERIS plc,Medical Devices,United States,Healthcare,IE00BFY8C754
530 | BCE,BCE Inc.,Telecom Services,Canada,Communication Services,CA05534B7604
531 | PSTG,"Pure Storage, Inc.",Computer Hardware,United States,Technology,US74624M1027
532 | CINF,Cincinnati Financial Corporation,Insurance - Property & Casualty,United States,Financials,US1720621010
533 | WDC,Western Digital Corporation,Computer Hardware,United States,Technology,US9581021055
534 | EIX,Edison International,Utilities - Regulated Electric,United States,Utilities,US2810201077
535 | SBAC,SBA Communications Corporation,REIT - Specialty,United States,Real Estate,US78410G1040
536 | VOD,Vodafone Group Public Limited Company,Telecom Services,United Kingdom,Communication Services,US92857W3088
537 | PUK,Prudential plc,Insurance - Life,Hong Kong,Financials,US74435K2042
538 | FTS,Fortis Inc.,Utilities - Regulated Electric,Canada,Utilities,CA3495531079
539 | CBOE,"Cboe Global Markets, Inc.",Financial Data & Stock Exchanges,United States,Financials,US12503M1080
540 | ERIE,Erie Indemnity Company,Insurance Brokers,United States,Financials,US29530P1021
541 | PKG,Packaging Corporation of America,Packaging & Containers,United States,Consumer Discretionary,US6951561090
542 | STX,Seagate Technology Holdings plc,Computer Hardware,Singapore,Technology,IE00BKVD2N49
543 | BIIB,Biogen Inc.,Drug Manufacturers - General,United States,Healthcare,US09062X1037
544 | ILMN,"Illumina, Inc.",Diagnostics & Research,United States,Healthcare,US4523271090
545 | VIK,Viking Holdings Ltd,Travel Services,Bermuda,Consumer Discretionary,BMG93A5A1010
546 | CCJ,Cameco Corporation,Uranium,Canada,Energy,CA13321L1085
547 | MDB,"MongoDB, Inc.",Software - Infrastructure,United States,Technology,US60937P1066
548 | PBA,Pembina Pipeline Corporation,Oil & Gas Midstream,Canada,Energy,CA7063271034
549 | ES,Eversource Energy,Utilities - Regulated Electric,United States,Utilities,US30040W1080
550 | CNP,"CenterPoint Energy, Inc.",Utilities - Regulated Electric,United States,Utilities,US15189T1079
551 | ZBRA,Zebra Technologies Corporation,Communication Equipment,United States,Technology,US9892071054
552 | TECK,Teck Resources Limited,Other Industrial Metals & Mining,Canada,Materials,CA8787422044
553 | CFG,"Citizens Financial Group, Inc.",Banks - Regional,United States,Financials,US1746101054
554 | LH,Labcorp Holdings Inc.,Diagnostics & Research,United States,Healthcare,US50540R4092
555 | IHG,InterContinental Hotels Group PLC,Lodging,United Kingdom,Consumer Discretionary,US45857P8068
556 | MKC.V,"McCormick & Company, Incorporated",Packaged Foods,United States,Consumer Staples,
557 | MKC,"McCormick & Company, Incorporated",Packaged Foods,United States,Consumer Staples,US5797802064
558 | CTRA,Coterra Energy Inc.,Oil & Gas Exploration & Production,United States,Energy,US1270971039
559 | IP,International Paper Company,Packaging & Containers,United States,Consumer Discretionary,US4601461035
560 | BEKE,KE Holdings Inc.,Real Estate Services,China,Real Estate,US4824971042
561 | TS,Tenaris S.A.,Oil & Gas Equipment & Services,Luxembourg,Energy,US88031M1099
562 | VRSN,"VeriSign, Inc.",Software - Infrastructure,United States,Technology,US92343E1029
563 | DKNG,DraftKings Inc.,Gambling,United States,Consumer Discretionary,US26142V1052
564 | NRG,"NRG Energy, Inc.",Utilities - Independent Power Producers,United States,Utilities,US6293775085
565 | CG,The Carlyle Group Inc.,Asset Management,United States,Financials,US14316J1088
566 | DKS,"DICK'S Sporting Goods, Inc.",Specialty Retail,United States,Consumer Discretionary,US2533931026
567 | EME,"EMCOR Group, Inc.",Engineering & Construction,United States,Industrials,US29084Q1004
568 | BBD,Banco Bradesco S.A.,Banks - Regional,Brazil,Financials,US0594603039
569 | BBDO,Banco Bradesco S.A.,Banks - Regional,Brazil,Financials,US0594604029
570 | TSN,"Tyson Foods, Inc.",Farm Products,United States,Consumer Staples,US9024941034
571 | SSNC,"SS&C Technologies Holdings, Inc.",Software - Application,United States,Technology,US78467J1007
572 | ONON,On Holding AG,Footwear & Accessories,Switzerland,Consumer Discretionary,CH1134540470
573 | TER,"Teradyne, Inc.",Semiconductor Equipment & Materials,United States,Technology,US8807701029
574 | CLX,The Clorox Company,Household & Personal Products,United States,Consumer Staples,US1890541097
575 | DOCU,"DocuSign, Inc.",Software - Application,United States,Technology,US2561631068
576 | COO,"The Cooper Companies, Inc.",Medical Instruments & Supplies,United States,Healthcare,US2166485019
577 | CMS,CMS Energy Corporation,Utilities - Regulated Electric,United States,Utilities,US1258961002
578 | KEY,KeyCorp,Banks - Regional,United States,Financials,US4932671088
579 | BLDR,"Builders FirstSource, Inc.",Building Products & Equipment,United States,Industrials,US12008R1077
580 | Z,"Zillow Group, Inc.",Internet Content & Information,United States,Communication Services,US98954M2008
581 | MT,ArcelorMittal S.A.,Steel,Luxembourg,Materials,US03938L2034
582 | PODD,Insulet Corporation,Medical Devices,United States,Healthcare,US45784P1012
583 | STLD,"Steel Dynamics, Inc.",Steel,United States,Materials,US8581191009
584 | ULTA,"Ulta Beauty, Inc.",Specialty Retail,United States,Consumer Discretionary,US90384S3031
585 | TRU,TransUnion,Financial Data & Stock Exchanges,United States,Financials,US89400J1079
586 | INVH,Invitation Homes Inc.,REIT - Residential,United States,Real Estate,US46187W1071
587 | LUV,Southwest Airlines Co.,Airlines,United States,Industrials,US8447411088
588 | ZG,"Zillow Group, Inc.",Internet Content & Information,United States,Communication Services,US98954M1018
589 | PFG,"Principal Financial Group, Inc.",Asset Management,United States,Financials,US74251V1026
590 | NMR,"Nomura Holdings, Inc.",Capital Markets,Japan,Financials,US65535H2085
591 | LDOS,"Leidos Holdings, Inc.",Information Technology Services,United States,Technology,US5253271028
592 | RPRX,Royalty Pharma plc,Biotechnology,United States,Healthcare,GB00BMVP7Y09
593 | SNAP,Snap Inc.,Internet Content & Information,United States,Communication Services,US83304A1060
594 | ESS,"Essex Property Trust, Inc.",REIT - Residential,United States,Real Estate,US2971781057
595 | L,Loews Corporation,Insurance - Property & Casualty,United States,Financials,US5404241086
596 | CRBG,"Corebridge Financial, Inc.",Asset Management,United States,Financials,US21871X1090
597 | TME,Tencent Music Entertainment Group,Internet Content & Information,China,Communication Services,US88034P1093
598 | KSPI,Joint Stock Company Kaspi.kz,Software - Infrastructure,Kazakhstan,Technology,US48581R2058
599 | BBY,"Best Buy Co., Inc.",Specialty Retail,United States,Consumer Discretionary,US0865161014
600 | CYBR,CyberArk Software Ltd.,Software - Infrastructure,Israel,Technology,IL0011334468
601 | SNA,Snap-on Incorporated,Tools & Accessories,United States,Industrials,US8330341012
602 | TRMB,Trimble Inc.,Scientific & Technical Instruments,United States,Technology,US8962391004
603 | GRAB,Grab Holdings Limited,Software - Application,Singapore,Technology,KYG4124C1096
604 | WSO,"Watsco, Inc.",Industrial Distribution,United States,Industrials,US9426222009
605 | BURL,"Burlington Stores, Inc.",Apparel Retail,United States,Consumer Discretionary,US1220171060
606 | NTNX,"Nutanix, Inc.",Software - Infrastructure,United States,Technology,US67059N1081
607 | WSO.B,"Watsco, Inc.",Industrial Distribution,United States,Industrials,US9426221019
608 | MAA,"Mid-America Apartment Communities, Inc.",REIT - Residential,United States,Real Estate,US59522J1034
609 | AFRM,"Affirm Holdings, Inc.",Software - Infrastructure,United States,Technology,US00827B1061
610 | MANH,"Manhattan Associates, Inc.",Software - Application,United States,Technology,US5627501092
611 | FDS,FactSet Research Systems Inc.,Financial Data & Stock Exchanges,United States,Financials,US3030751057
612 | CSL,Carlisle Companies Incorporated,Building Products & Equipment,United States,Industrials,US1423391002
613 | EC,Ecopetrol S.A.,Oil & Gas Integrated,Colombia,Energy,US2791581091
614 | JBL,Jabil Inc.,Electronic Components,United States,Technology,US4663131039
615 | SOFI,"SoFi Technologies, Inc.",Credit Services,United States,Financials,US83406F1021
616 | SHG,"Shinhan Financial Group Co., Ltd.",Banks - Regional,South Korea,Financials,US8245961003
617 | AER,AerCap Holdings N.V.,Rental & Leasing Services,Ireland,Industrials,NL0000687663
618 | MOH,"Molina Healthcare, Inc.",Healthcare Plans,United States,Healthcare,US60855R1005
619 | DGX,Quest Diagnostics Incorporated,Diagnostics & Research,United States,Healthcare,US74834L1008
620 | AS,"Amer Sports, Inc.",Leisure,Finland,Consumer Discretionary,FI0009000285
621 | SYM,Symbotic Inc.,Specialty Industrial Machinery,United States,Industrials,US87151X1019
622 | JBHT,"J.B. Hunt Transport Services, Inc.",Integrated Freight & Logistics,United States,Industrials,US4456581077
623 | MAS,Masco Corporation,Building Products & Equipment,United States,Industrials,US5745991068
624 | SMMT,Summit Therapeutics Inc.,Biotechnology,United States,Healthcare,US86627T1088
625 | GWRE,"Guidewire Software, Inc.",Software - Application,United States,Technology,US40171V1008
626 | AZPN,"Aspen Technology, Inc.",Software - Application,United States,Technology,US29109X1063
627 | DT,"Dynatrace, Inc.",Software - Application,United States,Technology,US2681501092
628 | MRNA,"Moderna, Inc.",Biotechnology,United States,Healthcare,US60770K1079
629 | YUMC,"Yum China Holdings, Inc.",Restaurants,China,Consumer Discretionary,US98850P1093
630 | FSLR,"First Solar, Inc.",Solar,United States,Technology,US3364331070
631 | RYAN,"Ryan Specialty Holdings, Inc.",Insurance - Specialty,United States,Financials,US78351F1075
632 | GEN,Gen Digital Inc.,Software - Infrastructure,United States,Technology,US6687711084
633 | OMC,Omnicom Group Inc.,Advertising Agencies,United States,Communication Services,US6819191064
634 | YPF,YPF Sociedad Anónima,Oil & Gas Integrated,Argentina,Energy,US9842451000
635 | J,Jacobs Solutions Inc.,Engineering & Construction,United States,Industrials,US46982L1089
636 | NI,NiSource Inc.,Utilities - Regulated Gas,United States,Utilities,US65473P1057
637 | PNR,Pentair plc,Specialty Industrial Machinery,United Kingdom,Industrials,IE00BLS09M33
638 | GFL,GFL Environmental Inc.,Waste Management,Canada,Industrials,CA36168Q1046
639 | TPR,"Tapestry, Inc.",Luxury Goods,United States,Consumer Discretionary,US8760301072
640 | ALGN,"Align Technology, Inc.",Medical Instruments & Supplies,United States,Healthcare,US0162551016
641 | ARE,"Alexandria Real Estate Equities, Inc.",REIT - Office,United States,Real Estate,US0152711091
642 | EQH,"Equitable Holdings, Inc.",Insurance - Diversified,United States,Financials,US29452E1010
643 | IEX,IDEX Corporation,Specialty Industrial Machinery,United States,Industrials,US45167R1041
644 | HRL,Hormel Foods Corporation,Packaged Foods,United States,Consumer Staples,US4404521001
645 | ICLR,ICON Public Limited Company,Diagnostics & Research,Ireland,Healthcare,IE0005711209
646 | BAX,Baxter International Inc.,Medical Instruments & Supplies,United States,Healthcare,US0718131099
647 | RBA,"RB Global, Inc.",Specialty Business Services,United States,Industrials,CA74935Q1072
648 | NWS,News Corporation,Entertainment,United States,Communication Services,US65249B2088
649 | BALL,Ball Corporation,Packaging & Containers,United States,Consumer Discretionary,US0584981064
650 | SUI,"Sun Communities, Inc.",REIT - Residential,United States,Real Estate,US8666741041
651 | UTHR,United Therapeutics Corporation,Biotechnology,United States,Healthcare,US91307C1027
652 | USFD,US Foods Holding Corp.,Food Distribution,United States,Consumer Staples,US9120081099
653 | SMCI,"Super Micro Computer, Inc.",Computer Hardware,United States,Technology,US86800U1043
654 | TLK,Perusahaan Perseroan (Persero) PT Telekomunikasi Indonesia Tbk,Telecom Services,Indonesia,Communication Services,US7156841063
655 | BAH,Booz Allen Hamilton Holding Corporation,Consulting Services,United States,Industrials,US0995021062
656 | CNH,CNH Industrial N.V.,Farm & Heavy Construction Machinery,United Kingdom,Industrials,NL0010545661
657 | WMG,Warner Music Group Corp.,Entertainment,United States,Communication Services,US9345502036
658 | OC,Owens Corning,Building Products & Equipment,United States,Industrials,US6907421019
659 | RPM,RPM International Inc.,Specialty Chemicals,United States,Materials,US7496851038
660 | GPC,Genuine Parts Company,Auto Parts,United States,Consumer Discretionary,US3724601055
661 | XPO,"XPO, Inc.",Trucking,United States,Industrials,US9837931008
662 | KOF,"Coca-Cola FEMSA, S.A.B. de C.V.",Beverages - Non-Alcoholic,Mexico,Consumer Staples,US1912411089
663 | OKTA,"Okta, Inc.",Software - Infrastructure,United States,Technology,US6792951054
664 | HOLX,"Hologic, Inc.",Medical Instruments & Supplies,United States,Healthcare,US4364401012
665 | DLTR,"Dollar Tree, Inc.",Discount Stores,United States,Consumer Staples,US2567461080
666 | DG,Dollar General Corporation,Discount Stores,United States,Consumer Staples,US2566771059
667 | RL,Ralph Lauren Corporation,Apparel Manufacturing,United States,Consumer Discretionary,US7512121010
668 | EXPD,"Expeditors International of Washington, Inc.",Integrated Freight & Logistics,United States,Industrials,US3021301094
669 | NWSA,News Corporation,Entertainment,United States,Communication Services,US65249B1098
670 | BSBR,Banco Santander (Brasil) S.A.,Banks - Regional,Brazil,Financials,US05967A1079
671 | WES,"Western Midstream Partners, LP",Oil & Gas Midstream,United States,Energy,US9586691035
672 | RCI,Rogers Communications Inc.,Telecom Services,Canada,Communication Services,CA7751092007
673 | CHWY,"Chewy, Inc.",Internet Retail,United States,Consumer Discretionary,US16679L1098
674 | FNF,"Fidelity National Financial, Inc.",Insurance - Specialty,United States,Financials,US31620R3030
675 | RS,"Reliance, Inc.",Steel,United States,Materials,US7595091023
676 | EG,"Everest Group, Ltd.",Insurance - Reinsurance,Bermuda,Financials,BMG3223R1088
677 | FLEX,Flex Ltd.,Electronic Components,United States,Technology,SG9999000020
678 | CF,"CF Industries Holdings, Inc.",Agricultural Inputs,United States,Materials,US1252691001
679 | SN,"SharkNinja, Inc.","Furnishings, Fixtures & Appliances",United States,Consumer Discretionary,KYG8068L1086
680 | JEF,Jefferies Financial Group Inc.,Capital Markets,United States,Financials,US47233W1099
681 | FFIV,"F5, Inc.",Software - Infrastructure,United States,Technology,US3156161024
682 | BF.B,Brown-Forman Corporation,Beverages - Wineries & Distilleries,United States,Consumer Staples,US1156372096
683 | BF.A,Brown-Forman Corporation,Beverages - Wineries & Distilleries,United States,Consumer Staples,US1156371007
684 | AVY,Avery Dennison Corporation,Packaging & Containers,United States,Consumer Discretionary,US0536111091
685 | KIM,Kimco Realty Corporation,REIT - Retail,United States,Real Estate,US49446R1095
686 | CASY,"Casey's General Stores, Inc.",Specialty Retail,United States,Consumer Discretionary,US1475281036
687 | DUOL,"Duolingo, Inc.",Software - Application,United States,Technology,US26603R1068
688 | UMC,United Microelectronics Corporation,Semiconductors,Taiwan,Technology,US9108734057
689 | UDR,"UDR, Inc.",REIT - Residential,United States,Real Estate,US9026531049
690 | RVTY,"Revvity, Inc.",Diagnostics & Research,United States,Healthcare,US7140461093
691 | AVTR,"Avantor, Inc.",Medical Instruments & Supplies,United States,Healthcare,US05352A1007
692 | NBIX,"Neurocrine Biosciences, Inc.",Drug Manufacturers - Specialty & Generic,United States,Healthcare,US64125C1099
693 | BIP,Brookfield Infrastructure Partners L.P.,Utilities - Diversified,Bermuda,Utilities,BMG162521014
694 | SFM,"Sprouts Farmers Market, Inc.",Grocery Stores,United States,Consumer Staples,US85208M1027
695 | ARCC,Ares Capital Corporation,Asset Management,United States,Financials,US04010L1035
696 | H,Hyatt Hotels Corporation,Lodging,United States,Consumer Discretionary,US4485791028
697 | ZTO,ZTO Express (Cayman) Inc.,Integrated Freight & Logistics,China,Industrials,US98980A1051
698 | RGA,"Reinsurance Group of America, Incorporated",Insurance - Reinsurance,United States,Financials,US7593516047
699 | LNT,Alliant Energy Corporation,Utilities - Regulated Electric,United States,Utilities,US0188021085
700 | AKAM,"Akamai Technologies, Inc.",Software - Infrastructure,United States,Technology,US00971T1016
701 | LINE,"Lineage, Inc.",REIT - Industrial,United States,Real Estate,US53566V1061
702 | WLK,Westlake Corporation,Specialty Chemicals,United States,Materials,US9604131022
703 | DPZ,"Domino's Pizza, Inc.",Restaurants,United States,Consumer Discretionary,US25754A2015
704 | AMH,American Homes 4 Rent,REIT - Residential,United States,Real Estate,US02665T3068
705 | FIX,"Comfort Systems USA, Inc.",Engineering & Construction,United States,Industrials,US1999081045
706 | APTV,Aptiv PLC,Auto Parts,Switzerland,Consumer Discretionary,JE00B783TY65
707 | DOC,"Healthpeak Properties, Inc.",REIT - Healthcare Facilities,United States,Real Estate,US71943U1043
708 | ENTG,"Entegris, Inc.",Semiconductor Equipment & Materials,United States,Technology,US29362U1043
709 | BSY,"Bentley Systems, Incorporated",Software - Application,United States,Technology,US08265T2087
710 | BSS,"Bentley Systems, Incorporated",,,,
711 | EDR,"Endeavor Group Holdings, Inc.",Entertainment,United States,Communication Services,US29260Y1091
712 | GFI,Gold Fields Limited,Gold,South Africa,Materials,US38059T1060
713 | EVRG,"Evergy, Inc.",Utilities - Regulated Electric,United States,Utilities,US30034W1062
714 | RKLB,"Rocket Lab USA, Inc.",Aerospace & Defense,United States,Industrials,US7731221062
715 | EPAM,"EPAM Systems, Inc.",Information Technology Services,United States,Technology,US29414B1044
716 | PAA,"Plains All American Pipeline, L.P.",Oil & Gas Midstream,United States,Energy,US7265031051
717 | CAVA,"CAVA Group, Inc.",Restaurants,United States,Consumer Discretionary,US1489291021
718 | JHX,James Hardie Industries plc,Building Materials,Ireland,Materials,US47030M1062
719 | BAP,Credicorp Ltd.,Banks - Regional,Peru,Financials,BMG2519Y1084
720 | FMS,Fresenius Medical Care AG,Medical Care Facilities,Germany,Healthcare,US3580291066
721 | SWKS,"Skyworks Solutions, Inc.",Semiconductors,United States,Technology,US83088M1027
722 | XPEV,XPeng Inc.,Auto Manufacturers,China,Consumer Discretionary,US98422D1054
723 | VIV,Telefônica Brasil S.A.,Telecom Services,Brazil,Communication Services,US87936R2058
724 | UHAL,U-Haul Holding Company,Rental & Leasing Services,United States,Industrials,US0235861004
725 | EWBC,"East West Bancorp, Inc.",Banks - Regional,United States,Financials,US27579R1041
726 | TXT,Textron Inc.,Aerospace & Defense,United States,Industrials,US8832031012
727 | ALAB,"Astera Labs, Inc.",Semiconductors,United States,Technology,US04626A1034
728 | DVA,DaVita Inc.,Medical Care Facilities,United States,Healthcare,US23918K1088
729 | AU,AngloGold Ashanti plc,Gold,United States,Materials,US0351282068
730 | MORN,"Morningstar, Inc.",Financial Data & Stock Exchanges,United States,Financials,US6177001095
731 | AMCR,Amcor plc,Packaging & Containers,Switzerland,Consumer Discretionary,JE00BJ1F3079
732 | GGG,Graco Inc.,Specialty Industrial Machinery,United States,Industrials,US3841091040
733 | INCY,Incyte Corporation,Biotechnology,United States,Healthcare,US45337C1027
734 | INSM,Insmed Incorporated,Biotechnology,United States,Healthcare,US4576693075
735 | PFGC,Performance Food Group Company,Food Distribution,United States,Consumer Staples,US71377A1034
736 | ACM,AECOM,Engineering & Construction,United States,Industrials,US00766T1007
737 | EBR,Centrais Elétricas Brasileiras S.A. - Eletrobrás,Utilities - Renewable,Brazil,Utilities,US15234Q2075
738 | UNM,Unum Group,Insurance - Life,United States,Financials,US91529Y1064
739 | GLPI,"Gaming and Leisure Properties, Inc.",REIT - Specialty,United States,Real Estate,US36467J1088
740 | WIX,Wix.com Ltd.,Software - Infrastructure,Israel,Technology,IL0011301780
741 | PKX,POSCO Holdings Inc.,Steel,South Korea,Materials,US6934831099
742 | TOL,"Toll Brothers, Inc.",Residential Construction,United States,Consumer Discretionary,US8894781033
743 | FUTU,Futu Holdings Limited,Capital Markets,Hong Kong,Financials,US36118L1061
744 | SWK,"Stanley Black & Decker, Inc.",Tools & Accessories,United States,Industrials,US8545021011
745 | RBRK,"Rubrik, Inc.",Software - Infrastructure,United States,Technology,US7811541090
746 | MBLY,Mobileye Global Inc.,Auto Parts,Israel,Consumer Discretionary,US60741F1049
747 | LOGI,Logitech International S.A.,Computer Hardware,Switzerland,Technology,CH0025751329
748 | ITCI,"Intra-Cellular Therapies, Inc.",Drug Manufacturers - Specialty & Generic,United States,Healthcare,US46116X1019
749 | CNA,CNA Financial Corporation,Insurance - Property & Casualty,United States,Financials,US1261171003
750 | VTRS,Viatris Inc.,Drug Manufacturers - Specialty & Generic,United States,Healthcare,US92556V1061
751 | KGC,Kinross Gold Corporation,Gold,Canada,Materials,CA4969024047
752 | JLL,Jones Lang LaSalle Incorporated,Real Estate Services,United States,Real Estate,US48020Q1076
753 | ELS,"Equity LifeStyle Properties, Inc.",REIT - Residential,United States,Real Estate,US29472R1086
754 | POOL,Pool Corporation,Industrial Distribution,United States,Industrials,US73278L1052
755 | THC,Tenet Healthcare Corporation,Medical Care Facilities,United States,Healthcare,US88033G4073
756 | SUZ,Suzano S.A.,Paper & Paper Products,Brazil,Materials,US86959K1051
757 | REG,Regency Centers Corporation,REIT - Retail,United States,Real Estate,US7588491032
758 | MNDY,monday.com Ltd.,Software - Application,Israel,Technology,IL0011762130
759 | ESLT,Elbit Systems Ltd.,Aerospace & Defense,Israel,Industrials,IL0010811243
760 | SAIA,"Saia, Inc.",Trucking,United States,Industrials,US78709Y1055
761 | KMX,"CarMax, Inc.",Auto & Truck Dealerships,United States,Consumer Discretionary,US1431301027
762 | FTI,TechnipFMC plc,Oil & Gas Equipment & Services,United States,Energy,GB00BDSFG982
763 | BJ,"BJ's Wholesale Club Holdings, Inc.",Discount Stores,United States,Consumer Staples,US05550J1016
764 | RNR,RenaissanceRe Holdings Ltd.,Insurance - Reinsurance,Bermuda,Financials,BMG7496G1033
765 | CHRW,"C.H. Robinson Worldwide, Inc.",Integrated Freight & Logistics,United States,Industrials,US12541W2098
766 | RIVN,"Rivian Automotive, Inc.",Auto Manufacturers,United States,Consumer Discretionary,US76954A1034
767 | UHAL.B,U-Haul Holding Company,Rental & Leasing Services,United States,Industrials,US0235865062
768 | LAMR,Lamar Advertising Company,REIT - Specialty,United States,Real Estate,US5128161099
769 | SOLV,Solventum Corporation,Health Information Services,United States,Healthcare,US83444M1018
770 | HLI,"Houlihan Lokey, Inc.",Capital Markets,United States,Financials,US4415931009
771 | BXP,"BXP, Inc.",REIT - Office,United States,Real Estate,US1011211018
772 | CW,Curtiss-Wright Corporation,Aerospace & Defense,United States,Industrials,US2315611010
773 | JKHY,"Jack Henry & Associates, Inc.",Information Technology Services,United States,Technology,US4262811015
774 | COHR,Coherent Corp.,Scientific & Technical Instruments,United States,Technology,US19247G1076
775 | CLH,"Clean Harbors, Inc.",Waste Management,United States,Industrials,US1844961078
776 | GMED,"Globus Medical, Inc.",Medical Devices,United States,Healthcare,US3795772082
777 | NDSN,Nordson Corporation,Specialty Industrial Machinery,United States,Industrials,US6556631025
778 | NCLH,Norwegian Cruise Line Holdings Ltd.,Travel Services,United States,Consumer Discretionary,BMG667211046
779 | PRMB,Primo Brands Corporation,Beverages - Non-Alcoholic,United States,Consumer Staples,US7416231022
780 | UHS,"Universal Health Services, Inc.",Medical Care Facilities,United States,Healthcare,US9139031002
781 | KVYO,"Klaviyo, Inc.",Software - Infrastructure,United States,Technology,US49845K1016
782 | GME,GameStop Corp.,Specialty Retail,United States,Consumer Discretionary,US36467W1099
783 | BCH,Banco de Chile,Banks - Regional,Chile,Financials,US0595201064
784 | CAG,"Conagra Brands, Inc.",Packaged Foods,United States,Consumer Staples,US2058871029
785 | CPT,Camden Property Trust,REIT - Residential,United States,Real Estate,US1331311027
786 | WPC,W. P. Carey Inc.,REIT - Diversified,United States,Real Estate,US92936U1097
787 | RTO,Rentokil Initial plc,Specialty Business Services,United Kingdom,Industrials,US7601251041
788 | PCOR,"Procore Technologies, Inc.",Software - Application,United States,Technology,US74275K1088
789 | ESTC,Elastic N.V.,Software - Application,Netherlands,Technology,NL0013056914
790 | GMAB,Genmab A/S,Biotechnology,Denmark,Healthcare,US3723032062
791 | TXRH,"Texas Roadhouse, Inc.",Restaurants,United States,Consumer Discretionary,US8826811098
792 | BMRN,BioMarin Pharmaceutical Inc.,Biotechnology,United States,Healthcare,US09061G1013
793 | JNPR,"Juniper Networks, Inc.",Communication Equipment,United States,Technology,US48203R1041
794 | CART,Maplebear Inc.,Internet Retail,United States,Consumer Discretionary,US5653941030
795 | SNX,TD SYNNEX Corporation,Electronics & Computer Distribution,United States,Technology,US87162W1009
796 | YMM,Full Truck Alliance Co. Ltd.,Software - Application,China,Technology,US35969L1089
797 | ROKU,"Roku, Inc.",Entertainment,United States,Communication Services,US77543R1023
798 | PR,Permian Resources Corporation,Oil & Gas Exploration & Production,United States,Energy,US71424F1057
799 | PAYC,"Paycom Software, Inc.",Software - Application,United States,Technology,US70432V1026
800 | ITT,ITT Inc.,Specialty Industrial Machinery,United States,Industrials,US45073V1089
801 | ALLY,Ally Financial Inc.,Credit Services,United States,Financials,US02005N1000
802 | HST,"Host Hotels & Resorts, Inc.",REIT - Hotel & Motel,United States,Real Estate,US44107P1049
803 | TECH,Bio-Techne Corporation,Biotechnology,United States,Healthcare,US09073M1045
804 | MGA,Magna International Inc.,Auto Parts,Canada,Consumer Discretionary,CA5592224011
805 | GTLB,GitLab Inc.,Software - Infrastructure,United States,Technology,US37637K1088
806 | SF,Stifel Financial Corp.,Capital Markets,United States,Financials,US8606301021
807 | GGAL,Grupo Financiero Galicia S.A.,Banks - Regional,Argentina,Financials,US3999091008
808 | MMYT,MakeMyTrip Limited,Travel Services,India,Consumer Discretionary,MU0295S00016
809 | CPB,The Campbell's Company,Packaged Foods,United States,Consumer Staples,US1344291091
810 | COKE,"Coca-Cola Consolidated, Inc.",Beverages - Non-Alcoholic,United States,Consumer Staples,US1910981026
811 | SCI,Service Corporation International,Personal Services,United States,Consumer Discretionary,US8175651046
812 | PCTY,Paylocity Holding Corporation,Software - Application,United States,Technology,US70438V1061
813 | TFII,TFI International Inc.,Trucking,Canada,Industrials,CA87241L1094
814 | DAY,Dayforce Inc.,Software - Application,United States,Technology,US15677J1088
815 | AUR,"Aurora Innovation, Inc.",Information Technology Services,United States,Technology,US0517741072
816 | SKX,"Skechers U.S.A., Inc.",Footwear & Accessories,United States,Consumer Discretionary,US8305661055
817 | EVR,Evercore Inc.,Capital Markets,United States,Financials,US29977A1051
818 | AR,Antero Resources Corporation,Oil & Gas Exploration & Production,United States,Energy,US03674X1063
819 | LBRDK,Liberty Broadband Corporation,Telecom Services,United States,Communication Services,US5303073051
820 | LBRDA,Liberty Broadband Corporation,Telecom Services,United States,Communication Services,US5303071071
821 | AFG,"American Financial Group, Inc.",Insurance - Property & Casualty,United States,Financials,US0259321042
822 | ACI,"Albertsons Companies, Inc.",Grocery Stores,United States,Consumer Staples,US0130911037
823 | ALLE,Allegion plc,Security & Protection Services,Ireland,Industrials,IE00BFRT3W74
824 | PCVX,"Vaxcyte, Inc.",Biotechnology,United States,Healthcare,US92243G1085
825 | BIRK,Birkenstock Holding plc,Footwear & Accessories,United Kingdom,Consumer Discretionary,JE00BS44BN30
826 | OVV,Ovintiv Inc.,Oil & Gas Exploration & Production,United States,Energy,US69047Q1022
827 | CIEN,Ciena Corporation,Communication Equipment,United States,Technology,US1717793095
828 | RDY,Dr. Reddy's Laboratories Limited,Drug Manufacturers - Specialty & Generic,India,Healthcare,US2561352038
829 | TAP.A,Molson Coors Beverage Company,Beverages - Brewers,United States,Consumer Staples,US60871R1005
830 | TAP,Molson Coors Beverage Company,Beverages - Brewers,United States,Consumer Staples,US60871R2094
831 | AAL,American Airlines Group Inc.,Airlines,United States,Industrials,US02376R1023
832 | CNM,"Core & Main, Inc.",Industrial Distribution,United States,Industrials,US21874C1027
833 | SRPT,"Sarepta Therapeutics, Inc.",Biotechnology,United States,Healthcare,US8036071004
834 | SJM,The J. M. Smucker Company,Packaged Foods,United States,Consumer Staples,US8326964058
835 | FHN,First Horizon Corporation,Banks - Regional,United States,Financials,US3205171057
836 | NLY,"Annaly Capital Management, Inc.",REIT - Mortgage,United States,Real Estate,US0357108390
837 | FND,"Floor & Decor Holdings, Inc.",Home Improvement Retail,United States,Consumer Discretionary,US3397501012
838 | SQM,Sociedad Química y Minera de Chile S.A.,Specialty Chemicals,Chile,Materials,US8336351056
839 | SNN,Smith & Nephew plc,Medical Devices,United Kingdom,Healthcare,US83175M2052
840 | LECO,"Lincoln Electric Holdings, Inc.",Tools & Accessories,United States,Industrials,US5339001068
841 | AIZ,"Assurant, Inc.",Insurance - Property & Casualty,United States,Financials,US04621X1081
842 | PAG,"Penske Automotive Group, Inc.",Auto & Truck Dealerships,United States,Consumer Discretionary,US70959W1036
843 | SBS,Companhia de Saneamento Básico do Estado de São Paulo - SABESP,Utilities - Regulated Water,Brazil,Utilities,US20441A1025
844 | CLS,Celestica Inc.,Electronic Components,Canada,Technology,CA15101Q1081
845 | WWD,"Woodward, Inc.",Aerospace & Defense,United States,Industrials,US9807451037
846 | PPC,Pilgrim's Pride Corporation,Packaged Foods,United States,Consumer Staples,US72147K1088
847 | SSB,SouthState Corporation,Banks - Regional,United States,Financials,US8404411097
848 | SEIC,SEI Investments Company,Asset Management,United States,Financials,US7841171033
849 | BG,Bunge Global SA,Farm Products,United States,Consumer Staples,CH1300646267
850 | ULS,UL Solutions Inc.,Specialty Business Services,United States,Industrials,US9037311076
851 | IPG,"The Interpublic Group of Companies, Inc.",Advertising Agencies,United States,Communication Services,US4606901001
852 | EMN,Eastman Chemical Company,Specialty Chemicals,United States,Materials,US2774321002
853 | PSO,Pearson plc,Publishing,United Kingdom,Communication Services,US7050151056
854 | MEDP,"Medpace Holdings, Inc.",Diagnostics & Research,United States,Healthcare,US58506Q1094
855 | DOCS,"Doximity, Inc.",Health Information Services,United States,Healthcare,US26622P1075
856 | NICE,NICE Ltd.,Software - Application,Israel,Technology,US6536561086
857 | RRX,Regal Rexnord Corporation,Specialty Industrial Machinery,United States,Industrials,US7587501039
858 | BEN,"Franklin Resources, Inc.",Asset Management,United States,Financials,US3546131018
859 | FOUR,"Shift4 Payments, Inc.",Software - Infrastructure,United States,Technology,US82452J1097
860 | BROS,Dutch Bros Inc.,Restaurants,United States,Consumer Discretionary,US26701L1008
861 | ATR,"AptarGroup, Inc.",Medical Instruments & Supplies,United States,Healthcare,US0383361039
862 | TPX,"Tempur Sealy International, Inc.","Furnishings, Fixtures & Appliances",United States,Consumer Discretionary,US88023U1016
863 | MTZ,"MasTec, Inc.",Engineering & Construction,United States,Industrials,US5763231090
864 | CCK,"Crown Holdings, Inc.",Packaging & Containers,United States,Consumer Discretionary,US2283681060
865 | AEG,Aegon Ltd.,Insurance - Diversified,Netherlands,Financials,US0076CA1045
866 | OHI,"Omega Healthcare Investors, Inc.",REIT - Healthcare Facilities,United States,Real Estate,US6819361006
867 | ARMK,Aramark,Specialty Business Services,United States,Industrials,US03852U1060
868 | NVT,nVent Electric plc,Electrical Equipment & Parts,United Kingdom,Industrials,IE00BDVJJQ56
869 | BNT,Brookfield Wealth Solutions Ltd.,Insurance - Diversified,Bermuda,Financials,BMG174341047
870 | PEN,"Penumbra, Inc.",Medical Devices,United States,Healthcare,US70975L1070
871 | TTEK,"Tetra Tech, Inc.",Engineering & Construction,United States,Industrials,US88162G1031
872 | VFC,V.F. Corporation,Apparel Manufacturing,United States,Consumer Discretionary,US9182041080
873 | HTHT,H World Group Limited,Lodging,China,Consumer Discretionary,US44332N1063
874 | MRNO,Murano Global Investments Plc,Real Estate - Development,United Kingdom,Real Estate,JE00BQ7X4L23
875 | KNSL,"Kinsale Capital Group, Inc.",Insurance - Property & Casualty,United States,Financials,US49714P1084
876 | APG,APi Group Corporation,Engineering & Construction,United States,Industrials,US00187Y1001
877 | CRS,Carpenter Technology Corporation,Metal Fabrication,United States,Industrials,US1442851036
878 | BIO,"Bio-Rad Laboratories, Inc.",Medical Devices,United States,Healthcare,US0905722072
879 | FTAI,FTAI Aviation Ltd.,Rental & Leasing Services,United States,Industrials,KYG3730V1059
880 | EXAS,Exact Sciences Corporation,Diagnostics & Research,United States,Healthcare,US30063P1057
881 | BWXT,"BWX Technologies, Inc.",Aerospace & Defense,United States,Industrials,US05605H1005
882 | BIO.B,"Bio-Rad Laboratories, Inc.",Medical Devices,United States,Healthcare,US0905721082
883 | CFLT,"Confluent, Inc.",Software - Infrastructure,United States,Technology,US20717M1036
884 | GL,Globe Life Inc.,Insurance - Life,United States,Financials,US37959E1029
885 | WBS,Webster Financial Corporation,Banks - Regional,United States,Financials,US9478901096
886 | AOS,A. O. Smith Corporation,Specialty Industrial Machinery,United States,Industrials,US8318652091
887 | DBX,"Dropbox, Inc.",Software - Infrastructure,United States,Technology,US26210C1045
888 | ALB,Albemarle Corporation,Specialty Chemicals,United States,Materials,US0126531013
889 | WPP,WPP plc,Advertising Agencies,United Kingdom,Communication Services,US92937A1025
890 | BRBR,"BellRing Brands, Inc.",Packaged Foods,United States,Consumer Staples,US07831C1036
891 | DSGX,The Descartes Systems Group Inc.,Software - Application,Canada,Technology,CA2499061083
892 | CR,Crane Company,Specialty Industrial Machinery,United States,Industrials,US2244081046
893 | GLBE,Global-E Online Ltd.,Internet Retail,Israel,Consumer Discretionary,IL0011741688
894 | BILL,"BILL Holdings, Inc.",Software - Application,United States,Technology,US0900431000
895 | AYI,"Acuity Brands, Inc.",Electrical Equipment & Parts,United States,Industrials,US00508Y1029
896 | UWMC,UWM Holdings Corporation,Mortgage Finance,United States,Financials,US91823B1098
897 | DTM,"DT Midstream, Inc.",Oil & Gas Midstream,United States,Energy,US23345M1071
898 | MUSA,Murphy USA Inc.,Specialty Retail,United States,Consumer Discretionary,US6267551025
899 | BLD,TopBuild Corp.,Engineering & Construction,United States,Industrials,US89055F1030
900 | ALSN,"Allison Transmission Holdings, Inc.",Auto Parts,United States,Consumer Discretionary,US01973R1014
901 | KNTK,Kinetik Holdings Inc.,Oil & Gas Midstream,United States,Energy,US02215L2097
902 | MGM,MGM Resorts International,Resorts & Casinos,United States,Consumer Discretionary,US5529531015
903 | LKQ,LKQ Corporation,Auto Parts,United States,Consumer Discretionary,US5018892084
904 | RBC,RBC Bearings Incorporated,Tools & Accessories,United States,Industrials,US75524B1044
905 | PNW,Pinnacle West Capital Corporation,Utilities - Regulated Electric,United States,Utilities,US7234841010
906 | WTRG,"Essential Utilities, Inc.",Utilities - Regulated Water,United States,Utilities,US29670G1022
907 | LAD,"Lithia Motors, Inc.",Auto & Truck Dealerships,United States,Consumer Discretionary,US5367971034
908 | DOX,Amdocs Limited,Software - Infrastructure,United States,Technology,GB0022569080
909 | RGEN,Repligen Corporation,Medical Instruments & Supplies,United States,Healthcare,US7599161095
910 | QGEN,Qiagen N.V.,Diagnostics & Research,Netherlands,Healthcare,NL0015001WM6
911 | EHC,Encompass Health Corporation,Medical Care Facilities,United States,Healthcare,US29261A1007
912 | WAL,Western Alliance Bancorporation,Banks - Regional,United States,Financials,US9576381092
913 | CRDO,Credo Technology Group Holding Ltd,Semiconductors,Cayman Islands,Technology,KYG254571055
914 | BEP,Brookfield Renewable Partners L.P.,Utilities - Renewable,Canada,Utilities,BMG162581083
915 | AIT,"Applied Industrial Technologies, Inc.",Industrial Distribution,United States,Industrials,US03820C1053
916 | PRI,"Primerica, Inc.",Insurance - Life,United States,Financials,US74164M1080
917 | WMS,"Advanced Drainage Systems, Inc.",Building Products & Equipment,United States,Industrials,US00790R1041
918 | PEGA,Pegasystems Inc.,Software - Application,United States,Technology,US7055731035
919 | CUBE,CubeSmart,REIT - Industrial,United States,Real Estate,US2296631094
920 | PNFP,"Pinnacle Financial Partners, Inc.",Banks - Regional,United States,Financials,US72346Q1040
921 | CIB,Bancolombia S.A.,Banks - Regional,Colombia,Financials,US05968L1026
922 | HSIC,"Henry Schein, Inc.",Medical Distribution,United States,Healthcare,US8064071025
923 | REXR,"Rexford Industrial Realty, Inc.",REIT - Industrial,United States,Real Estate,US76169C1009
924 | KNX,Knight-Swift Transportation Holdings Inc.,Trucking,United States,Industrials,US4990491049
925 | DRS,"Leonardo DRS, Inc.",Aerospace & Defense,United States,Industrials,US52661A1088
926 | KEP,Korea Electric Power Corporation,Utilities - Regulated Electric,South Korea,Utilities,US5006311063
927 | PAC,"Grupo Aeroportuario del Pacífico, S.A.B. de C.V.",Airports & Air Services,Mexico,Industrials,US4005061019
928 | WBA,"Walgreens Boots Alliance, Inc.",Pharmaceutical Retailers,United States,Healthcare,US9314271084
929 | ALTR,Altair Engineering Inc.,Software - Application,United States,Technology,US0213691035
930 | TLN,Talen Energy Corporation,Utilities - Independent Power Producers,United States,Utilities,US87422Q1094
931 | MASI,Masimo Corporation,Medical Devices,United States,Healthcare,US5747951003
932 | U,Unity Software Inc.,Software - Application,United States,Technology,US91332U1016
933 | HQY,"HealthEquity, Inc.",Health Information Services,United States,Healthcare,US42226A1079
934 | GAP,"The Gap, Inc.",Apparel Retail,United States,Consumer Discretionary,US3647601083
935 | BSAC,Banco Santander-Chile,Banks - Regional,Chile,Financials,US05965X1090
936 | EXEL,"Exelixis, Inc.",Biotechnology,United States,Healthcare,US30161Q1040
937 | APPF,"AppFolio, Inc.",Software - Application,United States,Technology,US03783C1009
938 | FRT,Federal Realty Investment Trust,REIT - Retail,United States,Real Estate,US3137451015
939 | MIDD,The Middleby Corporation,Specialty Industrial Machinery,United States,Industrials,US5962781010
940 | CHDN,Churchill Downs Incorporated,Gambling,United States,Consumer Discretionary,US1714841087
941 | TTAN,"ServiceTitan, Inc.",Software - Application,United States,Technology,US81764X1037
942 | ORI,Old Republic International Corporation,Insurance - Property & Casualty,United States,Financials,US6802231042
943 | VFS,VinFast Auto Ltd.,Auto Manufacturers,Vietnam,Consumer Discretionary,SGXZ55111462
944 | MTSI,"MACOM Technology Solutions Holdings, Inc.",Semiconductors,United States,Technology,US55405Y1001
945 | VERX,"Vertex, Inc.",Software - Application,United States,Technology,US92538J1060
946 | SUM,"Summit Materials, Inc.",Building Materials,United States,Materials,US86614U1007
947 | WYNN,"Wynn Resorts, Limited",Resorts & Casinos,United States,Consumer Discretionary,US9831341071
948 | RGLD,"Royal Gold, Inc.",Gold,United States,Materials,US7802871084
949 | MLI,"Mueller Industries, Inc.",Metal Fabrication,United States,Industrials,US6247561029
950 | AAON,"AAON, Inc.",Building Products & Equipment,United States,Industrials,US0003602069
951 | NIO,NIO Inc.,Auto Manufacturers,China,Consumer Discretionary,US62914V1061
952 | ONTO,Onto Innovation Inc.,Semiconductor Equipment & Materials,United States,Technology,US6833441057
953 | FBIN,"Fortune Brands Innovations, Inc.",Building Products & Equipment,United States,Industrials,US34964C1062
954 | WCC,"WESCO International, Inc.",Industrial Distribution,United States,Industrials,US95082P1057
955 | PLNT,"Planet Fitness, Inc.",Leisure,United States,Consumer Discretionary,US72703H1014
956 | RRC,Range Resources Corporation,Oil & Gas Exploration & Production,United States,Energy,US75281A1097
957 | GLOB,Globant S.A.,Information Technology Services,Luxembourg,Technology,LU0974299876
958 | CFR,"Cullen/Frost Bankers, Inc.",Banks - Regional,United States,Financials,US2298991090
959 | STN,Stantec Inc.,Engineering & Construction,Canada,Industrials,CA85472N1096
960 | MOS,The Mosaic Company,Agricultural Inputs,United States,Materials,US61945C1036
961 | HLNE,Hamilton Lane Incorporated,Asset Management,United States,Financials,US4074971064
962 | CBSH,"Commerce Bancshares, Inc.",Banks - Regional,United States,Financials,US2005251036
963 | KD,"Kyndryl Holdings, Inc.",Information Technology Services,United States,Technology,US50155Q1004
964 | HESM,Hess Midstream LP,Oil & Gas Midstream,United States,Energy,US4281031058
965 | FYBR,"Frontier Communications Parent, Inc.",Telecom Services,United States,Communication Services,US35909D1090
966 | NYT,The New York Times Company,Publishing,United States,Communication Services,US6501111073
967 | MTCH,"Match Group, Inc.",Internet Content & Information,United States,Communication Services,US57667L1070
968 | GNRC,Generac Holdings Inc.,Specialty Industrial Machinery,United States,Industrials,US3687361044
969 | AGNC,AGNC Investment Corp.,REIT - Mortgage,United States,Real Estate,US00123Q1040
970 | AA,Alcoa Corporation,Aluminum,United States,Materials,US0138721065
971 | INGR,Ingredion Incorporated,Packaged Foods,United States,Consumer Staples,US4571871023
972 | GKOS,Glaukos Corporation,Medical Devices,United States,Healthcare,US3773221029
973 | ALK,"Alaska Air Group, Inc.",Airlines,United States,Industrials,US0116591092
974 | CACI,CACI International Inc,Information Technology Services,United States,Technology,US1271903049
975 | WTFC,Wintrust Financial Corporation,Banks - Regional,United States,Financials,US97650W1080
976 | TTC,The Toro Company,Tools & Accessories,United States,Industrials,US8910921084
977 | VNOM,"Viper Energy, Inc.",Oil & Gas Midstream,United States,Energy,US9279591062
978 | SARO,"StandardAero, Inc.",Aerospace & Defense,United States,Industrials,US85423L1035
979 | VNO,Vornado Realty Trust,REIT - Office,United States,Real Estate,US9290421091
980 | EXP,Eagle Materials Inc.,Building Materials,United States,Materials,US26969P1084
981 | IVZ,Invesco Ltd.,Asset Management,United States,Financials,BMG491BT1088
982 | GTLS,"Chart Industries, Inc.",Specialty Industrial Machinery,United States,Industrials,US16115Q3083
983 | WING,Wingstop Inc.,Restaurants,United States,Consumer Discretionary,US9741551033
984 | APA,APA Corporation,Oil & Gas Exploration & Production,United States,Energy,US03743Q1085
985 | AGI,Alamos Gold Inc.,Gold,Canada,Materials,CA0115321089
986 | LW,"Lamb Weston Holdings, Inc.",Packaged Foods,United States,Consumer Staples,US5132721045
987 | ZION,"Zions Bancorporation, National Association",Banks - Regional,United States,Financials,US9897011071
988 | BRKR,Bruker Corporation,Medical Devices,United States,Healthcare,US1167941087
989 | PSN,Parsons Corporation,Information Technology Services,United States,Technology,US70202L1026
990 | DCI,"Donaldson Company, Inc.",Specialty Industrial Machinery,United States,Industrials,US2576511099
991 | LTM,LATAM Airlines Group S.A.,Airlines,Chile,Industrials,US51817R2058
992 | OGE,OGE Energy Corp.,Utilities - Regulated Electric,United States,Utilities,US6708371033
993 | EGP,"EastGroup Properties, Inc.",REIT - Industrial,United States,Real Estate,US2772761019
994 | CX,"CEMEX, S.A.B. de C.V.",Building Materials,Mexico,Materials,US1512908898
995 | FRHC,Freedom Holding Corp.,Capital Markets,Kazakhstan,Financials,US3563901046
996 | MKTX,MarketAxess Holdings Inc.,Capital Markets,United States,Financials,US57060D1081
997 | TFX,Teleflex Incorporated,Medical Instruments & Supplies,United States,Healthcare,US8793691069
998 | FSV,FirstService Corporation,Real Estate Services,Canada,Real Estate,CA33767E2024
999 | ENPH,"Enphase Energy, Inc.",Solar,United States,Technology,US29355A1079
1000 | IONQ,"IonQ, Inc.",Computer Hardware,United States,Technology,US46222L1089
1001 | G,Genpact Limited,Information Technology Services,Bermuda,Technology,BMG3922B1072
1002 | ASR,"Grupo Aeroportuario del Sureste, S. A. B. de C. V.",Airports & Air Services,Mexico,Industrials,US40051E2028
1003 | CHE,Chemed Corporation,Medical Care Facilities,United States,Healthcare,US16359R1032
1004 | CRL,"Charles River Laboratories International, Inc.",Diagnostics & Research,United States,Healthcare,US1598641074
1005 | GPK,Graphic Packaging Holding Company,Packaging & Containers,United States,Consumer Discretionary,US3886891015
1006 | CMA,Comerica Incorporated,Banks - Regional,United States,Financials,US2003401070
1007 | PATH,UiPath Inc.,Software - Infrastructure,United States,Technology,US90364P1057
1008 | LCID,"Lucid Group, Inc.",Auto Manufacturers,United States,Consumer Discretionary,US5494981039
1009 | BBWI,"Bath & Body Works, Inc.",Specialty Retail,United States,Consumer Discretionary,US0708301041
1010 | ATI,ATI Inc.,Metal Fabrication,United States,Industrials,US01741R1023
1011 | WH,"Wyndham Hotels & Resorts, Inc.",Lodging,United States,Consumer Discretionary,US98311A1051
1012 | WF,Woori Financial Group Inc.,Banks - Regional,South Korea,Financials,US9810641087
1013 | X,United States Steel Corporation,Steel,United States,Materials,US9129091081
1014 | SKM,"SK Telecom Co., Ltd.",Telecom Services,South Korea,Communication Services,US78440P3064
1015 | HAS,"Hasbro, Inc.",Leisure,United States,Consumer Discretionary,US4180561072
1016 | ROIV,Roivant Sciences Ltd.,Biotechnology,United Kingdom,Healthcare,BMG762791017
1017 | QRVO,"Qorvo, Inc.",Semiconductors,United States,Technology,US74736K1016
1018 | KT,KT Corporation,Telecom Services,South Korea,Communication Services,US48268K1016
1019 | EXLS,"ExlService Holdings, Inc.",Information Technology Services,United States,Technology,US3020811044
1020 | AXTA,Axalta Coating Systems Ltd.,Specialty Chemicals,United States,Materials,BMG0750C1082
1021 | LPX,Louisiana-Pacific Corporation,Building Products & Equipment,United States,Industrials,US5463471053
1022 | FLS,Flowserve Corporation,Specialty Industrial Machinery,United States,Industrials,US34354P1057
1023 | TEM,"Tempus AI, Inc",Health Information Services,United States,Healthcare,US88023B1035
1024 | BRX,Brixmor Property Group Inc.,REIT - Retail,United States,Real Estate,US11120U1051
1025 | ENSG,"The Ensign Group, Inc.",Medical Care Facilities,United States,Healthcare,US29358P1012
1026 | FLR,Fluor Corporation,Engineering & Construction,United States,Industrials,US3434121022
1027 | PAAS,Pan American Silver Corp.,Gold,Canada,Materials,CA6979001089
1028 | GIL,Gildan Activewear Inc.,Apparel Manufacturing,Canada,Consumer Discretionary,CA3759161035
1029 | BERY,"Berry Global Group, Inc.",Packaging & Containers,United States,Consumer Discretionary,US08579W1036
1030 | RH,RH,Specialty Retail,United States,Consumer Discretionary,US74967X1037
1031 | INFA,Informatica Inc.,Software - Infrastructure,United States,Technology,US45674M1018
1032 | CE,Celanese Corporation,Chemicals,United States,Materials,US1508701034
1033 | MHK,"Mohawk Industries, Inc.","Furnishings, Fixtures & Appliances",United States,Consumer Discretionary,US6081901042
1034 | PARAA,Paramount Global,Entertainment,United States,Communication Services,US92556H1077
1035 | TAL,TAL Education Group,Education & Training Services,China,Consumer Staples,US8740801043
1036 | S,"SentinelOne, Inc.",Software - Infrastructure,United States,Technology,US81730H1095
1037 | AGCO,AGCO Corporation,Farm & Heavy Construction Machinery,United States,Industrials,US0010841023
1038 | AES,The AES Corporation,Utilities - Diversified,United States,Utilities,US00130H1059
1039 | SATS,EchoStar Corporation,Communication Equipment,United States,Technology,US2787681061
1040 | SNV,Synovus Financial Corp.,Banks - Regional,United States,Financials,US87161C5013
1041 | EDU,New Oriental Education & Technology Group Inc.,Education & Training Services,China,Consumer Staples,US6475812060
1042 | SFD,"Smithfield Foods, Inc.",Farm Products,,Consumer Staples,
1043 | ALV,"Autoliv, Inc.",Auto Parts,Sweden,Consumer Discretionary,US0528001094
1044 | LSCC,Lattice Semiconductor Corporation,Semiconductors,United States,Technology,US5184151042
1045 | CAE,CAE Inc.,Aerospace & Defense,Canada,Industrials,CA1247651088
1046 | FRPT,"Freshpet, Inc.",Packaged Foods,United States,Consumer Staples,US3580391056
1047 | ASND,Ascendis Pharma A/S,Biotechnology,Denmark,Healthcare,US04351P1012
1048 | TREX,"Trex Company, Inc.",Building Products & Equipment,United States,Industrials,US89531P1057
1049 | STEP,StepStone Group Inc.,Asset Management,United States,Financials,US85914M1071
1050 | OTEX,Open Text Corporation,Software - Application,Canada,Technology,CA6837151068
1051 | DLB,"Dolby Laboratories, Inc.",Specialty Business Services,United States,Industrials,US25659T1079
1052 | HII,"Huntington Ingalls Industries, Inc.",Aerospace & Defense,United States,Industrials,US4464131063
1053 | SUN,Sunoco LP,Oil & Gas Refining & Marketing,United States,Energy,US86765K1097
1054 | PB,"Prosperity Bancshares, Inc.",Banks - Regional,United States,Financials,US7436061052
1055 | LNW,"Light & Wonder, Inc.",Gambling,United States,Consumer Discretionary,US80874P1093
1056 | AM,Antero Midstream Corporation,Oil & Gas Midstream,United States,Energy,US03676B1026
1057 | VIPS,Vipshop Holdings Limited,Internet Retail,China,Consumer Discretionary,US92763W1036
1058 | CZR,"Caesars Entertainment, Inc.",Resorts & Casinos,United States,Consumer Discretionary,US12769G1004
1059 | DDS,"Dillard's, Inc.",Department Stores,United States,Consumer Discretionary,US2540671011
1060 | AXS,AXIS Capital Holdings Limited,Insurance - Specialty,Bermuda,Financials,BMG0692U1099
1061 | ADC,Agree Realty Corporation,REIT - Retail,United States,Real Estate,US0084921008
1062 | RVMD,"Revolution Medicines, Inc.",Biotechnology,United States,Healthcare,US76155X1000
1063 | NNN,"NNN REIT, Inc.",REIT - Retail,United States,Real Estate,US6374171063
1064 | ICL,ICL Group Ltd,Agricultural Inputs,Israel,Materials,IL0002810146
1065 | ONB,Old National Bancorp,Banks - Regional,United States,Financials,US6800331075
1066 | MTDR,Matador Resources Company,Oil & Gas Exploration & Production,United States,Energy,US5764852050
1067 | FN,Fabrinet,Electronic Components,Cayman Islands,Technology,KYG3323L1005
1068 | SIRI,Sirius XM Holdings Inc.,Entertainment,United States,Communication Services,US82968B1035
1069 | JAZZ,Jazz Pharmaceuticals plc,Biotechnology,Ireland,Healthcare,IE00B4Q5ZN47
1070 | AN,"AutoNation, Inc.",Auto & Truck Dealerships,United States,Consumer Discretionary,US05329W1027
1071 | HRB,"H&R Block, Inc.",Personal Services,United States,Consumer Discretionary,US0936711052
1072 | ERJ,Embraer S.A.,Aerospace & Defense,Brazil,Industrials,US29082A1079
1073 | LOAR,Loar Holdings Inc.,Aerospace & Defense,United States,Industrials,US53947R1059
1074 | ESAB,ESAB Corporation,Metal Fabrication,United States,Industrials,US29605J1060
1075 | BECN,"Beacon Roofing Supply, Inc.",Industrial Distribution,United States,Industrials,US0736851090
1076 | PARA,Paramount Global,Entertainment,United States,Communication Services,US92556H2067
1077 | CCCS,CCC Intelligent Solutions Holdings Inc.,Software - Application,United States,Technology,US12510Q1004
1078 | SPSC,"SPS Commerce, Inc.",Software - Application,United States,Technology,US78463M1071
1079 | AZEK,The AZEK Company Inc.,Building Products & Equipment,United States,Industrials,US05478C1053
1080 | OS,"OneStream, Inc.",Software - Infrastructure,United States,Technology,US68278B1070
1081 | WHR,Whirlpool Corporation,"Furnishings, Fixtures & Appliances",United States,Consumer Discretionary,US9633201069
1082 | LEVI,Levi Strauss & Co.,Apparel Manufacturing,United States,Consumer Discretionary,US52736R1023
1083 | FR,"First Industrial Realty Trust, Inc.",REIT - Industrial,United States,Real Estate,US32054K1034
1084 | KBR,"KBR, Inc.",Engineering & Construction,United States,Industrials,US48242W1062
1085 | BPMC,Blueprint Medicines Corporation,Biotechnology,United States,Healthcare,US09627Y1091
1086 | CIGI,Colliers International Group Inc.,Real Estate Services,Canada,Real Estate,CA1946931070
1087 | MKSI,"MKS Instruments, Inc.",Scientific & Technical Instruments,United States,Technology,US55306N1046
1088 | WEX,WEX Inc.,Software - Infrastructure,United States,Technology,US96208T1043
1089 | BILI,Bilibili Inc.,Electronic Gaming & Multimedia,China,Communication Services,US0900401060
1090 | BPOP,"Popular, Inc.",Banks - Regional,United States,Financials,PR7331747001
1091 | CWAN,"Clearwater Analytics Holdings, Inc.",Software - Application,United States,Technology,US1851231068
1092 | MNSO,MINISO Group Holding Limited,Specialty Retail,China,Consumer Discretionary,US66981J1025
1093 | XP,XP Inc.,Capital Markets,Cayman Islands,Financials,KYG982391099
1094 | MDGL,"Madrigal Pharmaceuticals, Inc.",Biotechnology,United States,Healthcare,US5588681057
1095 | RHI,Robert Half Inc.,Staffing & Employment Services,United States,Industrials,US7703231032
1096 | CHRD,Chord Energy Corporation,Oil & Gas Exploration & Production,United States,Energy,US6742152076
1097 | HALO,"Halozyme Therapeutics, Inc.",Biotechnology,United States,Healthcare,US40637H1095
1098 | BWA,BorgWarner Inc.,Auto Parts,United States,Consumer Discretionary,US0997241064
1099 | BFAM,Bright Horizons Family Solutions Inc.,Personal Services,United States,Consumer Discretionary,US1091941005
1100 | UFPI,"UFP Industries, Inc.",Lumber & Wood Production,United States,Materials,US90278Q1085
1101 | NBIS,Nebius Group N.V.,Internet Content & Information,Netherlands,Communication Services,NL0009805522
1102 | BOKF,BOK Financial Corporation,Banks - Regional,United States,Financials,US05561Q2012
1103 | SSD,"Simpson Manufacturing Co., Inc.",Lumber & Wood Production,United States,Materials,US8290731053
1104 | WTS,"Watts Water Technologies, Inc.",Specialty Industrial Machinery,United States,Industrials,US9427491025
1105 | WFG,West Fraser Timber Co. Ltd.,Lumber & Wood Production,Canada,Materials,CA9528451052
1106 | FMC,FMC Corporation,Agricultural Inputs,United States,Materials,US3024913036
1107 | HCP,"HashiCorp, Inc.",Software - Infrastructure,United States,Technology,US4181001037
1108 | WAY,Waystar Holding Corp.,Health Information Services,United States,Healthcare,US9467841055
1109 | CVLT,"Commvault Systems, Inc.",Software - Application,United States,Technology,US2041661024
1110 | JXN,Jackson Financial Inc.,Insurance - Life,United States,Financials,US46817M1071
1111 | OLLI,"Ollie's Bargain Outlet Holdings, Inc.",Discount Stores,United States,Consumer Staples,US6811161099
1112 | FCN,"FTI Consulting, Inc.",Consulting Services,United States,Industrials,US3029411093
1113 | OMF,"OneMain Holdings, Inc.",Credit Services,United States,Financials,US68268W1036
1114 | CHH,"Choice Hotels International, Inc.",Lodging,United States,Consumer Discretionary,US1699051066
1115 | ENLC,"EnLink Midstream, LLC",Oil & Gas Midstream,United States,Energy,US29336T1007
1116 | VOYA,"Voya Financial, Inc.",Financial Conglomerates,United States,Financials,US9290891004
1117 | OLED,Universal Display Corporation,Electronic Components,United States,Technology,US91347P1057
1118 | HIMS,"Hims & Hers Health, Inc.",Household & Personal Products,United States,Consumer Staples,US4330001060
1119 | JHG,Janus Henderson Group plc,Asset Management,United Kingdom,Financials,JE00BYPZJM29
1120 | TMHC,Taylor Morrison Home Corporation,Residential Construction,United States,Consumer Discretionary,US87724P1066
1121 | BMA,Banco Macro S.A.,Banks - Regional,Argentina,Financials,US05961W1053
1122 | EAT,"Brinker International, Inc.",Restaurants,United States,Consumer Discretionary,US1096411004
1123 | BBIO,"BridgeBio Pharma, Inc.",Biotechnology,United States,Healthcare,US10806X1028
1124 | DINO,HF Sinclair Corporation,Oil & Gas Refining & Marketing,United States,Energy,US4039491000
1125 | WSC,WillScot Holdings Corporation,Rental & Leasing Services,United States,Industrials,US9713781048
1126 | BYD,Boyd Gaming Corporation,Resorts & Casinos,United States,Consumer Discretionary,US1033041013
1127 | PJT,PJT Partners Inc.,Capital Markets,United States,Financials,US69343T1079
1128 | CGNX,Cognex Corporation,Scientific & Technical Instruments,United States,Technology,US1924221039
1129 | R,"Ryder System, Inc.",Rental & Leasing Services,United States,Industrials,US7835491082
1130 | ADT,ADT Inc.,Security & Protection Services,United States,Industrials,US00090Q1031
1131 | COOP,Mr. Cooper Group Inc.,Mortgage Finance,United States,Financials,US62482R1077
1132 | SPXC,"SPX Technologies, Inc.",Building Products & Equipment,United States,Industrials,US78473E1038
1133 | CWST,"Casella Waste Systems, Inc.",Waste Management,United States,Industrials,US1474481041
1134 | RLI,RLI Corp.,Insurance - Property & Casualty,United States,Financials,US7496071074
1135 | ZWS,Zurn Elkay Water Solutions Corporation,Pollution & Treatment Controls,United States,Industrials,US98983L1089
1136 | LLYVK,Liberty Live Group,Entertainment,United States,Communication Services,US5312297220
1137 | NVMI,Nova Ltd.,Semiconductor Equipment & Materials,Israel,Technology,IL0010845571
1138 | TKC,Turkcell Iletisim Hizmetleri A.S.,Telecom Services,Turkey,Communication Services,US9001112047
1139 | LLYVA,Liberty Live Group,Entertainment,United States,Communication Services,US5312297485
1140 | HMY,Harmony Gold Mining Company Limited,Gold,South Africa,Materials,US4132163001
1141 | LEGN,Legend Biotech Corporation,Biotechnology,United States,Healthcare,US52490G1022
1142 | TRNO,Terreno Realty Corporation,REIT - Industrial,United States,Real Estate,US88146M1018
1143 | JBTM,JBT Marel Corporation,Specialty Industrial Machinery,United States,Industrials,
1144 | BZ,Kanzhun Limited,Internet Content & Information,China,Communication Services,US48553T1060
1145 | VMI,"Valmont Industries, Inc.",Conglomerates,United States,Industrials,US9202531011
1146 | SITE,"SiteOne Landscape Supply, Inc.",Industrial Distribution,United States,Industrials,US82982L1035
1147 | UGI,UGI Corporation,Utilities - Regulated Gas,United States,Utilities,US9026811052
1148 | AWI,"Armstrong World Industries, Inc.",Building Products & Equipment,United States,Industrials,US04247X1028
1149 | DJT,Trump Media & Technology Group Corp.,Internet Content & Information,United States,Communication Services,US25400Q1058
1150 | STWD,"Starwood Property Trust, Inc.",REIT - Mortgage,United States,Real Estate,US85571B1052
1151 | FAF,First American Financial Corporation,Insurance - Specialty,United States,Financials,US31847R1023
1152 | MTG,MGIC Investment Corporation,Insurance - Specialty,United States,Financials,US5528481030
1153 | QFIN,"Qifu Technology, Inc.",Credit Services,China,Financials,US88557W1018
1154 | CADE,Cadence Bank,Banks - Regional,United States,Financials,US12740C1036
1155 | MSA,MSA Safety Incorporated,Security & Protection Services,United States,Industrials,US5534981064
1156 | FSK,FS KKR Capital Corp.,Asset Management,United States,Financials,US3026352068
1157 | RMBS,Rambus Inc.,Semiconductors,United States,Technology,US7509171069
1158 | JOBY,"Joby Aviation, Inc.",Airports & Air Services,United States,Industrials,KYG651631007
1159 | COTY,Coty Inc.,Household & Personal Products,United States,Consumer Staples,US2220702037
1160 | TIMB,TIM S.A.,Telecom Services,Brazil,Communication Services,US88706T1088
1161 | CACC,Credit Acceptance Corporation,Credit Services,United States,Financials,US2253101016
1162 | MTN,"Vail Resorts, Inc.",Resorts & Casinos,United States,Consumer Discretionary,US91879Q1094
1163 | CORT,Corcept Therapeutics Incorporated,Biotechnology,United States,Healthcare,US2183521028
1164 | MMSI,"Merit Medical Systems, Inc.",Medical Instruments & Supplies,United States,Healthcare,US5898891040
1165 | RHP,"Ryman Hospitality Properties, Inc.",REIT - Hotel & Motel,United States,Real Estate,US78377T1079
1166 | GNTX,Gentex Corporation,Auto Parts,United States,Consumer Discretionary,US3719011096
1167 | LNTH,"Lantheus Holdings, Inc.",Drug Manufacturers - Specialty & Generic,United States,Healthcare,US5165441032
1168 | SRAD,Sportradar Group AG,Software - Application,Switzerland,Technology,CH1134239669
1169 | STAG,"STAG Industrial, Inc.",REIT - Industrial,United States,Real Estate,US85254J1025
1170 | COLD,"Americold Realty Trust, Inc.",REIT - Industrial,United States,Real Estate,US03064D1081
1171 | MAT,"Mattel, Inc.",Leisure,United States,Consumer Discretionary,US5770811025
1172 | ETSY,"Etsy, Inc.",Internet Retail,United States,Consumer Discretionary,US29786A1060
1173 | ESNT,Essent Group Ltd.,Insurance - Specialty,Bermuda,Financials,BMG3198U1027
1174 | POST,"Post Holdings, Inc.",Packaged Foods,United States,Consumer Staples,US7374461041
1175 | OSK,Oshkosh Corporation,Farm & Heavy Construction Machinery,United States,Industrials,US6882392011
1176 | LSTR,"Landstar System, Inc.",Integrated Freight & Logistics,United States,Industrials,US5150981018
1177 | MARA,"MARA Holdings, Inc.",Capital Markets,United States,Financials,US5657881067
1178 | ZK,ZEEKR Intelligent Technology Holding Limited,Auto Manufacturers,China,Consumer Discretionary,US98923K1034
1179 | NFG,National Fuel Gas Company,Oil & Gas Integrated,United States,Energy,US6361801011
1180 | ARW,"Arrow Electronics, Inc.",Electronics & Computer Distribution,United States,Technology,US0427351004
1181 | W,Wayfair Inc.,Internet Retail,United States,Consumer Discretionary,US94419L1017
1182 | ESI,Element Solutions Inc,Specialty Chemicals,United States,Materials,US28618M1062
1183 | ALTM,Arcadium Lithium plc,Specialty Chemicals,Ireland,Materials,JE00BM9HZ112
1184 | BRFS,BRF S.A.,Packaged Foods,Brazil,Consumer Staples,US10552T1079
1185 | BLCO,Bausch + Lomb Corporation,Medical Instruments & Supplies,Canada,Healthcare,CA0717051076
1186 | LTH,"Life Time Group Holdings, Inc.",Leisure,United States,Consumer Discretionary,US53190C1027
1187 | BMI,"Badger Meter, Inc.",Scientific & Technical Instruments,United States,Technology,US0565251081
1188 | KEX,Kirby Corporation,Marine Shipping,United States,Industrials,US4972661064
1189 | HR,Healthcare Realty Trust Incorporated,REIT - Healthcare Facilities,United States,Real Estate,US42226K1051
1190 | ANF,Abercrombie & Fitch Co.,Apparel Retail,United States,Consumer Discretionary,US0028962076
1191 | UPST,"Upstart Holdings, Inc.",Credit Services,United States,Financials,US91680M1071
1192 | NUVL,"Nuvalent, Inc.",Biotechnology,United States,Healthcare,US6707031075
1193 | HOMB,"Home Bancshares, Inc. (Conway, AR)",Banks - Regional,United States,Financials,US4368932004
1194 | TEO,Telecom Argentina S.A.,Telecom Services,Argentina,Communication Services,US8792732096
1195 | CROX,"Crocs, Inc.",Footwear & Accessories,United States,Consumer Discretionary,US2270461096
1196 | VIRT,"Virtu Financial, Inc.",Capital Markets,United States,Financials,US9282541013
1197 | ELAN,Elanco Animal Health Incorporated,Drug Manufacturers - Specialty & Generic,United States,Healthcare,US28414H1032
1198 | SLM,SLM Corporation,Credit Services,United States,Financials,US78442P1066
1199 | CSWI,"CSW Industrials, Inc.",Specialty Industrial Machinery,United States,Industrials,US1264021064
1200 | FSS,Federal Signal Corporation,Pollution & Treatment Controls,United States,Industrials,US3138551086
1201 | TLX,Telix Pharmaceuticals Limited,Biotechnology,Australia,Healthcare,
1202 | FRSH,Freshworks Inc.,Software - Application,United States,Technology,US3580541049
1203 | ELF,"e.l.f. Beauty, Inc.",Household & Personal Products,United States,Consumer Staples,US26856L1035
1204 | GPI,"Group 1 Automotive, Inc.",Auto & Truck Dealerships,United States,Consumer Discretionary,US3989051095
1205 | GH,"Guardant Health, Inc.",Diagnostics & Research,United States,Healthcare,US40131M1099
1206 | MC,Moelis & Company,Capital Markets,United States,Financials,US60786M1053
1207 | CIG,Companhia Energética de Minas Gerais - CEMIG,Utilities - Diversified,Brazil,Utilities,US2044096012
1208 | CIG.C,Companhia Energética de Minas Gerais - CEMIG,Utilities - Diversified,,Utilities,US2044098828
1209 | CRVL,CorVel Corporation,Insurance Brokers,United States,Financials,US2210061097
1210 | GGB,Gerdau S.A.,Steel,Brazil,Materials,US3737371050
1211 | AMKR,"Amkor Technology, Inc.",Semiconductor Equipment & Materials,United States,Technology,US0316521006
1212 | UMBF,UMB Financial Corporation,Banks - Regional,United States,Financials,US9027881088
1213 | RITM,Rithm Capital Corp.,REIT - Mortgage,United States,Real Estate,US64828T2015
1214 | GATX,GATX Corporation,Rental & Leasing Services,United States,Industrials,US3614481030
1215 | QTWO,"Q2 Holdings, Inc.",Software - Application,United States,Technology,US74736L1098
1216 | OBDC,Blue Owl Capital Corporation,Asset Management,United States,Financials,US69121K1043
1217 | COLB,"Columbia Banking System, Inc.",Banks - Regional,United States,Financials,US1972361026
1218 | MTH,Meritage Homes Corporation,Residential Construction,United States,Consumer Discretionary,US59001A1025
1219 | CELH,"Celsius Holdings, Inc.",Beverages - Non-Alcoholic,United States,Consumer Staples,US15118V2079
1220 | ASTS,"AST SpaceMobile, Inc.",Communication Equipment,United States,Technology,US00217D1000
1221 | LNC,Lincoln National Corporation,Insurance - Life,United States,Financials,US5341871094
1222 | LYFT,"Lyft, Inc.",Software - Application,United States,Technology,US55087P1049
1223 | KNF,Knife River Corporation,Building Materials,United States,Materials,US4988941047
1224 | WK,Workiva Inc.,Software - Application,United States,Technology,US98139A1051
1225 | IDA,"IDACORP, Inc.",Utilities - Regulated Electric,United States,Utilities,US4511071064
1226 | SIGI,"Selective Insurance Group, Inc.",Insurance - Property & Casualty,United States,Financials,US8163001071
1227 | INSP,"Inspire Medical Systems, Inc.",Medical Devices,United States,Healthcare,US4577301090
1228 | REYN,Reynolds Consumer Products Inc.,Packaging & Containers,United States,Consumer Discretionary,US76171L1061
1229 | OZK,Bank OZK,Banks - Regional,United States,Financials,US06417N1037
1230 | NXT,Nextracker Inc.,Solar,United States,Technology,US65290E1010
1231 | CYTK,"Cytokinetics, Incorporated",Biotechnology,United States,Healthcare,US23282W6057
1232 | AMG,"Affiliated Managers Group, Inc.",Asset Management,United States,Financials,US0082521081
1233 | MOG.A,Moog Inc.,Aerospace & Defense,United States,Industrials,US6153942023
1234 | PFSI,"PennyMac Financial Services, Inc.",Mortgage Finance,United States,Financials,US70932M1071
1235 | CMC,Commercial Metals Company,Steel,United States,Materials,US2017231034
1236 | TX,Ternium S.A.,Steel,Luxembourg,Materials,US8808901081
1237 | MOG.B,Moog Inc.,Aerospace & Defense,United States,Industrials,US6153943013
1238 | VNT,Vontier Corporation,Scientific & Technical Instruments,United States,Technology,US9288811014
1239 | STVN,Stevanato Group S.p.A.,Medical Instruments & Supplies,Italy,Healthcare,IT0005452658
1240 | VLY,Valley National Bancorp,Banks - Regional,United States,Financials,US9197941076
1241 | SLGN,Silgan Holdings Inc.,Packaging & Containers,United States,Consumer Discretionary,US8270481091
1242 | ACIW,"ACI Worldwide, Inc.",Software - Infrastructure,United States,Technology,US0044981019
1243 | GBCI,"Glacier Bancorp, Inc.",Banks - Regional,United States,Financials,US37637Q1058
1244 | HRI,Herc Holdings Inc.,Rental & Leasing Services,United States,Industrials,US42704L1044
1245 | THG,"The Hanover Insurance Group, Inc.",Insurance - Property & Casualty,United States,Financials,US4108671052
1246 | FG,"F&G Annuities & Life, Inc.",Insurance - Life,United States,Financials,US30190A1043
1247 | FNB,F.N.B. Corporation,Banks - Regional,United States,Financials,US3025201019
1248 | EPRT,"Essential Properties Realty Trust, Inc.",REIT - Diversified,United States,Real Estate,US29670E1073
1249 | INTA,"Intapp, Inc.",Software - Application,United States,Technology,US45827U1097
1250 | DAR,Darling Ingredients Inc.,Packaged Foods,United States,Consumer Staples,US2372661015
1251 | NOV,NOV Inc.,Oil & Gas Equipment & Services,United States,Energy,US62955J1034
1252 | CHX,ChampionX Corporation,Oil & Gas Equipment & Services,United States,Energy,US15872M1045
1253 | GRFS,"Grifols, S.A.",Drug Manufacturers - General,Spain,Healthcare,US3984384087
1254 | CRK,"Comstock Resources, Inc.",Oil & Gas Exploration & Production,United States,Energy,US2057683029
1255 | LFUS,"Littelfuse, Inc.",Electronic Components,United States,Technology,US5370081045
1256 | IBP,"Installed Building Products, Inc.",Residential Construction,United States,Consumer Discretionary,US45780R1014
1257 | QXO,"QXO, Inc.",Software - Application,United States,Technology,US82846H4056
1258 | GXO,"GXO Logistics, Inc.",Integrated Freight & Logistics,United States,Industrials,US36262G1013
1259 | USM,United States Cellular Corporation,Telecom Services,United States,Communication Services,US9116841084
1260 | CALM,"Cal-Maine Foods, Inc.",Farm Products,United States,Consumer Staples,US1280302027
1261 | NSIT,"Insight Enterprises, Inc.",Electronics & Computer Distribution,United States,Technology,US45765U1034
1262 | FFIN,"First Financial Bankshares, Inc.",Banks - Regional,United States,Financials,US32020R1095
1263 | HXL,Hexcel Corporation,Aerospace & Defense,United States,Industrials,US4282911084
1264 | MAIN,Main Street Capital Corporation,Asset Management,United States,Financials,US56035L1044
1265 | THO,"THOR Industries, Inc.",Recreational Vehicles,United States,Consumer Discretionary,US8851601018
1266 | QLYS,"Qualys, Inc.",Software - Infrastructure,United States,Technology,US74758T3032
1267 | IONS,"Ionis Pharmaceuticals, Inc.",Biotechnology,United States,Healthcare,US4622221004
1268 | INGM,Ingram Micro Holding Corporation,Information Technology Services,United States,Technology,US4571521065
1269 | TKR,The Timken Company,Tools & Accessories,United States,Industrials,US8873891043
1270 | CRUS,"Cirrus Logic, Inc.",Semiconductors,United States,Technology,US1727551004
1271 | ABG,"Asbury Automotive Group, Inc.",Auto & Truck Dealerships,United States,Consumer Discretionary,US0434361046
1272 | SMR,NuScale Power Corporation,Specialty Industrial Machinery,United States,Industrials,US67079K1007
1273 | TENB,"Tenable Holdings, Inc.",Software - Infrastructure,United States,Technology,US88025T1025
1274 | LITE,Lumentum Holdings Inc.,Communication Equipment,United States,Technology,US55024U1097
1275 | NOVT,Novanta Inc.,Scientific & Technical Instruments,United States,Technology,CA67000B1040
1276 | KRG,Kite Realty Group Trust,REIT - Retail,United States,Real Estate,US49803T3005
1277 | BOOT,"Boot Barn Holdings, Inc.",Apparel Retail,United States,Consumer Discretionary,US0994061002
1278 | SWX,"Southwest Gas Holdings, Inc.",Utilities - Regulated Gas,United States,Utilities,US8448951025
1279 | CLBT,Cellebrite DI Ltd.,Software - Infrastructure,Israel,Technology,IL0011794802
1280 | FIVE,"Five Below, Inc.",Specialty Retail,United States,Consumer Discretionary,US33829M1018
1281 | MSGS,Madison Square Garden Sports Corp.,Entertainment,United States,Communication Services,US55825T1034
1282 | SMTC,Semtech Corporation,Semiconductors,United States,Technology,US8168501018
1283 | SOUN,"SoundHound AI, Inc.",Software - Application,United States,Technology,US8361001071
1284 | MAC,The Macerich Company,REIT - Retail,United States,Real Estate,US5543821012
1285 | DNB,"Dun & Bradstreet Holdings, Inc.",Financial Data & Stock Exchanges,United States,Financials,US26484T1060
1286 | OPCH,"Option Care Health, Inc.",Medical Care Facilities,United States,Healthcare,US68404L2016
1287 | DY,"Dycom Industries, Inc.",Engineering & Construction,United States,Industrials,US2674751019
1288 | SNDR,"Schneider National, Inc.",Trucking,United States,Industrials,US80689H1023
1289 | BCPC,Balchem Corporation,Specialty Chemicals,United States,Materials,US0576652004
1290 | ACT,"Enact Holdings, Inc.",Insurance - Specialty,United States,Financials,US29249E1091
1291 | LEA,Lear Corporation,Auto Parts,United States,Consumer Discretionary,US5218652049
1292 | UBSI,"United Bankshares, Inc.",Banks - Regional,United States,Financials,US9099071071
1293 | SKY,"Champion Homes, Inc.",Residential Construction,United States,Consumer Discretionary,US8308301055
1294 | SAIC,Science Applications International Corporation,Information Technology Services,United States,Technology,US8086251076
1295 | LRN,"Stride, Inc.",Education & Training Services,United States,Consumer Staples,US86333M1080
1296 | SEE,Sealed Air Corporation,Packaging & Containers,United States,Consumer Discretionary,US81211K1007
1297 | NE.WSA,Noble Corporation plc,,,,
1298 | NE,Noble Corporation plc,Oil & Gas Drilling,United States,Energy,GB00BMXNWH07
1299 | GTES,Gates Industrial Corporation plc,Specialty Industrial Machinery,United States,Industrials,GB00BD9G2S12
1300 | LUMN,"Lumen Technologies, Inc.",Telecom Services,United States,Communication Services,US5502411037
1301 | TSEM,Tower Semiconductor Ltd.,Semiconductors,Israel,Technology,IL0010823792
1302 | VRNS,"Varonis Systems, Inc.",Software - Infrastructure,United States,Technology,US9222801022
1303 | KTB,"Kontoor Brands, Inc.",Apparel Manufacturing,United States,Consumer Discretionary,US50050N1037
1304 | HWC,Hancock Whitney Corporation,Banks - Regional,United States,Financials,US4101201097
1305 | COLM,Columbia Sportswear Company,Apparel Manufacturing,United States,Consumer Discretionary,US1985161066
1306 | URBN,"Urban Outfitters, Inc.",Apparel Retail,United States,Consumer Discretionary,US9170471026
1307 | PVH,PVH Corp.,Apparel Manufacturing,United States,Consumer Discretionary,US6936561009
1308 | RDN,Radian Group Inc.,Insurance - Specialty,United States,Financials,US7502361014
1309 | AL,Air Lease Corporation,Rental & Leasing Services,United States,Industrials,US00912X3026
1310 | CTRE,"CareTrust REIT, Inc.",REIT - Healthcare Facilities,United States,Real Estate,US14174T1079
1311 | RRR,"Red Rock Resorts, Inc.",Resorts & Casinos,United States,Consumer Discretionary,US75700L1089
1312 | CUZ,Cousins Properties Incorporated,REIT - Office,United States,Real Estate,US2227955026
1313 | PAGP,"Plains GP Holdings, L.P.",Oil & Gas Midstream,United States,Energy,US72651A2078
1314 | KTOS,"Kratos Defense & Security Solutions, Inc.",Aerospace & Defense,United States,Industrials,US50077B2079
1315 | ALKS,Alkermes plc,Drug Manufacturers - Specialty & Generic,Ireland,Healthcare,IE00B56GVS15
1316 | SHAK,Shake Shack Inc.,Restaurants,United States,Consumer Discretionary,US8190471016
1317 | PECO,"Phillips Edison & Company, Inc.",REIT - Retail,United States,Real Estate,US71844V2016
1318 | ASAN,"Asana, Inc.",Software - Application,United States,Technology,US04342Y1047
1319 | SFBS,"ServisFirst Bancshares, Inc.",Banks - Regional,United States,Financials,US81768T1088
1320 | CLF,Cleveland-Cliffs Inc.,Steel,United States,Materials,US1858991011
1321 | AROC,"Archrock, Inc.",Oil & Gas Equipment & Services,United States,Energy,US03957W1062
1322 | MOD,Modine Manufacturing Company,Auto Parts,United States,Consumer Discretionary,US6078281002
1323 | FCFS,"FirstCash Holdings, Inc.",Credit Services,United States,Financials,US33768G1076
1324 | AXSM,"Axsome Therapeutics, Inc.",Biotechnology,United States,Healthcare,US05464T1043
1325 | IEP,Icahn Enterprises L.P.,Oil & Gas Refining & Marketing,United States,Energy,US4511001012
1326 | VIST,"Vista Energy, S.A.B. de C.V.",Oil & Gas Exploration & Production,Mexico,Energy,US92837L1098
1327 | PIPR,Piper Sandler Companies,Capital Markets,United States,Financials,US7240781002
1328 | CIVI,"Civitas Resources, Inc.",Oil & Gas Exploration & Production,United States,Energy,US17888H1032
1329 | SOBO,South Bow Corporation,,Canada (Federal Level),,CA83671M1059
1330 | WHD,"Cactus, Inc.",Oil & Gas Equipment & Services,United States,Energy,US1272031071
1331 | KBH,KB Home,Residential Construction,United States,Consumer Discretionary,US48666K1097
1332 | PAM,Pampa Energía S.A.,Utilities - Independent Power Producers,Argentina,Utilities,US6976602077
1333 | LOPE,"Grand Canyon Education, Inc.",Education & Training Services,United States,Consumer Staples,US38526M1062
1334 | BCC,Boise Cascade Company,Building Materials,United States,Materials,US09739D1000
1335 | AVAV,"AeroVironment, Inc.",Aerospace & Defense,United States,Industrials,US0080731088
1336 | CWEN.A,"Clearway Energy, Inc.",Utilities - Renewable,United States,Utilities,US18539C2044
1337 | MGY,Magnolia Oil & Gas Corporation,Oil & Gas Exploration & Production,United States,Energy,US5596631094
1338 | BRZE,"Braze, Inc.",Software - Application,United States,Technology,US10576N1028
1339 | RDNT,"RadNet, Inc.",Diagnostics & Research,United States,Healthcare,US7504911022
1340 | NXST,"Nexstar Media Group, Inc.",Broadcasting,United States,Communication Services,US65336K1034
1341 | BWIN,"The Baldwin Insurance Group, Inc.",Insurance Brokers,United States,Financials,US05589G1022
1342 | WTM,"White Mountains Insurance Group, Ltd.",Insurance - Property & Casualty,Bermuda,Financials,BMG9618E1075
1343 | BIPC,Brookfield Infrastructure Corporation,Utilities - Regulated Gas,United States,Utilities,CA11275Q1072
1344 | SLG,SL Green Realty Corp.,REIT - Office,United States,Real Estate,US78440X8873
1345 | LAZ,"Lazard, Inc.",Capital Markets,United States,Financials,US52110M1099
1346 | PHI,PLDT Inc.,Telecom Services,Philippines,Communication Services,US69344D4088
1347 | ITGR,Integer Holdings Corporation,Medical Devices,United States,Healthcare,US45826H1095
1348 | NSA,National Storage Affiliates Trust,REIT - Industrial,United States,Real Estate,US6378701063
1349 | AMTM,"Amentum Holdings, Inc.",Specialty Business Services,United States,Industrials,US0239391016
1350 | BOX,"Box, Inc.",Software - Infrastructure,United States,Technology,US10316T1043
1351 | NEU,NewMarket Corporation,Specialty Chemicals,United States,Materials,US6515871076
1352 | WFRD,Weatherford International plc,Oil & Gas Equipment & Services,United States,Energy,IE00BLNN3691
1353 | AGO,Assured Guaranty Ltd.,Insurance - Specialty,Bermuda,Financials,BMG0585R1060
1354 | TGTX,"TG Therapeutics, Inc.",Biotechnology,United States,Healthcare,US88322Q1085
1355 | ESGR,Enstar Group Limited,Insurance - Diversified,Bermuda,Financials,BMG3075P1014
1356 | ACA,"Arcosa, Inc.",Engineering & Construction,United States,Industrials,US0396531008
1357 | VVV,Valvoline Inc.,Auto & Truck Dealerships,United States,Consumer Discretionary,US92047W1018
1358 | BBU,Brookfield Business Partners L.P.,Conglomerates,Bermuda,Industrials,BMG162341090
1359 | CBT,Cabot Corporation,Specialty Chemicals,United States,Materials,US1270551013
1360 | ITRI,"Itron, Inc.",Scientific & Technical Instruments,United States,Technology,US4657411066
1361 | BBAR,Banco BBVA Argentina S.A.,Banks - Regional,Argentina,Financials,US0589341009
1362 | SON,Sonoco Products Company,Packaging & Containers,United States,Consumer Discretionary,US8354951027
1363 | NJR,New Jersey Resources Corporation,Utilities - Regulated Gas,United States,Utilities,US6460251068
1364 | RUSHA,"Rush Enterprises, Inc.",Auto & Truck Dealerships,United States,Consumer Discretionary,US7818462092
1365 | EXPO,"Exponent, Inc.",Engineering & Construction,United States,Industrials,US30214U1025
1366 | TNET,"TriNet Group, Inc.",Staffing & Employment Services,United States,Industrials,US8962881079
1367 | PONY,Pony AI Inc.,Electronic Components,China,Technology,US7329081084
1368 | LANC,Lancaster Colony Corporation,Packaged Foods,United States,Consumer Staples,US5138471033
1369 | KRC,Kilroy Realty Corporation,REIT - Office,United States,Real Estate,US49427F1084
1370 | LB,LandBridge Company LLC,Oil & Gas Equipment & Services,United States,Energy,US5149521008
1371 | RUSHB,"Rush Enterprises, Inc.",Auto & Truck Dealerships,United States,Consumer Discretionary,US7818463082
1372 | NARI,"Inari Medical, Inc.",Medical Devices,United States,Healthcare,US45332Y1091
1373 | BDC,Belden Inc.,Communication Equipment,United States,Technology,US0774541066
1374 | TIGO,Millicom International Cellular S.A.,Telecom Services,Luxembourg,Communication Services,LU0038705702
1375 | CRC,California Resources Corporation,Oil & Gas Exploration & Production,United States,Energy,US13057Q3056
1376 | BE,Bloom Energy Corporation,Electrical Equipment & Parts,United States,Industrials,US0937121079
1377 | SNRE,Sunrise Communications AG,Other,Switzerland,,US8679751045
1378 | RELY,"Remitly Global, Inc.",Software - Infrastructure,United States,Technology,US75960P1049
1379 | FTDR,"Frontdoor, Inc.",Personal Services,United States,Consumer Discretionary,US35905A1097
1380 | ACHR,Archer Aviation Inc.,Aerospace & Defense,United States,Industrials,US03945R1023
1381 | ELP,Companhia Paranaense de Energia - COPEL,Utilities - Diversified,Brazil,Utilities,US20441B6056
1382 | ELPC,Companhia Paranaense de Energia - COPEL,Utilities - Diversified,Brazil,Utilities,US20441B7047
1383 | SKYW,"SkyWest, Inc.",Airlines,United States,Industrials,US8308791024
1384 | AHR,"American Healthcare REIT, Inc.",REIT - Healthcare Facilities,United States,Real Estate,US3981823038
1385 | MSM,"MSC Industrial Direct Co., Inc.",Industrial Distribution,United States,Industrials,US5535301064
1386 | SITM,SiTime Corporation,Semiconductors,United States,Technology,US82982T1060
1387 | IDCC,"InterDigital, Inc.",Software - Application,United States,Technology,US45867G1013
1388 | KRYS,"Krystal Biotech, Inc.",Biotechnology,United States,Healthcare,US5011471027
1389 | MATX,"Matson, Inc.",Marine Shipping,United States,Industrials,US57686G1058
1390 | AB,AllianceBernstein Holding L.P.,Asset Management,United States,Financials,US01881G1067
1391 | TGS,Transportadora de Gas del Sur S.A.,Oil & Gas Integrated,Argentina,Energy,US8938702045
1392 | AVT,"Avnet, Inc.",Electronics & Computer Distribution,United States,Technology,US0538071038
1393 | CNS,"Cohen & Steers, Inc.",Asset Management,United States,Financials,US19247A1007
1394 | FUN,Six Flags Entertainment Corporation,Leisure,United States,Consumer Discretionary,US1501851067
1395 | SM,SM Energy Company,Oil & Gas Exploration & Production,United States,Energy,US78454L1008
1396 | KAI,Kadant Inc.,Specialty Industrial Machinery,United States,Industrials,US48282T1043
1397 | FELE,"Franklin Electric Co., Inc.",Specialty Industrial Machinery,United States,Industrials,US3535141028
1398 | IPAR,"Interparfums, Inc.",Household & Personal Products,United States,Consumer Staples,US4583341098
1399 | BC,Brunswick Corporation,Recreational Vehicles,United States,Consumer Discretionary,US1170431092
1400 | BGC,"BGC Group, Inc.",Capital Markets,United States,Financials,US0889291045
1401 | ABCB,Ameris Bancorp,Banks - Regional,United States,Financials,US03076K1088
1402 | ROAD,"Construction Partners, Inc.",Engineering & Construction,United States,Industrials,US21044C1071
1403 | VRRM,Verra Mobility Corporation,Infrastructure Operations,United States,Industrials,US92511U1025
1404 | SANM,Sanmina Corporation,Electronic Components,United States,Technology,US8010561020
1405 | POR,Portland General Electric Company,Utilities - Regulated Electric,United States,Utilities,US7365088472
1406 | IRT,"Independence Realty Trust, Inc.",REIT - Residential,United States,Real Estate,US45378A1060
1407 | MMS,"Maximus, Inc.",Specialty Business Services,United States,Industrials,US5779331041
1408 | VRNA,Verona Pharma plc,Biotechnology,United Kingdom,Healthcare,US9250501064
1409 | SMG,The Scotts Miracle-Gro Company,Agricultural Inputs,United States,Materials,US8101861065
1410 | M,"Macy's, Inc.",Department Stores,United States,Consumer Discretionary,US55616P1049
1411 | NWL,Newell Brands Inc.,Household & Personal Products,United States,Consumer Staples,US6512291062
1412 | SLAB,Silicon Laboratories Inc.,Semiconductors,United States,Technology,US8269191024
1413 | EEFT,"Euronet Worldwide, Inc.",Software - Infrastructure,United States,Technology,US2987361092
1414 | AEIS,"Advanced Energy Industries, Inc.",Electrical Equipment & Parts,United States,Industrials,US0079731008
1415 | LBTYB,Liberty Global Ltd.,Telecom Services,Bermuda,Communication Services,BMG611881191
1416 | LBTYK,Liberty Global Ltd.,Telecom Services,Bermuda,Communication Services,BMG611881274
1417 | VCTR,"Victory Capital Holdings, Inc.",Asset Management,United States,Financials,US92645B1035
1418 | STRL,"Sterling Infrastructure, Inc.",Engineering & Construction,United States,Industrials,US8592411016
1419 | ZETA,Zeta Global Holdings Corp.,Software - Infrastructure,United States,Technology,US98956A1051
1420 | CBZ,"CBIZ, Inc.",Specialty Business Services,United States,Industrials,US1248051021
1421 | GDS,GDS Holdings Limited,Information Technology Services,China,Technology,US36165L1089
1422 | KMPR,Kemper Corporation,Insurance - Property & Casualty,United States,Financials,US4884011002
1423 | TXNM,"TXNM Energy, Inc.",Utilities - Regulated Electric,United States,Utilities,US69349H1077
1424 | IESC,"IES Holdings, Inc.",Engineering & Construction,United States,Industrials,US44951W1062
1425 | AI,"C3.ai, Inc.",Software - Application,United States,Technology,US12468P1049
1426 | MUR,Murphy Oil Corporation,Oil & Gas Exploration & Production,United States,Energy,US6267171022
1427 | LBTYA,Liberty Global Ltd.,Telecom Services,Bermuda,Communication Services,BMG611881019
1428 | GBTG,"Global Business Travel Group, Inc.",Software - Application,United States,Technology,US37890B1008
1429 | BKH,Black Hills Corporation,Utilities - Regulated Gas,United States,Utilities,US0921131092
1430 | CARG,"CarGurus, Inc.",Auto & Truck Dealerships,United States,Consumer Discretionary,US1417881091
1431 | ST,Sensata Technologies Holding plc,Scientific & Technical Instruments,United States,Technology,GB00BFMBMT84
1432 | RXO,"RXO, Inc.",Trucking,United States,Industrials,US74982T1034
1433 | KGS,"Kodiak Gas Services, Inc.",Oil & Gas Equipment & Services,United States,Energy,US50012A1088
1434 | OKLO,Oklo Inc.,Utilities - Regulated Electric,United States,Utilities,US02156V1098
1435 | GBDC,"Golub Capital BDC, Inc.",Asset Management,United States,Financials,US38173M1027
1436 | UNF,UniFirst Corporation,Specialty Business Services,United States,Industrials,US9047081040
1437 | ICUI,"ICU Medical, Inc.",Medical Instruments & Supplies,United States,Healthcare,US44930G1076
1438 | IBOC,International Bancshares Corporation,Banks - Regional,United States,Financials,US4590441030
1439 | CNX,CNX Resources Corporation,Oil & Gas Exploration & Production,United States,Energy,US12653C1080
1440 | HGV,Hilton Grand Vacations Inc.,Resorts & Casinos,United States,Consumer Discretionary,US43283X1054
1441 | OGN,Organon & Co.,Drug Manufacturers - General,United States,Healthcare,US68622V1061
1442 | BCO,The Brink's Company,Security & Protection Services,United States,Industrials,US1096961040
1443 | AX,"Axos Financial, Inc.",Banks - Regional,United States,Financials,US05465C1009
1444 | FLO,"Flowers Foods, Inc.",Packaged Foods,United States,Consumer Staples,US3434981011
1445 | ASGN,ASGN Incorporated,Information Technology Services,United States,Technology,US00191U1025
1446 | COMP,"Compass, Inc.",Real Estate Services,United States,Real Estate,US20464U1007
1447 | CNO,"CNO Financial Group, Inc.",Insurance - Life,United States,Financials,US12621E1038
1448 | GOLF,Acushnet Holdings Corp.,Leisure,United States,Consumer Discretionary,US0050981085
1449 | GEO,"The GEO Group, Inc.",Security & Protection Services,United States,Industrials,US36162J1060
1450 | ALGM,"Allegro MicroSystems, Inc.",Semiconductors,United States,Technology,US01749D1054
1451 | SR,Spire Inc.,Utilities - Regulated Gas,United States,Utilities,US84857L1017
1452 | DORM,"Dorman Products, Inc.",Auto Parts,United States,Consumer Discretionary,US2582781009
1453 | ENIC,Enel Chile S.A.,Utilities - Regulated Electric,Chile,Utilities,US29278D1054
1454 | GLNG,Golar LNG Limited,Oil & Gas Midstream,Bermuda,Energy,BMG9456A1009
1455 | TDS,"Telephone and Data Systems, Inc.",Telecom Services,United States,Communication Services,US8794338298
1456 | BL,"BlackLine, Inc.",Software - Application,United States,Technology,US09239B1098
1457 | SGHC,Super Group (SGHC) Limited,Gambling,Guernsey,Consumer Discretionary,GG00BMG42V42
1458 | SPR,"Spirit AeroSystems Holdings, Inc.",Aerospace & Defense,United States,Industrials,US8485741099
1459 | ACHC,"Acadia Healthcare Company, Inc.",Medical Care Facilities,United States,Healthcare,US00404A1097
1460 | ASB,Associated Banc-Corp,Banks - Regional,United States,Financials,US0454871056
1461 | NCNO,"nCino, Inc.",Software - Application,United States,Technology,US63947X1019
1462 | NNI,"Nelnet, Inc.",Credit Services,United States,Financials,US64031N1081
1463 | SBRA,"Sabra Health Care REIT, Inc.",REIT - Healthcare Facilities,United States,Real Estate,US78573L1061
1464 | OSCR,"Oscar Health, Inc.",Healthcare Plans,United States,Healthcare,US6877931096
1465 | UCB,"United Community Banks, Inc.",Banks - Regional,United States,Financials,US90984P3038
1466 | PYCR,"Paycor HCM, Inc.",Software - Application,United States,Technology,US70435P1021
1467 | GSHD,"Goosehead Insurance, Inc",Insurance - Diversified,United States,Financials,US38267D1090
1468 | FLG,"Flagstar Financial, Inc.",Banks - Regional,United States,Financials,US6494454001
1469 | NFE,New Fortress Energy Inc.,Utilities - Regulated Gas,United States,Utilities,US6443931000
1470 | JWN,"Nordstrom, Inc.",Department Stores,United States,Consumer Discretionary,US6556641008
1471 | WRD,WeRide Inc.,Auto Manufacturers,China,Consumer Discretionary,US94859U1034
1472 | FROG,JFrog Ltd.,Software - Application,United States,Technology,IL0011684185
1473 | FIZZ,National Beverage Corp.,Beverages - Non-Alcoholic,United States,Consumer Staples,US6350171061
1474 | RYN,Rayonier Inc.,REIT - Specialty,United States,Real Estate,US7549071030
1475 | BANF,BancFirst Corporation,Banks - Regional,United States,Financials,US05945F1030
1476 | SRRK,Scholar Rock Holding Corporation,Biotechnology,United States,Healthcare,US80706P1030
1477 | OGS,"ONE Gas, Inc.",Utilities - Regulated Gas,United States,Utilities,US68235P1084
1478 | BTSG,"BrightSpring Health Services, Inc.",Health Information Services,United States,Healthcare,US10950A1060
1479 | GHC,Graham Holdings Company,Education & Training Services,United States,Consumer Staples,US3846371041
1480 | CLVT,Clarivate Plc,Information Technology Services,United Kingdom,Technology,JE00BJJN4441
1481 | PRCT,PROCEPT BioRobotics Corporation,Medical Devices,United States,Healthcare,US74276L1052
1482 | RARE,Ultragenyx Pharmaceutical Inc.,Biotechnology,United States,Healthcare,US90400D1081
1483 | PBH,Prestige Consumer Healthcare Inc.,Drug Manufacturers - Specialty & Generic,United States,Healthcare,US74112D1019
1484 | CAMT,Camtek Ltd.,Semiconductor Equipment & Materials,Israel,Technology,IL0010952641
1485 | CRGY,Crescent Energy Company,Oil & Gas Integrated,United States,Energy,US44952J1043
1486 | PLXS,Plexus Corp.,Electronic Components,United States,Technology,US7291321005
1487 | AVNT,Avient Corporation,Specialty Chemicals,United States,Materials,US05368V1061
1488 | XRAY,DENTSPLY SIRONA Inc.,Medical Instruments & Supplies,United States,Healthcare,US24906P1093
1489 | SHC,Sotera Health Company,Diagnostics & Research,United States,Healthcare,US83601L1026
1490 | PRIM,Primoris Services Corporation,Engineering & Construction,United States,Industrials,US74164F1030
1491 | BHVN,Biohaven Ltd.,Biotechnology,United States,Healthcare,VGG1110E1079
1492 | DXC,DXC Technology Company,Information Technology Services,United States,Technology,US23355L1061
1493 | DOCN,"DigitalOcean Holdings, Inc.",Software - Infrastructure,United States,Technology,US25402D1028
1494 | CPA,"Copa Holdings, S.A.",Airlines,Panama,Industrials,PAP310761054
1495 | SMPL,The Simply Good Foods Company,Packaged Foods,United States,Consumer Staples,US82900L1026
1496 | SIM,"Grupo Simec, S.A.B. de C.V.",Steel,Mexico,Materials,US4004911065
1497 | ALVO,Alvotech,Drug Manufacturers - Specialty & Generic,Luxembourg,Healthcare,LU2458332611
1498 | BLKB,"Blackbaud, Inc.",Software - Application,United States,Technology,US09227Q1004
1499 | ASO,"Academy Sports and Outdoors, Inc.",Specialty Retail,United States,Consumer Discretionary,US00402L1070
1500 | SKT,Tanger Inc.,REIT - Retail,United States,Real Estate,US8754651060
1501 | ENS,EnerSys,Electrical Equipment & Parts,United States,Industrials,US29275Y1029
1502 | RNA,"Avidity Biosciences, Inc.",Biotechnology,United States,Healthcare,US05370A1088
1503 | VKTX,"Viking Therapeutics, Inc.",Biotechnology,United States,Healthcare,US92686J1060
1504 | CVCO,"Cavco Industries, Inc.",Residential Construction,United States,Consumer Discretionary,US1495681074
1505 | ADMA,"ADMA Biologics, Inc.",Biotechnology,United States,Healthcare,US0008991046
1506 | NPO,Enpro Inc.,Specialty Industrial Machinery,United States,Industrials,US29355X1072
1507 | OLN,Olin Corporation,Chemicals,United States,Materials,US6806652052
1508 | OMAB,"Grupo Aeroportuario del Centro Norte, S.A.B. de C.V.",Airports & Air Services,Mexico,Industrials,US4005011022
1509 | ALE,"ALLETE, Inc.",Utilities - Diversified,United States,Utilities,US0185223007
1510 | PAY,"Paymentus Holdings, Inc.",Software - Infrastructure,United States,Technology,US70439P1084
1511 | ATAT,Atour Lifestyle Holdings Limited,Lodging,China,Consumer Discretionary,US04965M1062
1512 | ORA,"Ormat Technologies, Inc.",Utilities - Renewable,United States,Utilities,US6866881021
1513 | APLE,"Apple Hospitality REIT, Inc.",REIT - Hotel & Motel,United States,Real Estate,US03784Y2000
1514 | HHH,Howard Hughes Holdings Inc.,Real Estate - Diversified,United States,Real Estate,US44267T1025
1515 | PI,"Impinj, Inc.",Semiconductors,United States,Technology,US4532041096
1516 | PAYO,Payoneer Global Inc.,Software - Infrastructure,United States,Technology,US70451X1046
1517 | NVST,Envista Holdings Corporation,Medical Instruments & Supplies,United States,Healthcare,US29415F1049
1518 | IMVT,"Immunovant, Inc.",Biotechnology,United States,Healthcare,US45258J1025
1519 | GVA,Granite Construction Incorporated,Engineering & Construction,United States,Industrials,US3873281071
1520 | TNL,Travel + Leisure Co.,Travel Services,United States,Consumer Discretionary,US8941641024
1521 | FULT,Fulton Financial Corporation,Banks - Regional,United States,Financials,US3602711000
1522 | ALIT,"Alight, Inc.",Software - Application,United States,Technology,US01626W1018
1523 | NOG,"Northern Oil and Gas, Inc.",Oil & Gas Exploration & Production,United States,Energy,US6655313079
1524 | GFF,Griffon Corporation,Conglomerates,United States,Industrials,US3984331021
1525 | DOOO,BRP Inc.,Recreational Vehicles,Canada,Consumer Discretionary,CA05577W2004
1526 | KFY,Korn Ferry,Staffing & Employment Services,United States,Industrials,US5006432000
1527 | IAC,IAC Inc.,Internet Content & Information,United States,Communication Services,US44891N2080
1528 | MHO,"M/I Homes, Inc.",Residential Construction,United States,Consumer Discretionary,US55305B1017
1529 | TGLS,Tecnoglass Inc.,Building Materials,Colombia,Materials,KYG872641009
1530 | SG,"Sweetgreen, Inc.",Restaurants,United States,Consumer Discretionary,US87043Q1085
1531 | ATGE,Adtalem Global Education Inc.,Education & Training Services,United States,Consumer Staples,US00737L1035
1532 | RGTI,"Rigetti Computing, Inc.",Computer Hardware,United States,Technology,US76655K1034
1533 | EBC,"Eastern Bankshares, Inc.",Banks - Regional,United States,Financials,US27627N1054
1534 | FRO,Frontline plc,Oil & Gas Midstream,Cyprus,Energy,CY0200352116
1535 | CXT,"Crane NXT, Co.",Specialty Industrial Machinery,United States,Industrials,US2244411052
1536 | APLS,"Apellis Pharmaceuticals, Inc.",Biotechnology,United States,Healthcare,US03753U1060
1537 | RIOT,"Riot Platforms, Inc.",Capital Markets,United States,Financials,US7672921050
1538 | MWA,"Mueller Water Products, Inc.",Specialty Industrial Machinery,United States,Industrials,US6247581084
1539 | BRC,Brady Corporation,Security & Protection Services,United States,Industrials,US1046741062
1540 | GSAT,"Globalstar, Inc.",Telecom Services,United States,Communication Services,US3789734080
1541 | MDU,"MDU Resources Group, Inc.",Conglomerates,United States,Industrials,US5526901096
1542 | ALKT,"Alkami Technology, Inc.",Software - Application,United States,Technology,US01644J1088
1543 | ZI,ZoomInfo Technologies Inc.,Software - Application,United States,Technology,US98980F1049
1544 | DLO,DLocal Limited,Software - Infrastructure,Uruguay,Technology,KYG290181018
1545 | TCBI,"Texas Capital Bancshares, Inc.",Banks - Regional,United States,Financials,US88224Q1076
1546 | NXE,NexGen Energy Ltd.,Uranium,Canada,Energy,CA65340P1062
1547 | AKRO,"Akero Therapeutics, Inc.",Biotechnology,United States,Healthcare,US00973Y1082
1548 | CNXC,Concentrix Corporation,Information Technology Services,United States,Technology,US20602D1019
1549 | APAM,Artisan Partners Asset Management Inc.,Asset Management,United States,Financials,US04316A1088
1550 | RUM,Rumble Inc.,Software - Application,United States,Technology,US78137L1052
1551 | ACVA,ACV Auctions Inc.,Auto & Truck Dealerships,United States,Consumer Discretionary,US00091G1040
1552 | DEI,"Douglas Emmett, Inc.",REIT - Office,United States,Real Estate,US25960P1093
1553 | CRSP,CRISPR Therapeutics AG,Biotechnology,Switzerland,Healthcare,CH0334081137
1554 | BEPC,Brookfield Renewable Corporation,Utilities - Renewable,United States,Utilities,CA11284V1058
1555 | EPR,EPR Properties,REIT - Specialty,United States,Real Estate,US26884U1097
1556 | ARLP,"Alliance Resource Partners, L.P.",Thermal Coal,United States,Energy,US01877R1086
1557 | TFSL,TFS Financial Corporation,Banks - Regional,United States,Financials,US87240R1077
1558 | CRNX,"Crinetics Pharmaceuticals, Inc.",Biotechnology,United States,Healthcare,US22663K1079
1559 | CCOI,"Cogent Communications Holdings, Inc.",Telecom Services,United States,Communication Services,US19239V3024
1560 | LIF,"Life360, Inc.",Software - Application,United States,Technology,
1561 | TPH,"Tri Pointe Homes, Inc.",Residential Construction,United States,Consumer Discretionary,US87265H1095
1562 | IRTC,"iRhythm Technologies, Inc.",Medical Devices,United States,Healthcare,US4500561067
1563 | UAA,"Under Armour, Inc.",Apparel Manufacturing,United States,Consumer Discretionary,US9043111072
1564 | DV,"DoubleVerify Holdings, Inc.",Software - Application,United States,Technology,US25862V1052
1565 | HOG,"Harley-Davidson, Inc.",Recreational Vehicles,United States,Consumer Discretionary,US4128221086
1566 | RYTM,"Rhythm Pharmaceuticals, Inc.",Biotechnology,United States,Healthcare,US76243J1051
1567 | OR,Osisko Gold Royalties Ltd,Gold,Canada,Materials,CA68827L1013
1568 | SNEX,StoneX Group Inc.,Capital Markets,United States,Financials,US8618961085
1569 | PTCT,"PTC Therapeutics, Inc.",Biotechnology,United States,Healthcare,US69366J2006
1570 | ATMU,Atmus Filtration Technologies Inc.,Pollution & Treatment Controls,United States,Industrials,US04956D1072
1571 | ATHM,Autohome Inc.,Internet Content & Information,China,Communication Services,US05278C1071
1572 | FIBK,"First Interstate BancSystem, Inc.",Banks - Regional,United States,Financials,US32055Y2019
1573 | ACLX,"Arcellx, Inc.",Biotechnology,United States,Healthcare,US03940C1009
1574 | HTGC,"Hercules Capital, Inc.",Asset Management,United States,Financials,US4270965084
1575 | WU,The Western Union Company,Credit Services,United States,Financials,US9598021098
1576 | AVPT,"AvePoint, Inc.",Software - Infrastructure,United States,Technology,US0536041041
1577 | ECG,"Everus Construction Group, Inc.",Engineering & Construction,United States,Industrials,US3004261034
1578 | BHF,"Brighthouse Financial, Inc.",Insurance - Life,United States,Financials,US10922N1037
1579 | HAE,Haemonetics Corporation,Medical Instruments & Supplies,United States,Healthcare,US4050241003
1580 | CNK,"Cinemark Holdings, Inc.",Entertainment,United States,Communication Services,US17243V1026
1581 | IGT,International Game Technology PLC,Gambling,United Kingdom,Consumer Discretionary,GB00BVG7F061
1582 | RIG,Transocean Ltd.,Oil & Gas Drilling,Switzerland,Energy,CH0048265513
1583 | CBU,"Community Financial System, Inc.",Banks - Regional,United States,Financials,US2036071064
1584 | FUL,H.B. Fuller Company,Specialty Chemicals,United States,Materials,US3596941068
1585 | PBF,PBF Energy Inc.,Oil & Gas Refining & Marketing,United States,Energy,US69318G1067
1586 | IRDM,Iridium Communications Inc.,Telecom Services,United States,Communication Services,US46269C1027
1587 | IAG,IAMGOLD Corporation,Gold,Canada,Materials,CA4509131088
1588 | AQN,Algonquin Power & Utilities Corp.,Utilities - Renewable,Canada,Utilities,CA0158571053
1589 | FHB,"First Hawaiian, Inc.",Banks - Regional,United States,Financials,US32051X1081
1590 | MP,MP Materials Corp.,Other Industrial Metals & Mining,United States,Materials,US5533681012
1591 | NMRK,"Newmark Group, Inc.",Real Estate Services,United States,Real Estate,US65158N1028
1592 | TBBB,BBB Foods Inc.,Discount Stores,Mexico,Consumer Staples,VGG0896C1032
1593 | HL,Hecla Mining Company,Other Precious Metals & Mining,United States,Materials,US4227041062
1594 | FBP,First BanCorp.,Banks - Regional,United States,Financials,PR3186727065
1595 | VCYT,"Veracyte, Inc.",Diagnostics & Research,United States,Healthcare,US92337F1075
1596 | DNLI,Denali Therapeutics Inc.,Biotechnology,United States,Healthcare,US24823R1059
1597 | PRGO,Perrigo Company plc,Drug Manufacturers - Specialty & Generic,Ireland,Healthcare,IE00BGH1M568
1598 | VAL,Valaris Limited,Oil & Gas Equipment & Services,Bermuda,Energy,BMG9460G1015
1599 | ESE,ESCO Technologies Inc.,Scientific & Technical Instruments,United States,Technology,US2963151046
1600 | AUB,Atlantic Union Bankshares Corporation,Banks - Regional,United States,Financials,US04911A1079
1601 | CDP,COPT Defense Properties,REIT - Office,United States,Real Estate,US22002T1088
1602 | ASH,Ashland Inc.,Specialty Chemicals,United States,Materials,US0441861046
1603 | REZI,"Resideo Technologies, Inc.",Industrial Distribution,United States,Industrials,US76118Y1047
1604 | YOU,"Clear Secure, Inc.",Software - Application,United States,Technology,US18467V1098
1605 | CATY,Cathay General Bancorp,Banks - Regional,United States,Financials,US1491501045
1606 | UA,"Under Armour, Inc.",Apparel Manufacturing,United States,Consumer Discretionary,US9043112062
1607 | POWI,"Power Integrations, Inc.",Semiconductors,United States,Technology,US7392761034
1608 | PCH,PotlatchDeltic Corporation,REIT - Specialty,United States,Real Estate,US7376301039
1609 | IFS,Intercorp Financial Services Inc.,Banks - Regional,Peru,Financials,PAL2400671A3
1610 | HGTY,"Hagerty, Inc.",Insurance - Property & Casualty,United States,Financials,US4051661092
1611 | NWE,"NorthWestern Energy Group, Inc.",Utilities - Regulated Electric,United States,Utilities,US6680743050
1612 | HP,"Helmerich & Payne, Inc.",Oil & Gas Drilling,United States,Energy,US4234521015
1613 | GMS,GMS Inc.,Building Products & Equipment,United States,Industrials,US36251C1036
1614 | MEOH,Methanex Corporation,Chemicals,Canada,Materials,CA59151K1084
1615 | OSIS,"OSI Systems, Inc.",Electronic Components,United States,Technology,US6710441055
1616 | ABM,ABM Industries Incorporated,Specialty Business Services,United States,Industrials,US0009571003
1617 | USLM,"United States Lime & Minerals, Inc.",Building Materials,United States,Materials,US9119221029
1618 | LBRT,Liberty Energy Inc.,Oil & Gas Equipment & Services,United States,Energy,US53115L1044
1619 | HASI,"HA Sustainable Infrastructure Capital, Inc.",Real Estate Services,United States,Real Estate,US41068X1000
1620 | RNG,"RingCentral, Inc.",Software - Application,United States,Technology,US76680R2067
1621 | SLVM,Sylvamo Corporation,Paper & Paper Products,United States,Materials,US8713321029
1622 | WSFS,WSFS Financial Corporation,Banks - Regional,United States,Financials,US9293281021
1623 | HAYW,"Hayward Holdings, Inc.",Electrical Equipment & Parts,United States,Industrials,US4212981009
1624 | SGRY,"Surgery Partners, Inc.",Medical Care Facilities,United States,Healthcare,US86881A1007
1625 | FA,First Advantage Corporation,Specialty Business Services,United States,Industrials,US31846B1089
1626 | LUNR,"Intuitive Machines, Inc.",Aerospace & Defense,United States,Industrials,US46125A1007
1627 | WRBY,Warby Parker Inc.,Medical Instruments & Supplies,United States,Healthcare,US93403J1060
1628 | WD,"Walker & Dunlop, Inc.",Mortgage Finance,United States,Financials,US93148P1021
1629 | CAR,"Avis Budget Group, Inc.",Rental & Leasing Services,United States,Industrials,US0537741052
1630 | PTEN,"Patterson-UTI Energy, Inc.",Oil & Gas Drilling,United States,Energy,US7034811015
1631 | OTTR,Otter Tail Corporation,Utilities - Diversified,United States,Utilities,US6896481032
1632 | PATK,"Patrick Industries, Inc.","Furnishings, Fixtures & Appliances",United States,Consumer Discretionary,US7033431039
1633 | SXT,Sensient Technologies Corporation,Specialty Chemicals,United States,Materials,US81725T1007
1634 | HEES,"H&E Equipment Services, Inc.",Rental & Leasing Services,United States,Industrials,US4040301081
1635 | EE,"Excelerate Energy, Inc.",Oil & Gas Midstream,United States,Energy,US30069T1016
1636 | RSI,"Rush Street Interactive, Inc.",Gambling,United States,Consumer Discretionary,US7820111000
1637 | GPOR,Gulfport Energy Corporation,Oil & Gas Exploration & Production,United States,Energy,US4026355028
1638 | WDFC,WD-40 Company,Specialty Chemicals,United States,Materials,US9292361071
1639 | BUR,Burford Capital Limited,Asset Management,Guernsey,Financials,GG00BMGYLN96
1640 | AEO,"American Eagle Outfitters, Inc.",Apparel Retail,United States,Consumer Discretionary,US02553E1064
1641 | PTVE,Pactiv Evergreen Inc.,Packaging & Containers,United States,Consumer Discretionary,US69526K1051
1642 | YETI,"YETI Holdings, Inc.",Leisure,United States,Consumer Discretionary,US98585X1046
1643 | MGEE,"MGE Energy, Inc.",Utilities - Regulated Electric,United States,Utilities,US55277P1049
1644 | VEON,VEON Ltd.,Telecom Services,Netherlands,Communication Services,US91822M5022
1645 | BNL,"Broadstone Net Lease, Inc.",REIT - Diversified,United States,Real Estate,US11135E2037
1646 | STR,Sitio Royalties Corp.,Oil & Gas Exploration & Production,United States,Energy,US82983N1081
1647 | TFPM,Triple Flag Precious Metals Corp.,Other Precious Metals & Mining,Canada,Materials,CA89679M1041
1648 | GRND,Grindr Inc.,Software - Application,United States,Technology,US39854F1012
1649 | PTON,"Peloton Interactive, Inc.",Leisure,United States,Consumer Discretionary,US70614W1009
1650 | LPL,"LG Display Co., Ltd.",Consumer Electronics,South Korea,Technology,US50186V1026
1651 | TAC,TransAlta Corporation,Utilities - Independent Power Producers,Canada,Utilities,CA89346D1078
1652 | HIW,"Highwoods Properties, Inc.",REIT - Office,United States,Real Estate,US4312841087
1653 | NHI,"National Health Investors, Inc.",REIT - Healthcare Facilities,United States,Real Estate,US63633D1046
1654 | CORZ,"Core Scientific, Inc.",Software - Infrastructure,United States,Technology,US21873J1088
1655 | HBM,Hudbay Minerals Inc.,Copper,Canada,Materials,CA4436281022
1656 | SYNA,Synaptics Incorporated,Semiconductors,United States,Technology,US87157D1090
1657 | VRN,Veren Inc.,Oil & Gas Exploration & Production,Canada,Energy,CA92340V1076
1658 | BVN,Compañía de Minas Buenaventura S.A.A.,Other Precious Metals & Mining,Peru,Materials,US2044481040
1659 | TEX,Terex Corporation,Farm & Heavy Construction Machinery,United States,Industrials,US8807791038
1660 | CWK,Cushman & Wakefield plc,Real Estate Services,United Kingdom,Real Estate,GB00BFZ4N465
1661 | BTG,B2Gold Corp.,Gold,Canada,Materials,CA11777Q2099
1662 | CAAP,Corporación América Airports S.A.,Airports & Air Services,Luxembourg,Industrials,LU1756447840
1663 | TDC,Teradata Corporation,Software - Infrastructure,United States,Technology,US88076W1036
1664 | BFH,"Bread Financial Holdings, Inc.",Credit Services,United States,Financials,US0185811082
1665 | BXMT,"Blackstone Mortgage Trust, Inc.",REIT - Mortgage,United States,Real Estate,US09257W1009
1666 | LFST,"LifeStance Health Group, Inc.",Medical Care Facilities,United States,Healthcare,US53228F1012
1667 | BSM,"Black Stone Minerals, L.P.",Oil & Gas Exploration & Production,United States,Energy,US09225M1018
1668 | FIVN,"Five9, Inc.",Software - Infrastructure,United States,Technology,US3383071012
1669 | TRN,"Trinity Industries, Inc.",Railroads,United States,Industrials,US8965221091
1670 | GNW,"Genworth Financial, Inc.",Insurance - Life,United States,Financials,US37247D1063
1671 | EGO,Eldorado Gold Corporation,Gold,Canada,Materials,CA2849025093
1672 | TWST,Twist Bioscience Corporation,Diagnostics & Research,United States,Healthcare,US90184D1000
1673 | NMIH,"NMI Holdings, Inc.",Insurance - Specialty,United States,Financials,US6292093050
1674 | ALRM,"Alarm.com Holdings, Inc.",Software - Application,United States,Technology,US0116421050
1675 | IPGP,IPG Photonics Corporation,Semiconductor Equipment & Materials,United States,Technology,US44980X1090
1676 | QDEL,QuidelOrtho Corporation,Medical Devices,United States,Healthcare,US2197981051
1677 | FHI,"Federated Hermes, Inc.",Asset Management,United States,Financials,US3142111034
1678 | AMBA,"Ambarella, Inc.",Semiconductor Equipment & Materials,United States,Technology,KYG037AX1015
1679 | ACAD,ACADIA Pharmaceuticals Inc.,Biotechnology,United States,Healthcare,US0042251084
1680 | VAC,Marriott Vacations Worldwide Corporation,Resorts & Casinos,United States,Consumer Discretionary,US57164Y1073
1681 | BKU,"BankUnited, Inc.",Banks - Regional,United States,Financials,US06652K1034
1682 | XENE,Xenon Pharmaceuticals Inc.,Biotechnology,Canada,Healthcare,CA98420N1050
1683 | MIR,"Mirion Technologies, Inc.",Specialty Industrial Machinery,United States,Industrials,US60471A1016
1684 | OUT,OUTFRONT Media Inc.,REIT - Specialty,United States,Real Estate,US69007J1060
1685 | PENN,"PENN Entertainment, Inc.",Resorts & Casinos,United States,Consumer Discretionary,US7075691094
1686 | UGP,Ultrapar Participações S.A.,Oil & Gas Refining & Marketing,Brazil,Energy,US90400P1012
1687 | HUN,Huntsman Corporation,Chemicals,United States,Materials,US4470111075
1688 | AMED,"Amedisys, Inc.",Medical Care Facilities,United States,Healthcare,US0234361089
1689 | CPRI,Capri Holdings Limited,Luxury Goods,United Kingdom,Consumer Discretionary,VGG1890L1076
1690 | MGRC,McGrath RentCorp,Rental & Leasing Services,United States,Industrials,US5805891091
1691 | BOH,Bank of Hawaii Corporation,Banks - Regional,United States,Financials,US0625401098
1692 | SHOO,"Steven Madden, Ltd.",Footwear & Accessories,United States,Consumer Discretionary,US5562691080
1693 | NSP,"Insperity, Inc.",Staffing & Employment Services,United States,Industrials,US45778Q1076
1694 | CON,"Concentra Group Holdings Parent, Inc.",Medical Care Facilities,United States,Healthcare,US20603L1026
1695 | VSCO,Victoria's Secret & Co.,Apparel Retail,United States,Consumer Discretionary,US9264001028
1696 | WEN,The Wendy's Company,Restaurants,United States,Consumer Discretionary,US95058W1009
1697 | GEF.B,"Greif, Inc.",Packaging & Containers,United States,Consumer Discretionary,US3976242061
1698 | VCEL,Vericel Corporation,Biotechnology,United States,Healthcare,US92346J1088
1699 | CWEN,"Clearway Energy, Inc.",Utilities - Renewable,United States,Utilities,US18539C2044
1700 | ENVA,"Enova International, Inc.",Credit Services,United States,Financials,US29357K1034
1701 | USAC,"USA Compression Partners, LP",Oil & Gas Equipment & Services,United States,Energy,US90290N1090
1702 | UEC,Uranium Energy Corp.,Uranium,United States,Energy,US9168961038
1703 | FORM,"FormFactor, Inc.",Semiconductor Equipment & Materials,United States,Technology,US3463751087
1704 | HBI,Hanesbrands Inc.,Apparel Manufacturing,United States,Consumer Discretionary,US4103451021
1705 | RXRX,"Recursion Pharmaceuticals, Inc.",Biotechnology,United States,Healthcare,US75629V1044
1706 | TGNA,TEGNA Inc.,Broadcasting,United States,Communication Services,US87901J1051
1707 | CVBF,CVB Financial Corp.,Banks - Regional,United States,Financials,US1266001056
1708 | ALHC,"Alignment Healthcare, Inc.",Healthcare Plans,United States,Healthcare,US01625V1044
1709 | GEF,"Greif, Inc.",Packaging & Containers,United States,Consumer Discretionary,US3976241071
1710 | ZLAB,Zai Lab Limited,Biotechnology,China,Healthcare,US98887Q1040
1711 | AAP,"Advance Auto Parts, Inc.",Specialty Retail,United States,Consumer Discretionary,US00751Y1064
[TRUNCATED]
```

src/company_names_tickers_news.csv
```
1 | Industry,Company Name,Symbol,Country,Sector,ISIN Number
2 | Consumer Electronics,Apple Inc.,AAPL,United States,Technology,US0378331005
3 | Software - Infrastructure,Microsoft Corporation,MSFT,United States,Technology,US5949181045
4 | Semiconductors,NVIDIA Corporation,NVDA,United States,Technology,US67066G1040
5 | Internet Retail,"Amazon.com, Inc.",AMZN,United States,Consumer Discretionary,US0231351067
6 | Internet Content & Information,Alphabet Inc.,GOOG,United States,Communication Services,US02079K1079
7 | Internet Content & Information,Alphabet Inc.,GOOGL,United States,Communication Services,US02079K3059
8 | Internet Content & Information,"Meta Platforms, Inc.",META,United States,Communication Services,US30303M1027
9 | Auto Manufacturers,"Tesla, Inc.",TSLA,United States,Consumer Discretionary,US88160R1014
10 | Insurance - Diversified,Berkshire Hathaway Inc.,BRK.A,United States,Financials,US0846701086
11 | Insurance - Diversified,Berkshire Hathaway Inc.,BRK.B,United States,Financials,US0846707026
12 | Semiconductors,Broadcom Inc.,AVGO,United States,Technology,US11135F1012
13 | Semiconductors,Taiwan Semiconductor Manufacturing Company Limited,TSM,Taiwan,Technology,US8740391003
14 | Discount Stores,Walmart Inc.,WMT,United States,Consumer Staples,US9311421039
15 | Banks - Diversified,JPMorgan Chase & Co.,JPM,United States,Financials,US46625H1005
16 | Drug Manufacturers - General,Eli Lilly and Company,LLY,United States,Healthcare,US5324571083
17 | Credit Services,Visa Inc.,V,United States,Financials,US92826C8394
18 | Credit Services,Mastercard Incorporated,MA,United States,Financials,US57636Q1040
19 | Healthcare Plans,UnitedHealth Group Incorporated,UNH,United States,Healthcare,US91324P1021
20 | Oil & Gas Integrated,Exxon Mobil Corporation,XOM,United States,Energy,US30231G1022
21 | Software - Infrastructure,Oracle Corporation,ORCL,United States,Technology,US68389X1054
22 | Discount Stores,Costco Wholesale Corporation,COST,United States,Consumer Staples,US22160K1051
23 | Home Improvement Retail,"The Home Depot, Inc.",HD,United States,Consumer Discretionary,US4370761029
24 | Entertainment,"Netflix, Inc.",NFLX,United States,Communication Services,US64110L1061
25 | Household & Personal Products,The Procter & Gamble Company,PG,United States,Consumer Staples,US7427181091
26 | Drug Manufacturers - General,Novo Nordisk A/S,NVO,Denmark,Healthcare,US6701002056
27 | Drug Manufacturers - General,Johnson & Johnson,JNJ,United States,Healthcare,US4781601046
28 | Banks - Diversified,Bank of America Corporation,BAC,United States,Financials,US0605051046
29 | Software - Application,"Salesforce, Inc.",CRM,United States,Technology,US79466L3024
30 | Software - Application,SAP SE,SAP,Germany,Technology,US8030542042
31 | Drug Manufacturers - General,AbbVie Inc.,ABBV,United States,Healthcare,US00287Y1091
32 | Oil & Gas Integrated,Chevron Corporation,CVX,United States,Energy,US1667641005
33 | Beverages - Non-Alcoholic,The Coca-Cola Company,KO,United States,Consumer Staples,US1912161007
34 | Semiconductor Equipment & Materials,ASML Holding N.V.,ASML,Netherlands,Technology,USN 70592100.00
35 | Telecom Services,"T-Mobile US, Inc.",TMUS,United States,Communication Services,US8725901040
36 | Banks - Diversified,Wells Fargo & Company,WFC,United States,Financials,US9497461015
37 | Auto Manufacturers,Toyota Motor Corporation,TM,Japan,Consumer Discretionary,US8923313071
38 | Drug Manufacturers - General,"Merck & Co., Inc.",MRK,United States,Healthcare,US58933Y1055
39 | Software - Application,"ServiceNow, Inc.",NOW,United States,Technology,US81762P1021
40 | Communication Equipment,"Cisco Systems, Inc.",CSCO,United States,Technology,US17275R1023
41 | Information Technology Services,Accenture plc,ACN,Ireland,Technology,IE00B4BNMY34
42 | Asset Management,Blackstone Inc.,BX,United States,Financials,US09260D1072
43 | Diagnostics & Research,Thermo Fisher Scientific Inc.,TMO,United States,Healthcare,US8835561023
44 | Capital Markets,Morgan Stanley,MS,United States,Financials,US6174464486
45 | Credit Services,American Express Company,AXP,United States,Financials,US0258161092
46 | Medical Devices,Abbott Laboratories,ABT,United States,Healthcare,US0028241000
47 | Internet Retail,Alibaba Group Holding Limited,BABA,China,Consumer Discretionary,US01609W1027
48 | Capital Markets,"The Goldman Sachs Group, Inc.",GS,United States,Financials,US38141G1040
49 | Drug Manufacturers - General,AstraZeneca PLC,AZN,United Kingdom,Healthcare,US0463531089
50 | Aerospace & Defense,General Electric Company,GE,United States,Industrials,US3696043013
51 | Information Technology Services,International Business Machines Corporation,IBM,United States,Technology,US4592001014
52 | Restaurants,McDonald's Corporation,MCD,United States,Consumer Discretionary,US5801351017
53 | Beverages - Non-Alcoholic,"PepsiCo, Inc.",PEP,United States,Consumer Staples,US7134481081
54 | Specialty Chemicals,Linde plc,LIN,United Kingdom,Materials,IE000S9YS762
55 | Medical Instruments & Supplies,"Intuitive Surgical, Inc.",ISRG,United States,Healthcare,US46120E6023
56 | Drug Manufacturers - General,Novartis AG,NVS,Switzerland,Healthcare,US66987V1098
57 | Entertainment,The Walt Disney Company,DIS,United States,Communication Services,US2546871060
58 | Tobacco,Philip Morris International Inc.,PM,United States,Consumer Staples,US7181721090
59 | Oil & Gas Integrated,Shell plc,SHEL,United Kingdom,Energy,US7802593050
60 | Software - Infrastructure,Adobe Inc.,ADBE,United States,Technology,US00724F1012
61 | Semiconductors,QUALCOMM Incorporated,QCOM,United States,Technology,US7475251036
62 | Farm & Heavy Construction Machinery,Caterpillar Inc.,CAT,United States,Industrials,US1491231015
63 | Semiconductors,"Advanced Micro Devices, Inc.",AMD,United States,Technology,US0079031078
64 | Software - Infrastructure,Palantir Technologies Inc.,PLTR,United States,Technology,US69608A1088
65 | Banks - Diversified,HSBC Holdings plc,HSBC,United Kingdom,Financials,US4042804066
66 | Diagnostics & Research,Danaher Corporation,DHR,United States,Healthcare,US2358511028
67 | Telecom Services,AT&T Inc.,T,United States,Communication Services,US00206R1023
68 | Banks - Diversified,Royal Bank of Canada,RY,Canada,Financials,CA7800871021
69 | Aerospace & Defense,RTX Corporation,RTX,United States,Industrials,US75513E1010
70 | Telecom Services,Verizon Communications Inc.,VZ,United States,Communication Services,US92343V1044
71 | Software - Application,Intuit Inc.,INTU,United States,Technology,US4612021034
72 | Semiconductors,Texas Instruments Incorporated,TXN,United States,Technology,US8825081040
73 | Asset Management,"BlackRock, Inc.",BLK,United States,Financials,US09247X1019
74 | Financial Data & Stock Exchanges,S&P Global Inc.,SPGI,United States,Financials,US78409V1044
75 | Semiconductors,Arm Holdings plc,ARM,United Kingdom,Technology,US0420682058
76 | Internet Retail,PDD Holdings Inc.,PDD,Ireland,Consumer Discretionary,US7223041028
77 | Travel Services,Booking Holdings Inc.,BKNG,United States,Consumer Discretionary,US09857L1089
78 | Software - Application,Shopify Inc.,SHOP,Canada,Technology,CA82509L1076
79 | Drug Manufacturers - General,Pfizer Inc.,PFE,United States,Healthcare,US7170811035
80 | Railroads,Union Pacific Corporation,UNP,United States,Industrials,US9078181081
81 | Medical Devices,Boston Scientific Corporation,BSX,United States,Healthcare,US1011371077
82 | Drug Manufacturers - General,Amgen Inc.,AMGN,United States,Healthcare,US0311621009
83 | Medical Devices,Stryker Corporation,SYK,United States,Healthcare,US8636671013
84 | Banks - Diversified,Citigroup Inc.,C,United States,Financials,US1729674242
85 | Household & Personal Products,Unilever PLC,UL,United Kingdom,Consumer Staples,US9047677045
86 | Capital Markets,The Charles Schwab Corporation,SCHW,United States,Financials,US8085131055
87 | Home Improvement Retail,"Lowe's Companies, Inc.",LOW,United States,Consumer Discretionary,US5486611073
88 | Asset Management,KKR & Co. Inc.,KKR,United States,Financials,US48251W1045
89 | Banks - Regional,HDFC Bank Limited,HDB,India,Financials,US40415F1012
90 | Banks - Diversified,"Mitsubishi UFJ Financial Group, Inc.",MUFG,Japan,Financials,US6068221042
91 | Utilities - Regulated Electric,"NextEra Energy, Inc.",NEE,United States,Utilities,US65339F1012
92 | Telecom Services,Comcast Corporation,CMCSA,United States,Communication Services,US20030N1019
93 | Insurance - Property & Casualty,The Progressive Corporation,PGR,United States,Financials,US7433151039
94 | Conglomerates,Honeywell International Inc.,HON,United States,Industrials,US4385161066
95 | Software - Application,"Uber Technologies, Inc.",UBER,United States,Technology,US90353T1007
96 | Semiconductor Equipment & Materials,"Applied Materials, Inc.",AMAT,United States,Technology,US0382221051
97 | Apparel Retail,"The TJX Companies, Inc.",TJX,United States,Consumer Discretionary,US8725401090
98 | Consumer Electronics,Sony Group Corporation,SONY,Japan,Technology,US8356993076
99 | Computer Hardware,Arista Networks Inc,ANET,United States,Technology,US0404131064
100 | Aerospace & Defense,The Boeing Company,BA,United States,Industrials,US0970231058
101 | Drug Manufacturers - General,Sanofi,SNY,France,Healthcare,US80105N1054
102 | Oil & Gas Exploration & Production,ConocoPhillips,COP,United States,Energy,US20825C1045
103 | Oil & Gas Integrated,TotalEnergies SE,TTE,France,Energy,US89151E1091
104 | Farm & Heavy Construction Machinery,Deere & Company,DE,United States,Industrials,US2441991054
105 | Software - Infrastructure,"Palo Alto Networks, Inc.",PANW,United States,Technology,US6974351057
106 | Other Industrial Metals & Mining,BHP Group Limited,BHP,Australia,Materials,US0886061086
107 | Specialty Industrial Machinery,Eaton Corporation plc,ETN,Ireland,Industrials,IE00B8KQN827
108 | Software - Application,"Automatic Data Processing, Inc.",ADP,United States,Technology,US0530151036
109 | Software - Application,AppLovin Corporation,APP,United States,Technology,US03831W1080
110 | Information Technology Services,"Fiserv, Inc.",FI,United States,Technology,US3377381088
111 | Drug Manufacturers - General,Bristol-Myers Squibb Company,BMY,United States,Healthcare,US1101221083
112 | Medical Devices,Medtronic plc,MDT,Ireland,Healthcare,IE00BTN1Y115
113 | Drug Manufacturers - General,"Gilead Sciences, Inc.",GILD,United States,Healthcare,US3755581036
114 | Integrated Freight & Logistics,"United Parcel Service, Inc.",UPS,United States,Industrials,US9113121068
115 | Restaurants,Starbucks Corporation,SBUX,United States,Consumer Discretionary,US8552441094
116 | Biotechnology,Vertex Pharmaceuticals Incorporated,VRTX,United States,Healthcare,US92532F1003
117 | REIT - Industrial,"Prologis, Inc.",PLD,United States,Real Estate,US74340W1036
118 | Banks - Diversified,UBS Group AG,UBS,Switzerland,Financials,CH0244767585
119 | Footwear & Accessories,"NIKE, Inc.",NKE,United States,Consumer Discretionary,US6541061031
120 | Insurance - Property & Casualty,Chubb Limited,CB,Switzerland,Financials,CH0044328745
121 | Insurance Brokers,"Marsh & McLennan Companies, Inc.",MMC,United States,Financials,US5717481023
122 | Aerospace & Defense,Lockheed Martin Corporation,LMT,United States,Industrials,US5398301094
123 | Internet Content & Information,Spotify Technology S.A.,SPOT,Luxembourg,Communication Services,LU1778762911
124 | Semiconductors,"Analog Devices, Inc.",ADI,United States,Technology,US0326541051
125 | Other Industrial Metals & Mining,Rio Tinto Group,RIO,United Kingdom,Materials,US7672041008
126 | Banks - Regional,ICICI Bank Limited,IBN,India,Financials,US45104G1040
127 | Software - Infrastructure,"CrowdStrike Holdings, Inc.",CRWD,United States,Technology,US22788C1053
128 | Banks - Diversified,The Toronto-Dominion Bank,TD,Canada,Financials,CA8911605092
129 | Semiconductors,"Micron Technology, Inc.",MU,United States,Technology,US5951121038
130 | Utilities - Renewable,GE Vernova Inc.,GEV,United States,Utilities,US36828A1016
131 | Beverages - Brewers,Anheuser-Busch InBev SA/NV,BUD,Belgium,Consumer Staples,US03524A1088
132 | Banks - Diversified,"Sumitomo Mitsui Financial Group, Inc.",SMFG,Japan,Financials,US86562M2098
133 | Oil & Gas Midstream,Enbridge Inc.,ENB,Canada,Energy,CA29250N1050
134 | Internet Retail,"MercadoLibre, Inc.",MELI,Uruguay,Consumer Discretionary,US58733R1023
135 | Semiconductor Equipment & Materials,Lam Research Corporation,LRCX,United States,Technology,US5128071082
136 | Asset Management,"Apollo Global Management, Inc.",APO,United States,Financials,US03769M1062
137 | Semiconductor Equipment & Materials,KLA Corporation,KLAC,United States,Technology,US4824801009
138 | Healthcare Plans,"Elevance Health, Inc.",ELV,United States,Healthcare,US0367521038
139 | Utilities - Regulated Electric,The Southern Company,SO,United States,Utilities,US8425871071
140 | Specialty Chemicals,The Sherwin-Williams Company,SHW,United States,Materials,US8243481061
141 | Specialty Business Services,RELX PLC,RELX,United Kingdom,Industrials,US7595301083
142 | Financial Data & Stock Exchanges,"Intercontinental Exchange, Inc.",ICE,United States,Financials,US45866F1049
143 | Asset Management,Brookfield Corporation,BN,Canada,Financials,CA11271J1075
144 | Semiconductors,"Marvell Technology, Inc.",MRVL,United States,Technology,US5738741041
145 | Financial Data & Stock Exchanges,Moody's Corporation,MCO,United States,Financials,US6153691059
146 | Tobacco,"Altria Group, Inc.",MO,United States,Consumer Staples,US02209S1033
147 | Credit Services,"PayPal Holdings, Inc.",PYPL,United States,Financials,US70450Y1038
148 | Information Technology Services,Infosys Limited,INFY,India,Technology,US4567881085
149 | REIT - Specialty,"Equinix, Inc.",EQIX,United States,Real Estate,US29444U7000
150 | REIT - Specialty,American Tower Corporation,AMT,United States,Real Estate,US03027X1000
151 | Utilities - Renewable,Constellation Energy Corporation,CEG,United States,Utilities,US21037T1097
152 | Tobacco,British American Tobacco p.l.c.,BTI,United Kingdom,Consumer Staples,US1104481072
153 | Oil & Gas Integrated,Petróleo Brasileiro S.A. - Petrobras,PBR,Brazil,Energy,US71654V4086
154 | Oil & Gas Integrated,Petróleo Brasileiro S.A. - Petrobras,PBR.A,Brazil,Energy,US71654V1017
155 | Utilities - Regulated Electric,Duke Energy Corporation,DUK,United States,Utilities,US26441C2044
156 | Specialty Industrial Machinery,Parker-Hannifin Corporation,PH,United States,Industrials,US7010941042
157 | Waste Management,"Waste Management, Inc.",WM,United States,Industrials,US94106L1098
158 | REIT - Healthcare Facilities,Welltower Inc.,WELL,United States,Real Estate,US95040Q1040
159 | Semiconductors,Intel Corporation,INTC,United States,Technology,US4581401001
160 | Financial Data & Stock Exchanges,CME Group Inc.,CME,United States,Financials,US12572Q1058
161 | Healthcare Plans,The Cigna Group,CI,United States,Healthcare,US1255231003
162 | Software - Application,MicroStrategy Incorporated,MSTR,United States,Technology,US5949724083
163 | Medical Care Facilities,"HCA Healthcare, Inc.",HCA,United States,Healthcare,US40412C1018
164 | Electronic Components,Amphenol Corporation,APH,United States,Technology,US0320951017
165 | Building Products & Equipment,Trane Technologies plc,TT,Ireland,Industrials,IE00BK9ZQ967
166 | Software - Application,"Cadence Design Systems, Inc.",CDNS,United States,Technology,US1273871087
167 | Travel Services,"Airbnb, Inc.",ABNB,United States,Consumer Discretionary,US0090661010
168 | Oil & Gas Integrated,BP p.l.c.,BP,United Kingdom,Energy,US0556221044
169 | Conglomerates,3M Company,MMM,United States,Industrials,US88579Y1010
170 | Software - Infrastructure,"Synopsys, Inc.",SNPS,United States,Technology,US8716071076
171 | Specialty Business Services,Cintas Corporation,CTAS,United States,Industrials,US1729081059
172 | Insurance Brokers,Aon plc,AON,Ireland,Financials,IE00BLP1HW54
173 | Lodging,"Marriott International, Inc.",MAR,United States,Consumer Discretionary,US5719032022
174 | Banks - Regional,"The PNC Financial Services Group, Inc.",PNC,United States,Financials,US6934751057
175 | Restaurants,"Chipotle Mexican Grill, Inc.",CMG,United States,Consumer Discretionary,US1696561059
176 | Communication Equipment,"Motorola Solutions, Inc.",MSI,United States,Technology,US6200763075
177 | Banks - Diversified,"Banco Santander, S.A.",SAN,Spain,Financials,US05964H1059
178 | Credit Services,Capital One Financial Corporation,COF,United States,Financials,US14040H1059
179 | Auto Manufacturers,Ferrari N.V.,RACE,Italy,Consumer Discretionary,NL0011585146
180 | Drug Manufacturers - Specialty & Generic,Zoetis Inc.,ZTS,United States,Healthcare,US98978V1035
181 | Internet Content & Information,"DoorDash, Inc.",DASH,United States,Communication Services,US25809K1051
182 | Medical Distribution,McKesson Corporation,MCK,United States,Healthcare,US58155Q1031
183 | Software - Infrastructure,"Fortinet, Inc.",FTNT,United States,Technology,US34959E1091
184 | Specialty Industrial Machinery,Illinois Tool Works Inc.,ITW,United States,Industrials,US4523081093
185 | Confectioners,"Mondelez International, Inc.",MDLZ,United States,Consumer Staples,US6092071058
186 | Banks - Regional,U.S. Bancorp,USB,United States,Financials,US9029733048
187 | Specialty Business Services,Thomson Reuters Corporation,TRI,Canada,Industrials,CA8849038085
188 | Aerospace & Defense,TransDigm Group Incorporated,TDG,United States,Industrials,US8936411003
189 | Specialty Industrial Machinery,Emerson Electric Co.,EMR,United States,Industrials,US2910111044
190 | Railroads,Canadian Pacific Kansas City Limited,CP,Canada,Industrials,CA13646K1084
191 | Biotechnology,"Regeneron Pharmaceuticals, Inc.",REGN,United States,Healthcare,US75886F1075
192 | Specialty Retail,"O'Reilly Automotive, Inc.",ORLY,United States,Consumer Discretionary,US67103H1077
193 | Household & Personal Products,Colgate-Palmolive Company,CL,United States,Consumer Staples,US1941621039
194 | Banks - Diversified,Bank of Montreal,BMO,Canada,Financials,CA0636711016
195 | Insurance Brokers,Arthur J. Gallagher & Co.,AJG,United States,Financials,US3635761097
196 | Oil & Gas Midstream,Enterprise Products Partners L.P.,EPD,United States,Energy,US2937921078
197 | Oil & Gas Exploration & Production,"EOG Resources, Inc.",EOG,United States,Energy,US26875P1012
198 | Specialty Chemicals,"Air Products and Chemicals, Inc.",APD,United States,Materials,US0091581068
199 | Medical Instruments & Supplies,"Becton, Dickinson and Company",BDX,United States,Healthcare,US0758871091
200 | Healthcare Plans,CVS Health Corporation,CVS,United States,Healthcare,US1266501006
201 | Aerospace & Defense,General Dynamics Corporation,GD,United States,Industrials,US3695501086
202 | Software - Application,"Workday, Inc.",WDAY,United States,Technology,US98138H1014
203 | Copper,Southern Copper Corporation,SCCO,United States,Materials,US84265V1052
204 | Software - Application,Atlassian Corporation,TEAM,Australia,Technology,US0494681010
205 | Travel Services,Royal Caribbean Cruises Ltd.,RCL,United States,Consumer Discretionary,LR0008862868
206 | Aerospace & Defense,Northrop Grumman Corporation,NOC,United States,Industrials,US6668071029
207 | Computer Hardware,Dell Technologies Inc.,DELL,United States,Technology,US24703L2025
208 | Specialty Chemicals,Ecolab Inc.,ECL,United States,Materials,US2788651006
209 | Financial Data & Stock Exchanges,"Coinbase Global, Inc.",COIN,United States,Financials,US19260Q1076
210 | Drug Manufacturers - General,GSK plc,GSK,United Kingdom,Healthcare,US37733W2044
211 | Oil & Gas Midstream,Energy Transfer LP,ET,United States,Energy,US29273V1008
212 | Beverages - Wineries & Distilleries,Diageo plc,DEO,United Kingdom,Consumer Staples,US25243Q2057
213 | Banks - Regional,"Mizuho Financial Group, Inc.",MFG,Japan,Financials,US60687Y1091
214 | Internet Retail,Sea Limited,SE,Singapore,Consumer Discretionary,US81141R1005
215 | Waste Management,"Republic Services, Inc.",RSG,United States,Industrials,US7607591002
216 | Oil & Gas Midstream,"The Williams Companies, Inc.",WMB,United States,Energy,US9694571004
217 | Integrated Freight & Logistics,FedEx Corporation,FDX,United States,Industrials,US31428X1063
218 | Building Materials,CRH plc,CRH,Ireland,Materials,IE0001827041
219 | Electronic Gaming & Multimedia,"NetEase, Inc.",NTES,China,Communication Services,US64110W1027
220 | Software - Application,"Autodesk, Inc.",ADSK,United States,Technology,US0527691069
221 | Railroads,Canadian National Railway Company,CNI,Canada,Industrials,CA1363751027
222 | REIT - Retail,"Simon Property Group, Inc.",SPG,United States,Real Estate,US8288061091
223 | Discount Stores,Target Corporation,TGT,United States,Consumer Staples,US87612E1064
224 | Oil & Gas Exploration & Production,Canadian Natural Resources Limited,CNQ,Canada,Energy,CA1363851017
225 | Banks - Diversified,The Bank of Nova Scotia,BNS,Canada,Financials,CA0641491075
226 | Oil & Gas Integrated,Equinor ASA,EQNR,Norway,Energy,US29446M1027
227 | Railroads,CSX Corporation,CSX,United States,Industrials,US1264081035
228 | Banks - Regional,Truist Financial Corporation,TFC,United States,Financials,US89832Q1094
229 | Software - Application,Snowflake Inc.,SNOW,United States,Technology,US8334451098
230 | Banks - Diversified,The Bank of New York Mellon Corporation,BK,United States,Financials,US0640581007
231 | Lodging,Hilton Worldwide Holdings Inc.,HLT,United States,Consumer Discretionary,US43300A2033
232 | Banks - Diversified,"Banco Bilbao Vizcaya Argentaria, S.A.",BBVA,Spain,Financials,US05946K1016
233 | Oil & Gas Midstream,"Kinder Morgan, Inc.",KMI,United States,Energy,US49456B1017
234 | Banks - Diversified,Canadian Imperial Bank of Commerce,CM,Canada,Financials,CA1360691010
235 | Banks - Regional,Nu Holdings Ltd.,NU,Brazil,Financials,KYG6683N1034
236 | Asset Management,Ares Management Corporation,ARES,United States,Financials,US03990B1017
237 | Building Products & Equipment,Carrier Global Corporation,CARR,United States,Industrials,US14448C1045
238 | Insurance - Life,Aflac Incorporated,AFL,United States,Financials,US0010551028
239 | Internet Retail,"JD.com, Inc.",JD,China,Consumer Discretionary,US47215P1066
240 | Software - Application,"The Trade Desk, Inc.",TTD,United States,Technology,US88339J1051
241 | Insurance - Life,"MetLife, Inc.",MET,United States,Financials,US59156R1086
242 | Utilities - Regulated Electric,National Grid plc,NGG,United Kingdom,Utilities,US6362744095
243 | Software - Application,"Roper Technologies, Inc.",ROP,United States,Technology,US7766961061
244 | Oil & Gas Midstream,"ONEOK, Inc.",OKE,United States,Energy,US6826801036
245 | Telecom Services,"Charter Communications, Inc.",CHTR,United States,Communication Services,US16119P1084
246 | Oil & Gas Equipment & Services,Schlumberger Limited,SLB,United States,Energy,AN8068571086
247 | Railroads,Norfolk Southern Corporation,NSC,United States,Industrials,US6558441084
248 | Insurance - Property & Casualty,"The Travelers Companies, Inc.",TRV,United States,Financials,US89417E1091
249 | Farm & Heavy Construction Machinery,PACCAR Inc,PCAR,United States,Industrials,US6937181088
250 | Specialty Retail,"AutoZone, Inc.",AZO,United States,Consumer Discretionary,US0533321024
251 | Asset Management,"Ameriprise Financial, Inc.",AMP,United States,Financials,US03076C1062
252 | Specialty Business Services,"Copart, Inc.",CPRT,United States,Industrials,US2172041061
253 | Industrial Distribution,"W.W. Grainger, Inc.",GWW,United States,Industrials,US3848021040
254 | Auto Manufacturers,General Motors Company,GM,United States,Consumer Discretionary,US37045V1008
255 | Software - Infrastructure,"Block, Inc.",XYZ,United States,Technology,US8522341036
256 | REIT - Specialty,"Digital Realty Trust, Inc.",DLR,United States,Real Estate,US2538681030
257 | Semiconductors,NXP Semiconductors N.V.,NXPI,Netherlands,Technology,NL0009538784
258 | Utilities - Regulated Electric,"American Electric Power Company, Inc.",AEP,United States,Utilities,US0255371017
259 | Software - Application,"Paychex, Inc.",PAYX,United States,Technology,US7043261079
260 | Oil & Gas Midstream,MPLX LP,MPLX,United States,Energy,US55336V1008
261 | REIT - Industrial,Public Storage,PSA,United States,Real Estate,US74460D1090
262 | Insurance - Life,Manulife Financial Corporation,MFC,Canada,Financials,CA56501R1064
263 | Banks - Regional,Itaú Unibanco Holding S.A.,ITUB,Brazil,Financials,US4655621062
264 | Utilities - Diversified,Sempra,SRE,United States,Utilities,US8168511090
265 | Banks - Diversified,Barclays PLC,BCS,United Kingdom,Financials,US06738E2046
266 | Auto & Truck Dealerships,Carvana Co.,CVNA,United States,Consumer Discretionary,US1468691027
267 | Software - Application,"Datadog, Inc.",DDOG,United States,Technology,US23804L1035
268 | Copper,Freeport-McMoRan Inc.,FCX,United States,Materials,US35671D8570
269 | Banks - Diversified,ING Groep N.V.,ING,Netherlands,Financials,US4568371037
270 | Aerospace & Defense,Howmet Aerospace Inc.,HWM,United States,Industrials,US4432011082
271 | Utilities - Independent Power Producers,Vistra Corp.,VST,United States,Utilities,US92840M1027
272 | Oil & Gas Midstream,"Cheniere Energy, Inc.",LNG,United States,Energy,US16411R2085
273 | Insurance - Property & Casualty,The Allstate Corporation,ALL,United States,Financials,US0200021014
274 | Rental & Leasing Services,"United Rentals, Inc.",URI,United States,Industrials,US9113631090
275 | Building Products & Equipment,Johnson Controls International plc,JCI,Ireland,Industrials,IE00BY7QL619
276 | Credit Services,Discover Financial Services,DFS,United States,Financials,US2547091080
277 | Oil & Gas Refining & Marketing,Phillips 66,PSX,United States,Energy,US7185461040
278 | Apparel Retail,Lululemon Athletica Inc.,LULU,Canada,Consumer Discretionary,US5500211090
279 | Medical Distribution,"Cencora, Inc.",COR,United States,Healthcare,US03073E1055
280 | Oil & Gas Exploration & Production,"Diamondback Energy, Inc.",FANG,United States,Energy,US25278X1090
281 | Financial Data & Stock Exchanges,MSCI Inc.,MSCI,United States,Financials,US55354G1004
282 | Apparel Retail,"Ross Stores, Inc.",ROST,United States,Consumer Discretionary,US7782961038
283 | Aerospace & Defense,"Axon Enterprise, Inc.",AXON,United States,Industrials,US05464C1018
284 | Oil & Gas Refining & Marketing,Marathon Petroleum Corporation,MPC,United States,Energy,US56585A1025
285 | Oil & Gas Exploration & Production,"Venture Global, Inc.",VG,,Energy,
286 | REIT - Retail,Realty Income Corporation,O,United States,Real Estate,US7561091049
287 | Oil & Gas Integrated,Suncor Energy Inc.,SU,Canada,Energy,CA8672241079
288 | Specialty Industrial Machinery,Cummins Inc.,CMI,United States,Industrials,US2310211063
289 | Software - Infrastructure,"Cloudflare, Inc.",NET,United States,Technology,US18915M1071
290 | Gambling,Flutter Entertainment plc,FLUT,Ireland,Consumer Discretionary,IE00BWT6H894
291 | Beverages - Non-Alcoholic,Monster Beverage Corporation,MNST,United States,Consumer Staples,US61174X1090
292 | Waste Management,"Waste Connections, Inc.",WCN,Canada,Industrials,CA94106B1013
293 | Oil & Gas Midstream,TC Energy Corporation,TRP,Canada,Energy,CA87807B1076
294 | Insurance - Diversified,"American International Group, Inc.",AIG,United States,Financials,US0268747849
295 | Financial Data & Stock Exchanges,"Nasdaq, Inc.",NDAQ,United States,Financials,US6311031081
296 | Gold,Newmont Corporation,NEM,United States,Materials,US6516391066
297 | Travel Services,Trip.com Group Limited,TCOM,Singapore,Consumer Discretionary,US89677Q1076
298 | Utilities - Regulated Electric,"Dominion Energy, Inc.",D,United States,Utilities,US25746U1097
299 | Banks - Regional,Lloyds Banking Group plc,LYG,United Kingdom,Financials,US5394391099
300 | Oil & Gas Exploration & Production,Occidental Petroleum Corporation,OXY,United States,Energy,US6745991058
301 | Residential Construction,"D.R. Horton, Inc.",DHI,United States,Consumer Discretionary,US23331A1097
302 | Medical Instruments & Supplies,Alcon Inc.,ALC,Switzerland,Healthcare,CH0432492467
303 | Software - Application,Fair Isaac Corporation,FICO,United States,Technology,US3032501047
304 | Gold,Agnico Eagle Mines Limited,AEM,Canada,Materials,CA0084741085
305 | Electronic Gaming & Multimedia,Roblox Corporation,RBLX,United States,Communication Services,US7710491033
306 | Oil & Gas Exploration & Production,Hess Corporation,HES,United States,Energy,US42809H1077
307 | Auto Manufacturers,"Honda Motor Co., Ltd.",HMC,Japan,Consumer Discretionary,US4381283088
308 | Electronic Components,TE Connectivity plc,TEL,Ireland,Technology,CH0102993182
309 | Agricultural Inputs,"Corteva, Inc.",CTVA,United States,Materials,US22052L1044
310 | Oil & Gas Midstream,Targa Resources Corp.,TRGP,United States,Energy,US87612G1013
311 | Electronic Components,Corning Incorporated,GLW,United States,Technology,US2193501051
312 | Oil & Gas Refining & Marketing,Valero Energy Corporation,VLO,United States,Energy,US91913Y1001
313 | Grocery Stores,The Kroger Co.,KR,United States,Consumer Staples,US5010441013
314 | Capital Markets,"Robinhood Markets, Inc.",HOOD,United States,Financials,US7707001027
315 | Engineering & Construction,"Quanta Services, Inc.",PWR,United States,Industrials,US74762E1029
316 | Airlines,"Delta Air Lines, Inc.",DAL,United States,Industrials,US2473617023
317 | Information Technology Services,"Fidelity National Information Services, Inc.",FIS,United States,Technology,US31620M1062
318 | Telecom Services,"América Móvil, S.A.B. de C.V.",AMX,Mexico,Communication Services,US02390A1016
319 | Household & Personal Products,Kimberly-Clark Corporation,KMB,United States,Consumer Staples,US4943681035
320 | Oil & Gas Integrated,Eni S.p.A.,E,Italy,Energy,US26874R1086
321 | Insurance - Life,"Prudential Financial, Inc.",PRU,United States,Financials,US7443201022
322 | Diagnostics & Research,"Agilent Technologies, Inc.",A,United States,Healthcare,US00846U1016
323 | Real Estate Services,"CBRE Group, Inc.",CBRE,United States,Real Estate,US12504L1098
324 | Industrial Distribution,Fastenal Company,FAST,United States,Industrials,US3119001044
325 | Oil & Gas Equipment & Services,Baker Hughes Company,BKR,United States,Energy,US05722G1004
326 | Medical Devices,Edwards Lifesciences Corporation,EW,United States,Healthcare,US28176E1082
327 | Banks - Regional,NatWest Group plc,NWG,United Kingdom,Financials,US6390572070
328 | Drug Manufacturers - Specialty & Generic,Haleon plc,HLN,United Kingdom,Healthcare,US4055521003
329 | Beverages - Non-Alcoholic,Keurig Dr Pepper Inc.,KDP,United States,Consumer Staples,US49271V1008
330 | Drug Manufacturers - Specialty & Generic,Takeda Pharmaceutical Company Limited,TAK,Japan,Healthcare,US8740602052
331 | Specialty Industrial Machinery,"AMETEK, Inc.",AME,United States,Industrials,US0311001004
332 | Information Technology Services,"Gartner, Inc.",IT,United States,Technology,US3666511072
333 | Scientific & Technical Instruments,Garmin Ltd.,GRMN,Switzerland,Technology,CH0114405324
334 | Internet Retail,"Coupang, Inc.",CPNG,United States,Consumer Discretionary,US22266T1097
335 | Software - Application,"HubSpot, Inc.",HUBS,United States,Technology,US4435731009
336 | Household & Personal Products,Kenvue Inc.,KVUE,United States,Consumer Staples,US49177J1025
337 | Utilities - Regulated Electric,Public Service Enterprise Group Incorporated,PEG,United States,Utilities,US7445731067
338 | Trucking,"Old Dominion Freight Line, Inc.",ODFL,United States,Industrials,US6795801009
339 | Aerospace & Defense,"L3Harris Technologies, Inc.",LHX,United States,Industrials,US5024311095
340 | Other,Advantest Corporation,ATE,,,
341 | Information Technology Services,Cognizant Technology Solutions Corporation,CTSH,United States,Technology,US1924461023
342 | Health Information Services,GE HealthCare Technologies Inc.,GEHC,United States,Healthcare,US36266G1076
343 | Auto Manufacturers,Ford Motor Company,F,United States,Consumer Discretionary,US3453708600
344 | Utilities - Regulated Electric,Exelon Corporation,EXC,United States,Utilities,US30161N1019
345 | Electrical Equipment & Parts,Vertiv Holdings Co,VRT,United States,Industrials,US92537N1081
346 | Consulting Services,"Verisk Analytics, Inc.",VRSK,United States,Industrials,US92345Y1064
347 | Biotechnology,argenx SE,ARGX,Netherlands,Healthcare,NL0010832176
348 | Banks - Regional,Deutsche Bank Aktiengesellschaft,DB,Germany,Financials,DE0005140008
349 | REIT - Specialty,Crown Castle Inc.,CCI,United States,Real Estate,US22822V1017
350 | Asset Management,Blue Owl Capital Inc.,OWL,United States,Financials,US09581B1035
351 | Other Industrial Metals & Mining,Vale S.A.,VALE,Brazil,Materials,US91912E1055
352 | Specialty Industrial Machinery,Otis Worldwide Corporation,OTIS,United States,Industrials,US68902V1070
353 | Utilities - Regulated Electric,Xcel Energy Inc.,XEL,United States,Utilities,US98389B1008
354 | Information Technology Services,Wipro Limited,WIT,India,Technology,US97651M1099
355 | Health Information Services,Veeva Systems Inc.,VEEV,United States,Healthcare,US9224751084
356 | Diagnostics & Research,IQVIA Holdings Inc.,IQV,United States,Healthcare,US46266C1053
357 | Medical Instruments & Supplies,ResMed Inc.,RMD,United States,Healthcare,US7611521078
358 | Auto Manufacturers,Stellantis N.V.,STLA,Netherlands,Consumer Discretionary,NL00150001Q9
359 | Specialty Industrial Machinery,Ingersoll Rand Inc.,IR,United States,Industrials,US45687V1061
360 | Industrial Distribution,Ferguson Enterprises Inc.,FERG,United States,Industrials,JE00BJVNSS43
361 | Healthcare Plans,Humana Inc.,HUM,United States,Healthcare,US4448591028
362 | Oil & Gas Integrated,Imperial Oil Limited,IMO,Canada,Energy,CA4530384086
363 | Travel Services,Carnival Corporation & plc,CCL,United States,Consumer Discretionary,GB0031215220
364 | Building Materials,Vulcan Materials Company,VMC,United States,Materials,US9291601097
365 | Residential Construction,Lennar Corporation,LEN,United States,Consumer Discretionary,US5260571048
366 | Restaurants,"Yum! Brands, Inc.",YUM,United States,Consumer Discretionary,US9884981013
367 | Biotechnology,"Alnylam Pharmaceuticals, Inc.",ALNY,United States,Healthcare,US02043Q1076
368 | Leisure,Carnival Corporation & plc,CUK,United States,Consumer Discretionary,US14365C1036
369 | Beverages - Non-Alcoholic,Coca-Cola Europacific Partners PLC,CCEP,United Kingdom,Consumer Staples,GB00BDCPN049
370 | Residential Construction,Lennar Corporation,LEN.B,United States,Consumer Discretionary,US5260573028
371 | Packaged Foods,The Kraft Heinz Company,KHC,United States,Consumer Staples,US5007541064
372 | Insurance - Diversified,Arch Capital Group Ltd.,ACGL,Bermuda,Financials,BMG0450A1053
373 | Food Distribution,Sysco Corporation,SYY,United States,Consumer Staples,US8718291078
374 | Railroads,Westinghouse Air Brake Technologies Corporation,WAB,United States,Industrials,US9297401088
375 | Asset Management,"Raymond James Financial, Inc.",RJF,United States,Financials,US7547301090
376 | Airlines,"United Airlines Holdings, Inc.",UAL,United States,Industrials,US9100471096
377 | Utilities - Regulated Electric,PG&E Corporation,PCG,United States,Utilities,US69331C1080
378 | Medical Devices,"DexCom, Inc.",DXCM,United States,Healthcare,US2521311074
379 | Diagnostics & Research,"IDEXX Laboratories, Inc.",IDXX,United States,Healthcare,US45168D1046
380 | Internet Content & Information,"Reddit, Inc.",RDDT,United States,Communication Services,US75734B1008
381 | REIT - Industrial,Extra Space Storage Inc.,EXR,United States,Real Estate,US30225T1025
382 | Consulting Services,Equifax Inc.,EFX,United States,Industrials,US2944291051
383 | Insurance - Diversified,Sun Life Financial Inc.,SLF,Canada,Financials,CA8667961053
384 | Utilities - Regulated Electric,Entergy Corporation,ETR,United States,Utilities,US29364G1031
385 | Building Materials,"Martin Marietta Materials, Inc.",MLM,United States,Materials,US5732841060
386 | Beverages - Brewers,"Constellation Brands, Inc.",STZ,United States,Consumer Staples,US21036P1084
387 | Banks - Regional,M&T Bank Corporation,MTB,United States,Financials,US55261F1049
388 | Packaged Foods,"General Mills, Inc.",GIS,United States,Consumer Staples,US3703341046
389 | Insurance - Property & Casualty,"The Hartford Financial Services Group, Inc.",HIG,United States,Financials,US4165151048
390 | Electronic Gaming & Multimedia,"Take-Two Interactive Software, Inc.",TTWO,United States,Communication Services,US8740541094
391 | Entertainment,"Live Nation Entertainment, Inc.",LYV,United States,Communication Services,US5380341090
392 | Insurance Brokers,Willis Towers Watson Public Limited Company,WTW,United Kingdom,Financials,IE00BDB6Q211
393 | Footwear & Accessories,Deckers Outdoor Corporation,DECK,United States,Consumer Discretionary,US2435371073
394 | Healthcare Plans,Centene Corporation,CNC,United States,Healthcare,US15135B1017
395 | Aerospace & Defense,HEICO Corporation,HEI,United States,Industrials,US4228061093
396 | Utilities - Regulated Electric,"Consolidated Edison, Inc.",ED,United States,Utilities,US2091151041
397 | Internet Retail,eBay Inc.,EBAY,United States,Consumer Discretionary,US2786421030
398 | Internet Content & Information,"Baidu, Inc.",BIDU,China,Communication Services,US0567521085
399 | Infrastructure Operations,Ferrovial SE,FER,Netherlands,Industrials,NL0015001FS8
400 | Specialty Chemicals,"DuPont de Nemours, Inc.",DD,United States,Materials,US26614N1028
401 | Specialty Industrial Machinery,"Rockwell Automation, Inc.",ROK,United States,Industrials,US7739031091
402 | REIT - Diversified,VICI Properties Inc.,VICI,United States,Real Estate,US9256521090
403 | Software - Infrastructure,"Zscaler, Inc.",ZS,United States,Technology,US98980G1022
404 | Resorts & Casinos,Las Vegas Sands Corp.,LVS,United States,Consumer Discretionary,US5178341070
405 | Utilities - Regulated Electric,"WEC Energy Group, Inc.",WEC,United States,Utilities,US92939U1060
406 | Real Estate Services,"CoStar Group, Inc.",CSGP,United States,Real Estate,US22160N1090
407 | REIT - Residential,"AvalonBay Communities, Inc.",AVB,United States,Real Estate,US0534841012
408 | Medical Distribution,"Cardinal Health, Inc.",CAH,United States,Healthcare,US14149Y1082
409 | Computer Hardware,HP Inc.,HPQ,United States,Technology,US40434L1052
410 | Specialty Retail,Tractor Supply Company,TSCO,United States,Consumer Discretionary,US8923561067
411 | Software - Application,"ANSYS, Inc.",ANSS,United States,Technology,US03662Q1058
412 | Electronic Gaming & Multimedia,Electronic Arts Inc.,EA,United States,Communication Services,US2855121099
413 | Capital Markets,Tradeweb Markets Inc.,TW,United States,Financials,US8926721064
414 | Confectioners,The Hershey Company,HSY,United States,Consumer Staples,US4278661081
415 | Semiconductors,Microchip Technology Incorporated,MCHP,United States,Technology,US5950171042
416 | Semiconductors,"Monolithic Power Systems, Inc.",MPWR,United States,Technology,US6098391054
417 | Software - Infrastructure,GoDaddy Inc.,GDDY,United States,Technology,US3802371076
418 | Insurance Brokers,"Brown & Brown, Inc.",BRO,United States,Financials,US1152361010
419 | Banks - Regional,Fifth Third Bancorp,FITB,United States,Financials,US3167731005
420 | Oil & Gas Midstream,"Cheniere Energy Partners, L.P.",CQP,United States,Energy,US16411Q1013
421 | Banks - Regional,"First Citizens BancShares, Inc.",FCNCA,United States,Financials,US31946M1036
422 | Biotechnology,BioNTech SE,BNTX,Germany,Healthcare,US09075V1026
423 | Household & Personal Products,The Estée Lauder Companies Inc.,EL,United States,Consumer Staples,US5184391044
424 | Beverages - Brewers,Ambev S.A.,ABEV,Brazil,Consumer Staples,US02319V1035
425 | Oil & Gas Exploration & Production,EQT Corporation,EQT,United States,Energy,US26884L1098
426 | Steel,Nucor Corporation,NUE,United States,Materials,US6703461052
427 | Telecom Services,"Chunghwa Telecom Co., Ltd.",CHT,Taiwan,Communication Services,US17133Q5027
428 | Specialty Industrial Machinery,Xylem Inc.,XYL,United States,Industrials,US98419M1009
429 | Banks - Regional,"First Citizens BancShares, Inc.",FCNCO,United States,Financials,US31959X2027
430 | Oil & Gas Exploration & Production,Texas Pacific Land Corporation,TPL,United States,Energy,US88262P1021
431 | Oil & Gas Exploration & Production,Woodside Energy Group Ltd,WDS,Australia,Energy,US9802283088
432 | Chemicals,Dow Inc.,DOW,United States,Materials,US2605571031
433 | Software - Infrastructure,Samsara Inc.,IOT,United States,Technology,US79589L1061
434 | Scientific & Technical Instruments,"Keysight Technologies, Inc.",KEYS,United States,Technology,US49338L1035
435 | Asset Management,State Street Corporation,STT,United States,Financials,US8574771031
436 | REIT - Specialty,Iron Mountain Incorporated,IRM,United States,Real Estate,US46284V1017
437 | Beverages - Brewers,"Fomento Económico Mexicano, S.A.B. de C.V.",FMX,Mexico,Consumer Staples,US3444191064
438 | Aerospace & Defense,HEICO Corporation,HEI.A,United States,Industrials,US4228062083
439 | Diagnostics & Research,Mettler-Toledo International Inc.,MTD,United States,Healthcare,US5926881054
440 | Specialty Chemicals,"PPG Industries, Inc.",PPG,United States,Materials,US6935061076
441 | Communication Equipment,Hewlett Packard Enterprise Company,HPE,United States,Technology,US42824C1099
442 | Packaged Foods,Kellanova,K,United States,Consumer Staples,US4878361082
443 | Packaging & Containers,Smurfit Westrock Plc,SW,Ireland,Consumer Discretionary,IE00028FXN24
444 | Restaurants,Restaurant Brands International Inc.,QSR,Canada,Consumer Discretionary,CA76131D1033
445 | Specialty Business Services,Global Payments Inc.,GPN,United States,Industrials,US37940X1028
446 | Gold,Barrick Gold Corporation,GOLD,Canada,Materials,CA0679011084
447 | Scientific & Technical Instruments,Fortive Corporation,FTV,United States,Technology,US34959J1088
448 | Information Technology Services,"Broadridge Financial Solutions, Inc.",BR,United States,Technology,US11133T1034
449 | Gold,Wheaton Precious Metals Corp.,WPM,Canada,Materials,CA9628791027
450 | Specialty Industrial Machinery,Dover Corporation,DOV,United States,Industrials,US2600031080
451 | Software - Application,Zoom Communications Inc.,ZM,United States,Technology,US98980L1017
452 | REIT - Residential,Equity Residential,EQR,United States,Real Estate,US29476L1070
453 | Entertainment,"TKO Group Holdings, Inc.",TKO,United States,Communication Services,US87256C1018
454 | Capital Markets,LPL Financial Holdings Inc.,LPLA,United States,Financials,US50212V1008
455 | Oil & Gas Integrated,Cenovus Energy Inc.,CVE,Canada,Energy,CA15135U1093
456 | Software - Application,"Tyler Technologies, Inc.",TYL,United States,Technology,US9022521051
457 | Specialty Retail,"Williams-Sonoma, Inc.",WSM,United States,Consumer Discretionary,US9699041011
458 | Software - Infrastructure,"Corpay, Inc.",CPAY,United States,Technology,US2199481068
459 | Household & Personal Products,"Church & Dwight Co., Inc.",CHD,United States,Consumer Staples,US1713401024
460 | Mortgage Finance,"Rocket Companies, Inc.",RKT,United States,Financials,US77311W1018
461 | Information Technology Services,CDW Corporation,CDW,United States,Technology,US12514G1085
462 | Agricultural Inputs,Nutrien Ltd.,NTR,Canada,Materials,CA67077M1086
463 | Credit Services,Synchrony Financial,SYF,United States,Financials,US87165B1035
464 | Communication Equipment,Telefonaktiebolaget LM Ericsson (publ),ERIC,Sweden,Technology,US2948216088
465 | Information Technology Services,CGI Inc.,GIB,Canada,Technology,CA12532H1047
466 | REIT - Healthcare Facilities,"Ventas, Inc.",VTR,United States,Real Estate,US92276F1003
467 | Asset Management,"T. Rowe Price Group, Inc.",TROW,United States,Financials,US74144T1088
468 | Asset Management,Brookfield Asset Management Ltd.,BAM,Canada,Financials,CA1130041058
469 | Pollution & Treatment Controls,Veralto Corporation,VLTO,United States,Industrials,US92338C1036
470 | Medical Devices,Koninklijke Philips N.V.,PHG,Netherlands,Healthcare,US5004723038
471 | Specialty Chemicals,LyondellBasell Industries N.V.,LYB,United States,Materials,NL0009434992
472 | Gold,Franco-Nevada Corporation,FNV,Canada,Materials,CA3518581051
473 | Entertainment,"Warner Bros. Discovery, Inc.",WBD,United States,Communication Services,US9344231041
474 | Banks - Regional,Huntington Bancshares Incorporated,HBAN,United States,Financials,US4461501045
475 | Utilities - Regulated Electric,Ameren Corporation,AEE,United States,Utilities,US0236081024
476 | Medical Instruments & Supplies,"West Pharmaceutical Services, Inc.",WST,United States,Healthcare,US9553061055
477 | Utilities - Regulated Water,"American Water Works Company, Inc.",AWK,United States,Utilities,US0304201033
478 | Utilities - Regulated Electric,DTE Energy Company,DTE,United States,Utilities,US2333311072
479 | Diagnostics & Research,Waters Corporation,WAT,United States,Healthcare,US9418481035
480 | Drug Manufacturers - Specialty & Generic,Teva Pharmaceutical Industries Limited,TEVA,Israel,Healthcare,US8816242098
481 | Asset Management,TPG Inc.,TPG,United States,Financials,US8726571016
482 | Computer Hardware,"NetApp, Inc.",NTAP,United States,Technology,US64110D1046
483 | Residential Construction,"NVR, Inc.",NVR,United States,Consumer Discretionary,US62944T1051
484 | Utilities - Regulated Electric,PPL Corporation,PPL,United States,Utilities,US69351T1060
485 | Farm Products,Archer-Daniels-Midland Company,ADM,United States,Consumer Staples,US0394831020
486 | Biotechnology,"BeiGene, Ltd.",ONC,Cayman Islands,Healthcare,
487 | Financial Conglomerates,ORIX Corporation,IX,Japan,Financials,US6863301015
488 | Communication Equipment,Ubiquiti Inc.,UI,United States,Technology,US90353W1036
489 | Communication Equipment,Nokia Oyj,NOK,Finland,Technology,US6549022043
490 | Personal Services,"Rollins, Inc.",ROL,United States,Consumer Discretionary,US7757111049
491 | Scientific & Technical Instruments,Teledyne Technologies Incorporated,TDY,United States,Technology,US8793601050
492 | Entertainment,Formula One Group,FWONK,United States,Communication Services,US5312297550
493 | Building Products & Equipment,Lennox International Inc.,LII,United States,Industrials,US5261071071
494 | Oil & Gas Exploration & Production,Expand Energy Corporation,EXE,United States,Energy,US1651677353
495 | Residential Construction,"PulteGroup, Inc.",PHM,United States,Consumer Discretionary,US7458671010
496 | Insurance - Property & Casualty,Markel Group Inc.,MKL,United States,Financials,US5705351048
497 | Semiconductors,"ASE Technology Holding Co., Ltd.",ASX,Taiwan,Technology,US00215W1009
498 | Entertainment,Formula One Group,FWONA,United States,Communication Services,US5312297717
499 | Oil & Gas Equipment & Services,Halliburton Company,HAL,United States,Energy,US4062161017
500 | Banks - Regional,KB Financial Group Inc.,KB,South Korea,Financials,US48241A1051
501 | Auto Manufacturers,Li Auto Inc.,LI,China,Consumer Discretionary,US50202M1027
502 | Utilities - Regulated Electric,FirstEnergy Corp.,FE,United States,Utilities,US3379321074
503 | Airlines,Ryanair Holdings plc,RYAAY,Ireland,Industrials,US7835132033
504 | Telecom Services,"Telefónica, S.A.",TEF,Spain,Communication Services,US8793822086
505 | Software - Application,PTC Inc.,PTC,United States,Technology,US69370C1009
506 | Semiconductors,ON Semiconductor Corporation,ON,United States,Technology,US6821891057
507 | Oil & Gas Exploration & Production,Devon Energy Corporation,DVN,United States,Energy,US25179M1036
508 | Entertainment,Fox Corporation,FOXA,United States,Communication Services,US35137L1052
509 | Semiconductors,GlobalFoundries Inc.,GFS,United States,Technology,KYG393871085
510 | Software - Infrastructure,"Toast, Inc.",TOST,United States,Technology,US8887871080
511 | Capital Markets,"Interactive Brokers Group, Inc.",IBKR,United States,Financials,US45841N1072
512 | Insurance - Property & Casualty,W. R. Berkley Corporation,WRB,United States,Financials,US0844231029
513 | Software - Infrastructure,Twilio Inc.,TWLO,United States,Technology,US90138F1021
514 | Restaurants,"Darden Restaurants, Inc.",DRI,United States,Consumer Discretionary,US2371941053
515 | Banks - Regional,Regions Financial Corporation,RF,United States,Financials,US7591EP1005
516 | REIT - Specialty,Weyerhaeuser Company,WY,United States,Real Estate,US9621661043
517 | Software - Infrastructure,Check Point Software Technologies Ltd.,CHKP,Israel,Technology,IL0010824113
518 | Entertainment,Fox Corporation,FOX,United States,Communication Services,US35137L2043
519 | Medical Devices,"Zimmer Biomet Holdings, Inc.",ZBH,United States,Healthcare,US98956P1021
520 | Internet Content & Information,"Pinterest, Inc.",PINS,United States,Communication Services,US72352L1061
521 | Diagnostics & Research,"Natera, Inc.",NTRA,United States,Healthcare,US6323071042
522 | Electrical Equipment & Parts,Hubbell Incorporated,HUBB,United States,Industrials,US4435106079
523 | Specialty Chemicals,International Flavors & Fragrances Inc.,IFF,United States,Materials,US4595061015
524 | Semiconductors,STMicroelectronics N.V.,STM,Netherlands,Technology,US8610121027
525 | Travel Services,"Expedia Group, Inc.",EXPE,United States,Consumer Discretionary,US30212P3038
526 | Telecom Services,TELUS Corporation,TU,Canada,Communication Services,CA87971M1032
527 | Asset Management,Northern Trust Corporation,NTRS,United States,Financials,US6658591044
528 | Utilities - Regulated Gas,Atmos Energy Corporation,ATO,United States,Utilities,US0495601058
529 | Medical Devices,STERIS plc,STE,United States,Healthcare,IE00BFY8C754
530 | Telecom Services,BCE Inc.,BCE,Canada,Communication Services,CA05534B7604
531 | Computer Hardware,"Pure Storage, Inc.",PSTG,United States,Technology,US74624M1027
532 | Insurance - Property & Casualty,Cincinnati Financial Corporation,CINF,United States,Financials,US1720621010
533 | Computer Hardware,Western Digital Corporation,WDC,United States,Technology,US9581021055
534 | Utilities - Regulated Electric,Edison International,EIX,United States,Utilities,US2810201077
535 | REIT - Specialty,SBA Communications Corporation,SBAC,United States,Real Estate,US78410G1040
536 | Telecom Services,Vodafone Group Public Limited Company,VOD,United Kingdom,Communication Services,US92857W3088
537 | Insurance - Life,Prudential plc,PUK,Hong Kong,Financials,US74435K2042
538 | Utilities - Regulated Electric,Fortis Inc.,FTS,Canada,Utilities,CA3495531079
539 | Financial Data & Stock Exchanges,"Cboe Global Markets, Inc.",CBOE,United States,Financials,US12503M1080
540 | Insurance Brokers,Erie Indemnity Company,ERIE,United States,Financials,US29530P1021
541 | Packaging & Containers,Packaging Corporation of America,PKG,United States,Consumer Discretionary,US6951561090
542 | Computer Hardware,Seagate Technology Holdings plc,STX,Singapore,Technology,IE00BKVD2N49
543 | Drug Manufacturers - General,Biogen Inc.,BIIB,United States,Healthcare,US09062X1037
544 | Diagnostics & Research,"Illumina, Inc.",ILMN,United States,Healthcare,US4523271090
545 | Travel Services,Viking Holdings Ltd,VIK,Bermuda,Consumer Discretionary,BMG93A5A1010
546 | Uranium,Cameco Corporation,CCJ,Canada,Energy,CA13321L1085
547 | Software - Infrastructure,"MongoDB, Inc.",MDB,United States,Technology,US60937P1066
548 | Oil & Gas Midstream,Pembina Pipeline Corporation,PBA,Canada,Energy,CA7063271034
549 | Utilities - Regulated Electric,Eversource Energy,ES,United States,Utilities,US30040W1080
550 | Utilities - Regulated Electric,"CenterPoint Energy, Inc.",CNP,United States,Utilities,US15189T1079
551 | Communication Equipment,Zebra Technologies Corporation,ZBRA,United States,Technology,US9892071054
552 | Other Industrial Metals & Mining,Teck Resources Limited,TECK,Canada,Materials,CA8787422044
553 | Banks - Regional,"Citizens Financial Group, Inc.",CFG,United States,Financials,US1746101054
554 | Diagnostics & Research,Labcorp Holdings Inc.,LH,United States,Healthcare,US50540R4092
555 | Lodging,InterContinental Hotels Group PLC,IHG,United Kingdom,Consumer Discretionary,US45857P8068
556 | Packaged Foods,"McCormick & Company, Incorporated",MKC.V,United States,Consumer Staples,
557 | Packaged Foods,"McCormick & Company, Incorporated",MKC,United States,Consumer Staples,US5797802064
558 | Oil & Gas Exploration & Production,Coterra Energy Inc.,CTRA,United States,Energy,US1270971039
559 | Packaging & Containers,International Paper Company,IP,United States,Consumer Discretionary,US4601461035
560 | Real Estate Services,KE Holdings Inc.,BEKE,China,Real Estate,US4824971042
561 | Oil & Gas Equipment & Services,Tenaris S.A.,TS,Luxembourg,Energy,US88031M1099
562 | Software - Infrastructure,"VeriSign, Inc.",VRSN,United States,Technology,US92343E1029
563 | Gambling,DraftKings Inc.,DKNG,United States,Consumer Discretionary,US26142V1052
564 | Utilities - Independent Power Producers,"NRG Energy, Inc.",NRG,United States,Utilities,US6293775085
565 | Asset Management,The Carlyle Group Inc.,CG,United States,Financials,US14316J1088
566 | Specialty Retail,"DICK'S Sporting Goods, Inc.",DKS,United States,Consumer Discretionary,US2533931026
567 | Engineering & Construction,"EMCOR Group, Inc.",EME,United States,Industrials,US29084Q1004
568 | Banks - Regional,Banco Bradesco S.A.,BBD,Brazil,Financials,US0594603039
569 | Banks - Regional,Banco Bradesco S.A.,BBDO,Brazil,Financials,US0594604029
570 | Farm Products,"Tyson Foods, Inc.",TSN,United States,Consumer Staples,US9024941034
571 | Software - Application,"SS&C Technologies Holdings, Inc.",SSNC,United States,Technology,US78467J1007
572 | Footwear & Accessories,On Holding AG,ONON,Switzerland,Consumer Discretionary,CH1134540470
573 | Semiconductor Equipment & Materials,"Teradyne, Inc.",TER,United States,Technology,US8807701029
574 | Household & Personal Products,The Clorox Company,CLX,United States,Consumer Staples,US1890541097
575 | Software - Application,"DocuSign, Inc.",DOCU,United States,Technology,US2561631068
576 | Medical Instruments & Supplies,"The Cooper Companies, Inc.",COO,United States,Healthcare,US2166485019
577 | Utilities - Regulated Electric,CMS Energy Corporation,CMS,United States,Utilities,US1258961002
578 | Banks - Regional,KeyCorp,KEY,United States,Financials,US4932671088
579 | Building Products & Equipment,"Builders FirstSource, Inc.",BLDR,United States,Industrials,US12008R1077
580 | Internet Content & Information,"Zillow Group, Inc.",Z,United States,Communication Services,US98954M2008
581 | Steel,ArcelorMittal S.A.,MT,Luxembourg,Materials,US03938L2034
582 | Medical Devices,Insulet Corporation,PODD,United States,Healthcare,US45784P1012
583 | Steel,"Steel Dynamics, Inc.",STLD,United States,Materials,US8581191009
584 | Specialty Retail,"Ulta Beauty, Inc.",ULTA,United States,Consumer Discretionary,US90384S3031
585 | Financial Data & Stock Exchanges,TransUnion,TRU,United States,Financials,US89400J1079
586 | REIT - Residential,Invitation Homes Inc.,INVH,United States,Real Estate,US46187W1071
587 | Airlines,Southwest Airlines Co.,LUV,United States,Industrials,US8447411088
588 | Internet Content & Information,"Zillow Group, Inc.",ZG,United States,Communication Services,US98954M1018
589 | Asset Management,"Principal Financial Group, Inc.",PFG,United States,Financials,US74251V1026
590 | Capital Markets,"Nomura Holdings, Inc.",NMR,Japan,Financials,US65535H2085
591 | Information Technology Services,"Leidos Holdings, Inc.",LDOS,United States,Technology,US5253271028
592 | Biotechnology,Royalty Pharma plc,RPRX,United States,Healthcare,GB00BMVP7Y09
593 | Internet Content & Information,Snap Inc.,SNAP,United States,Communication Services,US83304A1060
594 | REIT - Residential,"Essex Property Trust, Inc.",ESS,United States,Real Estate,US2971781057
595 | Insurance - Property & Casualty,Loews Corporation,L,United States,Financials,US5404241086
596 | Asset Management,"Corebridge Financial, Inc.",CRBG,United States,Financials,US21871X1090
597 | Internet Content & Information,Tencent Music Entertainment Group,TME,China,Communication Services,US88034P1093
598 | Software - Infrastructure,Joint Stock Company Kaspi.kz,KSPI,Kazakhstan,Technology,US48581R2058
599 | Specialty Retail,"Best Buy Co., Inc.",BBY,United States,Consumer Discretionary,US0865161014
600 | Software - Infrastructure,CyberArk Software Ltd.,CYBR,Israel,Technology,IL0011334468
601 | Tools & Accessories,Snap-on Incorporated,SNA,United States,Industrials,US8330341012
602 | Scientific & Technical Instruments,Trimble Inc.,TRMB,United States,Technology,US8962391004
603 | Software - Application,Grab Holdings Limited,GRAB,Singapore,Technology,KYG4124C1096
604 | Industrial Distribution,"Watsco, Inc.",WSO,United States,Industrials,US9426222009
605 | Apparel Retail,"Burlington Stores, Inc.",BURL,United States,Consumer Discretionary,US1220171060
606 | Software - Infrastructure,"Nutanix, Inc.",NTNX,United States,Technology,US67059N1081
607 | Industrial Distribution,"Watsco, Inc.",WSO.B,United States,Industrials,US9426221019
608 | REIT - Residential,"Mid-America Apartment Communities, Inc.",MAA,United States,Real Estate,US59522J1034
609 | Software - Infrastructure,"Affirm Holdings, Inc.",AFRM,United States,Technology,US00827B1061
610 | Software - Application,"Manhattan Associates, Inc.",MANH,United States,Technology,US5627501092
611 | Financial Data & Stock Exchanges,FactSet Research Systems Inc.,FDS,United States,Financials,US3030751057
612 | Building Products & Equipment,Carlisle Companies Incorporated,CSL,United States,Industrials,US1423391002
613 | Oil & Gas Integrated,Ecopetrol S.A.,EC,Colombia,Energy,US2791581091
614 | Electronic Components,Jabil Inc.,JBL,United States,Technology,US4663131039
615 | Credit Services,"SoFi Technologies, Inc.",SOFI,United States,Financials,US83406F1021
616 | Banks - Regional,"Shinhan Financial Group Co., Ltd.",SHG,South Korea,Financials,US8245961003
617 | Rental & Leasing Services,AerCap Holdings N.V.,AER,Ireland,Industrials,NL0000687663
618 | Healthcare Plans,"Molina Healthcare, Inc.",MOH,United States,Healthcare,US60855R1005
619 | Diagnostics & Research,Quest Diagnostics Incorporated,DGX,United States,Healthcare,US74834L1008
620 | Leisure,"Amer Sports, Inc.",AS,Finland,Consumer Discretionary,FI0009000285
621 | Specialty Industrial Machinery,Symbotic Inc.,SYM,United States,Industrials,US87151X1019
622 | Integrated Freight & Logistics,"J.B. Hunt Transport Services, Inc.",JBHT,United States,Industrials,US4456581077
623 | Building Products & Equipment,Masco Corporation,MAS,United States,Industrials,US5745991068
624 | Biotechnology,Summit Therapeutics Inc.,SMMT,United States,Healthcare,US86627T1088
625 | Software - Application,"Guidewire Software, Inc.",GWRE,United States,Technology,US40171V1008
626 | Software - Application,"Aspen Technology, Inc.",AZPN,United States,Technology,US29109X1063
627 | Software - Application,"Dynatrace, Inc.",DT,United States,Technology,US2681501092
628 | Biotechnology,"Moderna, Inc.",MRNA,United States,Healthcare,US60770K1079
629 | Restaurants,"Yum China Holdings, Inc.",YUMC,China,Consumer Discretionary,US98850P1093
630 | Solar,"First Solar, Inc.",FSLR,United States,Technology,US3364331070
631 | Insurance - Specialty,"Ryan Specialty Holdings, Inc.",RYAN,United States,Financials,US78351F1075
632 | Software - Infrastructure,Gen Digital Inc.,GEN,United States,Technology,US6687711084
633 | Advertising Agencies,Omnicom Group Inc.,OMC,United States,Communication Services,US6819191064
634 | Oil & Gas Integrated,YPF Sociedad Anónima,YPF,Argentina,Energy,US9842451000
635 | Engineering & Construction,Jacobs Solutions Inc.,J,United States,Industrials,US46982L1089
636 | Utilities - Regulated Gas,NiSource Inc.,NI,United States,Utilities,US65473P1057
637 | Specialty Industrial Machinery,Pentair plc,PNR,United Kingdom,Industrials,IE00BLS09M33
638 | Waste Management,GFL Environmental Inc.,GFL,Canada,Industrials,CA36168Q1046
639 | Luxury Goods,"Tapestry, Inc.",TPR,United States,Consumer Discretionary,US8760301072
640 | Medical Instruments & Supplies,"Align Technology, Inc.",ALGN,United States,Healthcare,US0162551016
641 | REIT - Office,"Alexandria Real Estate Equities, Inc.",ARE,United States,Real Estate,US0152711091
642 | Insurance - Diversified,"Equitable Holdings, Inc.",EQH,United States,Financials,US29452E1010
643 | Specialty Industrial Machinery,IDEX Corporation,IEX,United States,Industrials,US45167R1041
644 | Packaged Foods,Hormel Foods Corporation,HRL,United States,Consumer Staples,US4404521001
645 | Diagnostics & Research,ICON Public Limited Company,ICLR,Ireland,Healthcare,IE0005711209
646 | Medical Instruments & Supplies,Baxter International Inc.,BAX,United States,Healthcare,US0718131099
647 | Specialty Business Services,"RB Global, Inc.",RBA,United States,Industrials,CA74935Q1072
648 | Entertainment,News Corporation,NWS,United States,Communication Services,US65249B2088
649 | Packaging & Containers,Ball Corporation,BALL,United States,Consumer Discretionary,US0584981064
650 | REIT - Residential,"Sun Communities, Inc.",SUI,United States,Real Estate,US8666741041
651 | Biotechnology,United Therapeutics Corporation,UTHR,United States,Healthcare,US91307C1027
652 | Food Distribution,US Foods Holding Corp.,USFD,United States,Consumer Staples,US9120081099
653 | Computer Hardware,"Super Micro Computer, Inc.",SMCI,United States,Technology,US86800U1043
654 | Telecom Services,Perusahaan Perseroan (Persero) PT Telekomunikasi Indonesia Tbk,TLK,Indonesia,Communication Services,US7156841063
655 | Consulting Services,Booz Allen Hamilton Holding Corporation,BAH,United States,Industrials,US0995021062
656 | Farm & Heavy Construction Machinery,CNH Industrial N.V.,CNH,United Kingdom,Industrials,NL0010545661
657 | Entertainment,Warner Music Group Corp.,WMG,United States,Communication Services,US9345502036
658 | Building Products & Equipment,Owens Corning,OC,United States,Industrials,US6907421019
659 | Specialty Chemicals,RPM International Inc.,RPM,United States,Materials,US7496851038
660 | Auto Parts,Genuine Parts Company,GPC,United States,Consumer Discretionary,US3724601055
661 | Trucking,"XPO, Inc.",XPO,United States,Industrials,US9837931008
662 | Beverages - Non-Alcoholic,"Coca-Cola FEMSA, S.A.B. de C.V.",KOF,Mexico,Consumer Staples,US1912411089
663 | Software - Infrastructure,"Okta, Inc.",OKTA,United States,Technology,US6792951054
664 | Medical Instruments & Supplies,"Hologic, Inc.",HOLX,United States,Healthcare,US4364401012
665 | Discount Stores,"Dollar Tree, Inc.",DLTR,United States,Consumer Staples,US2567461080
666 | Discount Stores,Dollar General Corporation,DG,United States,Consumer Staples,US2566771059
667 | Apparel Manufacturing,Ralph Lauren Corporation,RL,United States,Consumer Discretionary,US7512121010
668 | Integrated Freight & Logistics,"Expeditors International of Washington, Inc.",EXPD,United States,Industrials,US3021301094
669 | Entertainment,News Corporation,NWSA,United States,Communication Services,US65249B1098
670 | Banks - Regional,Banco Santander (Brasil) S.A.,BSBR,Brazil,Financials,US05967A1079
671 | Oil & Gas Midstream,"Western Midstream Partners, LP",WES,United States,Energy,US9586691035
672 | Telecom Services,Rogers Communications Inc.,RCI,Canada,Communication Services,CA7751092007
673 | Internet Retail,"Chewy, Inc.",CHWY,United States,Consumer Discretionary,US16679L1098
674 | Insurance - Specialty,"Fidelity National Financial, Inc.",FNF,United States,Financials,US31620R3030
675 | Steel,"Reliance, Inc.",RS,United States,Materials,US7595091023
676 | Insurance - Reinsurance,"Everest Group, Ltd.",EG,Bermuda,Financials,BMG3223R1088
677 | Electronic Components,Flex Ltd.,FLEX,United States,Technology,SG9999000020
678 | Agricultural Inputs,"CF Industries Holdings, Inc.",CF,United States,Materials,US1252691001
679 | "Furnishings, Fixtures & Appliances","SharkNinja, Inc.",SN,United States,Consumer Discretionary,KYG8068L1086
680 | Capital Markets,Jefferies Financial Group Inc.,JEF,United States,Financials,US47233W1099
681 | Software - Infrastructure,"F5, Inc.",FFIV,United States,Technology,US3156161024
682 | Beverages - Wineries & Distilleries,Brown-Forman Corporation,BF.B,United States,Consumer Staples,US1156372096
683 | Beverages - Wineries & Distilleries,Brown-Forman Corporation,BF.A,United States,Consumer Staples,US1156371007
684 | Packaging & Containers,Avery Dennison Corporation,AVY,United States,Consumer Discretionary,US0536111091
685 | REIT - Retail,Kimco Realty Corporation,KIM,United States,Real Estate,US49446R1095
686 | Specialty Retail,"Casey's General Stores, Inc.",CASY,United States,Consumer Discretionary,US1475281036
687 | Software - Application,"Duolingo, Inc.",DUOL,United States,Technology,US26603R1068
688 | Semiconductors,United Microelectronics Corporation,UMC,Taiwan,Technology,US9108734057
689 | REIT - Residential,"UDR, Inc.",UDR,United States,Real Estate,US9026531049
690 | Diagnostics & Research,"Revvity, Inc.",RVTY,United States,Healthcare,US7140461093
691 | Medical Instruments & Supplies,"Avantor, Inc.",AVTR,United States,Healthcare,US05352A1007
692 | Drug Manufacturers - Specialty & Generic,"Neurocrine Biosciences, Inc.",NBIX,United States,Healthcare,US64125C1099
693 | Utilities - Diversified,Brookfield Infrastructure Partners L.P.,BIP,Bermuda,Utilities,BMG162521014
694 | Grocery Stores,"Sprouts Farmers Market, Inc.",SFM,United States,Consumer Staples,US85208M1027
695 | Asset Management,Ares Capital Corporation,ARCC,United States,Financials,US04010L1035
696 | Lodging,Hyatt Hotels Corporation,H,United States,Consumer Discretionary,US4485791028
697 | Integrated Freight & Logistics,ZTO Express (Cayman) Inc.,ZTO,China,Industrials,US98980A1051
698 | Insurance - Reinsurance,"Reinsurance Group of America, Incorporated",RGA,United States,Financials,US7593516047
699 | Utilities - Regulated Electric,Alliant Energy Corporation,LNT,United States,Utilities,US0188021085
700 | Software - Infrastructure,"Akamai Technologies, Inc.",AKAM,United States,Technology,US00971T1016
701 | REIT - Industrial,"Lineage, Inc.",LINE,United States,Real Estate,US53566V1061
702 | Specialty Chemicals,Westlake Corporation,WLK,United States,Materials,US9604131022
703 | Restaurants,"Domino's Pizza, Inc.",DPZ,United States,Consumer Discretionary,US25754A2015
704 | REIT - Residential,American Homes 4 Rent,AMH,United States,Real Estate,US02665T3068
705 | Engineering & Construction,"Comfort Systems USA, Inc.",FIX,United States,Industrials,US1999081045
706 | Auto Parts,Aptiv PLC,APTV,Switzerland,Consumer Discretionary,JE00B783TY65
707 | REIT - Healthcare Facilities,"Healthpeak Properties, Inc.",DOC,United States,Real Estate,US71943U1043
708 | Semiconductor Equipment & Materials,"Entegris, Inc.",ENTG,United States,Technology,US29362U1043
709 | Software - Application,"Bentley Systems, Incorporated",BSY,United States,Technology,US08265T2087
710 | ,"Bentley Systems, Incorporated",BSS,,,
711 | Entertainment,"Endeavor Group Holdings, Inc.",EDR,United States,Communication Services,US29260Y1091
712 | Gold,Gold Fields Limited,GFI,South Africa,Materials,US38059T1060
713 | Utilities - Regulated Electric,"Evergy, Inc.",EVRG,United States,Utilities,US30034W1062
714 | Aerospace & Defense,"Rocket Lab USA, Inc.",RKLB,United States,Industrials,US7731221062
715 | Information Technology Services,"EPAM Systems, Inc.",EPAM,United States,Technology,US29414B1044
716 | Oil & Gas Midstream,"Plains All American Pipeline, L.P.",PAA,United States,Energy,US7265031051
717 | Restaurants,"CAVA Group, Inc.",CAVA,United States,Consumer Discretionary,US1489291021
718 | Building Materials,James Hardie Industries plc,JHX,Ireland,Materials,US47030M1062
719 | Banks - Regional,Credicorp Ltd.,BAP,Peru,Financials,BMG2519Y1084
720 | Medical Care Facilities,Fresenius Medical Care AG,FMS,Germany,Healthcare,US3580291066
721 | Semiconductors,"Skyworks Solutions, Inc.",SWKS,United States,Technology,US83088M1027
722 | Auto Manufacturers,XPeng Inc.,XPEV,China,Consumer Discretionary,US98422D1054
723 | Telecom Services,Telefônica Brasil S.A.,VIV,Brazil,Communication Services,US87936R2058
724 | Rental & Leasing Services,U-Haul Holding Company,UHAL,United States,Industrials,US0235861004
725 | Banks - Regional,"East West Bancorp, Inc.",EWBC,United States,Financials,US27579R1041
726 | Aerospace & Defense,Textron Inc.,TXT,United States,Industrials,US8832031012
727 | Semiconductors,"Astera Labs, Inc.",ALAB,United States,Technology,US04626A1034
728 | Medical Care Facilities,DaVita Inc.,DVA,United States,Healthcare,US23918K1088
729 | Gold,AngloGold Ashanti plc,AU,United States,Materials,US0351282068
730 | Financial Data & Stock Exchanges,"Morningstar, Inc.",MORN,United States,Financials,US6177001095
731 | Packaging & Containers,Amcor plc,AMCR,Switzerland,Consumer Discretionary,JE00BJ1F3079
732 | Specialty Industrial Machinery,Graco Inc.,GGG,United States,Industrials,US3841091040
733 | Biotechnology,Incyte Corporation,INCY,United States,Healthcare,US45337C1027
734 | Biotechnology,Insmed Incorporated,INSM,United States,Healthcare,US4576693075
735 | Food Distribution,Performance Food Group Company,PFGC,United States,Consumer Staples,US71377A1034
736 | Engineering & Construction,AECOM,ACM,United States,Industrials,US00766T1007
737 | Utilities - Renewable,Centrais Elétricas Brasileiras S.A. - Eletrobrás,EBR,Brazil,Utilities,US15234Q2075
738 | Insurance - Life,Unum Group,UNM,United States,Financials,US91529Y1064
739 | REIT - Specialty,"Gaming and Leisure Properties, Inc.",GLPI,United States,Real Estate,US36467J1088
740 | Software - Infrastructure,Wix.com Ltd.,WIX,Israel,Technology,IL0011301780
741 | Steel,POSCO Holdings Inc.,PKX,South Korea,Materials,US6934831099
742 | Residential Construction,"Toll Brothers, Inc.",TOL,United States,Consumer Discretionary,US8894781033
743 | Capital Markets,Futu Holdings Limited,FUTU,Hong Kong,Financials,US36118L1061
744 | Tools & Accessories,"Stanley Black & Decker, Inc.",SWK,United States,Industrials,US8545021011
745 | Software - Infrastructure,"Rubrik, Inc.",RBRK,United States,Technology,US7811541090
746 | Auto Parts,Mobileye Global Inc.,MBLY,Israel,Consumer Discretionary,US60741F1049
747 | Computer Hardware,Logitech International S.A.,LOGI,Switzerland,Technology,CH0025751329
748 | Drug Manufacturers - Specialty & Generic,"Intra-Cellular Therapies, Inc.",ITCI,United States,Healthcare,US46116X1019
749 | Insurance - Property & Casualty,CNA Financial Corporation,CNA,United States,Financials,US1261171003
750 | Drug Manufacturers - Specialty & Generic,Viatris Inc.,VTRS,United States,Healthcare,US92556V1061
751 | Gold,Kinross Gold Corporation,KGC,Canada,Materials,CA4969024047
752 | Real Estate Services,Jones Lang LaSalle Incorporated,JLL,United States,Real Estate,US48020Q1076
753 | REIT - Residential,"Equity LifeStyle Properties, Inc.",ELS,United States,Real Estate,US29472R1086
754 | Industrial Distribution,Pool Corporation,POOL,United States,Industrials,US73278L1052
755 | Medical Care Facilities,Tenet Healthcare Corporation,THC,United States,Healthcare,US88033G4073
756 | Paper & Paper Products,Suzano S.A.,SUZ,Brazil,Materials,US86959K1051
757 | REIT - Retail,Regency Centers Corporation,REG,United States,Real Estate,US7588491032
758 | Software - Application,monday.com Ltd.,MNDY,Israel,Technology,IL0011762130
759 | Aerospace & Defense,Elbit Systems Ltd.,ESLT,Israel,Industrials,IL0010811243
760 | Trucking,"Saia, Inc.",SAIA,United States,Industrials,US78709Y1055
761 | Auto & Truck Dealerships,"CarMax, Inc.",KMX,United States,Consumer Discretionary,US1431301027
762 | Oil & Gas Equipment & Services,TechnipFMC plc,FTI,United States,Energy,GB00BDSFG982
763 | Discount Stores,"BJ's Wholesale Club Holdings, Inc.",BJ,United States,Consumer Staples,US05550J1016
764 | Insurance - Reinsurance,RenaissanceRe Holdings Ltd.,RNR,Bermuda,Financials,BMG7496G1033
765 | Integrated Freight & Logistics,"C.H. Robinson Worldwide, Inc.",CHRW,United States,Industrials,US12541W2098
766 | Auto Manufacturers,"Rivian Automotive, Inc.",RIVN,United States,Consumer Discretionary,US76954A1034
767 | Rental & Leasing Services,U-Haul Holding Company,UHAL.B,United States,Industrials,US0235865062
768 | REIT - Specialty,Lamar Advertising Company,LAMR,United States,Real Estate,US5128161099
769 | Health Information Services,Solventum Corporation,SOLV,United States,Healthcare,US83444M1018
770 | Capital Markets,"Houlihan Lokey, Inc.",HLI,United States,Financials,US4415931009
771 | REIT - Office,"BXP, Inc.",BXP,United States,Real Estate,US1011211018
772 | Aerospace & Defense,Curtiss-Wright Corporation,CW,United States,Industrials,US2315611010
773 | Information Technology Services,"Jack Henry & Associates, Inc.",JKHY,United States,Technology,US4262811015
774 | Scientific & Technical Instruments,Coherent Corp.,COHR,United States,Technology,US19247G1076
775 | Waste Management,"Clean Harbors, Inc.",CLH,United States,Industrials,US1844961078
776 | Medical Devices,"Globus Medical, Inc.",GMED,United States,Healthcare,US3795772082
777 | Specialty Industrial Machinery,Nordson Corporation,NDSN,United States,Industrials,US6556631025
778 | Travel Services,Norwegian Cruise Line Holdings Ltd.,NCLH,United States,Consumer Discretionary,BMG667211046
779 | Beverages - Non-Alcoholic,Primo Brands Corporation,PRMB,United States,Consumer Staples,US7416231022
780 | Medical Care Facilities,"Universal Health Services, Inc.",UHS,United States,Healthcare,US9139031002
781 | Software - Infrastructure,"Klaviyo, Inc.",KVYO,United States,Technology,US49845K1016
782 | Specialty Retail,GameStop Corp.,GME,United States,Consumer Discretionary,US36467W1099
783 | Banks - Regional,Banco de Chile,BCH,Chile,Financials,US0595201064
784 | Packaged Foods,"Conagra Brands, Inc.",CAG,United States,Consumer Staples,US2058871029
785 | REIT - Residential,Camden Property Trust,CPT,United States,Real Estate,US1331311027
786 | REIT - Diversified,W. P. Carey Inc.,WPC,United States,Real Estate,US92936U1097
787 | Specialty Business Services,Rentokil Initial plc,RTO,United Kingdom,Industrials,US7601251041
788 | Software - Application,"Procore Technologies, Inc.",PCOR,United States,Technology,US74275K1088
789 | Software - Application,Elastic N.V.,ESTC,Netherlands,Technology,NL0013056914
790 | Biotechnology,Genmab A/S,GMAB,Denmark,Healthcare,US3723032062
791 | Restaurants,"Texas Roadhouse, Inc.",TXRH,United States,Consumer Discretionary,US8826811098
792 | Biotechnology,BioMarin Pharmaceutical Inc.,BMRN,United States,Healthcare,US09061G1013
793 | Communication Equipment,"Juniper Networks, Inc.",JNPR,United States,Technology,US48203R1041
794 | Internet Retail,Maplebear Inc.,CART,United States,Consumer Discretionary,US5653941030
795 | Electronics & Computer Distribution,TD SYNNEX Corporation,SNX,United States,Technology,US87162W1009
796 | Software - Application,Full Truck Alliance Co. Ltd.,YMM,China,Technology,US35969L1089
797 | Entertainment,"Roku, Inc.",ROKU,United States,Communication Services,US77543R1023
798 | Oil & Gas Exploration & Production,Permian Resources Corporation,PR,United States,Energy,US71424F1057
799 | Software - Application,"Paycom Software, Inc.",PAYC,United States,Technology,US70432V1026
800 | Specialty Industrial Machinery,ITT Inc.,ITT,United States,Industrials,US45073V1089
801 | Credit Services,Ally Financial Inc.,ALLY,United States,Financials,US02005N1000
802 | REIT - Hotel & Motel,"Host Hotels & Resorts, Inc.",HST,United States,Real Estate,US44107P1049
803 | Biotechnology,Bio-Techne Corporation,TECH,United States,Healthcare,US09073M1045
804 | Auto Parts,Magna International Inc.,MGA,Canada,Consumer Discretionary,CA5592224011
805 | Software - Infrastructure,GitLab Inc.,GTLB,United States,Technology,US37637K1088
806 | Capital Markets,Stifel Financial Corp.,SF,United States,Financials,US8606301021
807 | Banks - Regional,Grupo Financiero Galicia S.A.,GGAL,Argentina,Financials,US3999091008
808 | Travel Services,MakeMyTrip Limited,MMYT,India,Consumer Discretionary,MU0295S00016
809 | Packaged Foods,The Campbell's Company,CPB,United States,Consumer Staples,US1344291091
810 | Beverages - Non-Alcoholic,"Coca-Cola Consolidated, Inc.",COKE,United States,Consumer Staples,US1910981026
811 | Personal Services,Service Corporation International,SCI,United States,Consumer Discretionary,US8175651046
812 | Software - Application,Paylocity Holding Corporation,PCTY,United States,Technology,US70438V1061
813 | Trucking,TFI International Inc.,TFII,Canada,Industrials,CA87241L1094
814 | Software - Application,Dayforce Inc.,DAY,United States,Technology,US15677J1088
815 | Information Technology Services,"Aurora Innovation, Inc.",AUR,United States,Technology,US0517741072
816 | Footwear & Accessories,"Skechers U.S.A., Inc.",SKX,United States,Consumer Discretionary,US8305661055
817 | Capital Markets,Evercore Inc.,EVR,United States,Financials,US29977A1051
818 | Oil & Gas Exploration & Production,Antero Resources Corporation,AR,United States,Energy,US03674X1063
819 | Telecom Services,Liberty Broadband Corporation,LBRDK,United States,Communication Services,US5303073051
820 | Telecom Services,Liberty Broadband Corporation,LBRDA,United States,Communication Services,US5303071071
821 | Insurance - Property & Casualty,"American Financial Group, Inc.",AFG,United States,Financials,US0259321042
822 | Grocery Stores,"Albertsons Companies, Inc.",ACI,United States,Consumer Staples,US0130911037
823 | Security & Protection Services,Allegion plc,ALLE,Ireland,Industrials,IE00BFRT3W74
824 | Biotechnology,"Vaxcyte, Inc.",PCVX,United States,Healthcare,US92243G1085
825 | Footwear & Accessories,Birkenstock Holding plc,BIRK,United Kingdom,Consumer Discretionary,JE00BS44BN30
826 | Oil & Gas Exploration & Production,Ovintiv Inc.,OVV,United States,Energy,US69047Q1022
827 | Communication Equipment,Ciena Corporation,CIEN,United States,Technology,US1717793095
828 | Drug Manufacturers - Specialty & Generic,Dr. Reddy's Laboratories Limited,RDY,India,Healthcare,US2561352038
829 | Beverages - Brewers,Molson Coors Beverage Company,TAP.A,United States,Consumer Staples,US60871R1005
830 | Beverages - Brewers,Molson Coors Beverage Company,TAP,United States,Consumer Staples,US60871R2094
831 | Airlines,American Airlines Group Inc.,AAL,United States,Industrials,US02376R1023
832 | Industrial Distribution,"Core & Main, Inc.",CNM,United States,Industrials,US21874C1027
833 | Biotechnology,"Sarepta Therapeutics, Inc.",SRPT,United States,Healthcare,US8036071004
834 | Packaged Foods,The J. M. Smucker Company,SJM,United States,Consumer Staples,US8326964058
835 | Banks - Regional,First Horizon Corporation,FHN,United States,Financials,US3205171057
836 | REIT - Mortgage,"Annaly Capital Management, Inc.",NLY,United States,Real Estate,US0357108390
837 | Home Improvement Retail,"Floor & Decor Holdings, Inc.",FND,United States,Consumer Discretionary,US3397501012
838 | Specialty Chemicals,Sociedad Química y Minera de Chile S.A.,SQM,Chile,Materials,US8336351056
839 | Medical Devices,Smith & Nephew plc,SNN,United Kingdom,Healthcare,US83175M2052
840 | Tools & Accessories,"Lincoln Electric Holdings, Inc.",LECO,United States,Industrials,US5339001068
841 | Insurance - Property & Casualty,"Assurant, Inc.",AIZ,United States,Financials,US04621X1081
842 | Auto & Truck Dealerships,"Penske Automotive Group, Inc.",PAG,United States,Consumer Discretionary,US70959W1036
843 | Utilities - Regulated Water,Companhia de Saneamento Básico do Estado de São Paulo - SABESP,SBS,Brazil,Utilities,US20441A1025
844 | Electronic Components,Celestica Inc.,CLS,Canada,Technology,CA15101Q1081
845 | Aerospace & Defense,"Woodward, Inc.",WWD,United States,Industrials,US9807451037
846 | Packaged Foods,Pilgrim's Pride Corporation,PPC,United States,Consumer Staples,US72147K1088
847 | Banks - Regional,SouthState Corporation,SSB,United States,Financials,US8404411097
848 | Asset Management,SEI Investments Company,SEIC,United States,Financials,US7841171033
849 | Farm Products,Bunge Global SA,BG,United States,Consumer Staples,CH1300646267
850 | Specialty Business Services,UL Solutions Inc.,ULS,United States,Industrials,US9037311076
851 | Advertising Agencies,"The Interpublic Group of Companies, Inc.",IPG,United States,Communication Services,US4606901001
852 | Specialty Chemicals,Eastman Chemical Company,EMN,United States,Materials,US2774321002
853 | Publishing,Pearson plc,PSO,United Kingdom,Communication Services,US7050151056
854 | Diagnostics & Research,"Medpace Holdings, Inc.",MEDP,United States,Healthcare,US58506Q1094
855 | Health Information Services,"Doximity, Inc.",DOCS,United States,Healthcare,US26622P1075
856 | Software - Application,NICE Ltd.,NICE,Israel,Technology,US6536561086
857 | Specialty Industrial Machinery,Regal Rexnord Corporation,RRX,United States,Industrials,US7587501039
858 | Asset Management,"Franklin Resources, Inc.",BEN,United States,Financials,US3546131018
859 | Software - Infrastructure,"Shift4 Payments, Inc.",FOUR,United States,Technology,US82452J1097
860 | Restaurants,Dutch Bros Inc.,BROS,United States,Consumer Discretionary,US26701L1008
861 | Medical Instruments & Supplies,"AptarGroup, Inc.",ATR,United States,Healthcare,US0383361039
862 | "Furnishings, Fixtures & Appliances","Tempur Sealy International, Inc.",TPX,United States,Consumer Discretionary,US88023U1016
863 | Engineering & Construction,"MasTec, Inc.",MTZ,United States,Industrials,US5763231090
864 | Packaging & Containers,"Crown Holdings, Inc.",CCK,United States,Consumer Discretionary,US2283681060
865 | Insurance - Diversified,Aegon Ltd.,AEG,Netherlands,Financials,US0076CA1045
866 | REIT - Healthcare Facilities,"Omega Healthcare Investors, Inc.",OHI,United States,Real Estate,US6819361006
867 | Specialty Business Services,Aramark,ARMK,United States,Industrials,US03852U1060
868 | Electrical Equipment & Parts,nVent Electric plc,NVT,United Kingdom,Industrials,IE00BDVJJQ56
869 | Insurance - Diversified,Brookfield Wealth Solutions Ltd.,BNT,Bermuda,Financials,BMG174341047
870 | Medical Devices,"Penumbra, Inc.",PEN,United States,Healthcare,US70975L1070
871 | Engineering & Construction,"Tetra Tech, Inc.",TTEK,United States,Industrials,US88162G1031
872 | Apparel Manufacturing,V.F. Corporation,VFC,United States,Consumer Discretionary,US9182041080
873 | Lodging,H World Group Limited,HTHT,China,Consumer Discretionary,US44332N1063
874 | Real Estate - Development,Murano Global Investments Plc,MRNO,United Kingdom,Real Estate,JE00BQ7X4L23
875 | Insurance - Property & Casualty,"Kinsale Capital Group, Inc.",KNSL,United States,Financials,US49714P1084
876 | Engineering & Construction,APi Group Corporation,APG,United States,Industrials,US00187Y1001
877 | Metal Fabrication,Carpenter Technology Corporation,CRS,United States,Industrials,US1442851036
878 | Medical Devices,"Bio-Rad Laboratories, Inc.",BIO,United States,Healthcare,US0905722072
879 | Rental & Leasing Services,FTAI Aviation Ltd.,FTAI,United States,Industrials,KYG3730V1059
880 | Diagnostics & Research,Exact Sciences Corporation,EXAS,United States,Healthcare,US30063P1057
881 | Aerospace & Defense,"BWX Technologies, Inc.",BWXT,United States,Industrials,US05605H1005
882 | Medical Devices,"Bio-Rad Laboratories, Inc.",BIO.B,United States,Healthcare,US0905721082
883 | Software - Infrastructure,"Confluent, Inc.",CFLT,United States,Technology,US20717M1036
884 | Insurance - Life,Globe Life Inc.,GL,United States,Financials,US37959E1029
885 | Banks - Regional,Webster Financial Corporation,WBS,United States,Financials,US9478901096
886 | Specialty Industrial Machinery,A. O. Smith Corporation,AOS,United States,Industrials,US8318652091
887 | Software - Infrastructure,"Dropbox, Inc.",DBX,United States,Technology,US26210C1045
888 | Specialty Chemicals,Albemarle Corporation,ALB,United States,Materials,US0126531013
889 | Advertising Agencies,WPP plc,WPP,United Kingdom,Communication Services,US92937A1025
890 | Packaged Foods,"BellRing Brands, Inc.",BRBR,United States,Consumer Staples,US07831C1036
891 | Software - Application,The Descartes Systems Group Inc.,DSGX,Canada,Technology,CA2499061083
892 | Specialty Industrial Machinery,Crane Company,CR,United States,Industrials,US2244081046
893 | Internet Retail,Global-E Online Ltd.,GLBE,Israel,Consumer Discretionary,IL0011741688
894 | Software - Application,"BILL Holdings, Inc.",BILL,United States,Technology,US0900431000
895 | Electrical Equipment & Parts,"Acuity Brands, Inc.",AYI,United States,Industrials,US00508Y1029
896 | Mortgage Finance,UWM Holdings Corporation,UWMC,United States,Financials,US91823B1098
897 | Oil & Gas Midstream,"DT Midstream, Inc.",DTM,United States,Energy,US23345M1071
898 | Specialty Retail,Murphy USA Inc.,MUSA,United States,Consumer Discretionary,US6267551025
899 | Engineering & Construction,TopBuild Corp.,BLD,United States,Industrials,US89055F1030
900 | Auto Parts,"Allison Transmission Holdings, Inc.",ALSN,United States,Consumer Discretionary,US01973R1014
901 | Oil & Gas Midstream,Kinetik Holdings Inc.,KNTK,United States,Energy,US02215L2097
902 | Resorts & Casinos,MGM Resorts International,MGM,United States,Consumer Discretionary,US5529531015
903 | Auto Parts,LKQ Corporation,LKQ,United States,Consumer Discretionary,US5018892084
904 | Tools & Accessories,RBC Bearings Incorporated,RBC,United States,Industrials,US75524B1044
905 | Utilities - Regulated Electric,Pinnacle West Capital Corporation,PNW,United States,Utilities,US7234841010
906 | Utilities - Regulated Water,"Essential Utilities, Inc.",WTRG,United States,Utilities,US29670G1022
907 | Auto & Truck Dealerships,"Lithia Motors, Inc.",LAD,United States,Consumer Discretionary,US5367971034
908 | Software - Infrastructure,Amdocs Limited,DOX,United States,Technology,GB0022569080
909 | Medical Instruments & Supplies,Repligen Corporation,RGEN,United States,Healthcare,US7599161095
910 | Diagnostics & Research,Qiagen N.V.,QGEN,Netherlands,Healthcare,NL0015001WM6
911 | Medical Care Facilities,Encompass Health Corporation,EHC,United States,Healthcare,US29261A1007
912 | Banks - Regional,Western Alliance Bancorporation,WAL,United States,Financials,US9576381092
913 | Semiconductors,Credo Technology Group Holding Ltd,CRDO,Cayman Islands,Technology,KYG254571055
914 | Utilities - Renewable,Brookfield Renewable Partners L.P.,BEP,Canada,Utilities,BMG162581083
915 | Industrial Distribution,"Applied Industrial Technologies, Inc.",AIT,United States,Industrials,US03820C1053
916 | Insurance - Life,"Primerica, Inc.",PRI,United States,Financials,US74164M1080
917 | Building Products & Equipment,"Advanced Drainage Systems, Inc.",WMS,United States,Industrials,US00790R1041
918 | Software - Application,Pegasystems Inc.,PEGA,United States,Technology,US7055731035
919 | REIT - Industrial,CubeSmart,CUBE,United States,Real Estate,US2296631094
920 | Banks - Regional,"Pinnacle Financial Partners, Inc.",PNFP,United States,Financials,US72346Q1040
921 | Banks - Regional,Bancolombia S.A.,CIB,Colombia,Financials,US05968L1026
922 | Medical Distribution,"Henry Schein, Inc.",HSIC,United States,Healthcare,US8064071025
923 | REIT - Industrial,"Rexford Industrial Realty, Inc.",REXR,United States,Real Estate,US76169C1009
924 | Trucking,Knight-Swift Transportation Holdings Inc.,KNX,United States,Industrials,US4990491049
925 | Aerospace & Defense,"Leonardo DRS, Inc.",DRS,United States,Industrials,US52661A1088
926 | Utilities - Regulated Electric,Korea Electric Power Corporation,KEP,South Korea,Utilities,US5006311063
927 | Airports & Air Services,"Grupo Aeroportuario del Pacífico, S.A.B. de C.V.",PAC,Mexico,Industrials,US4005061019
928 | Pharmaceutical Retailers,"Walgreens Boots Alliance, Inc.",WBA,United States,Healthcare,US9314271084
929 | Software - Application,Altair Engineering Inc.,ALTR,United States,Technology,US0213691035
930 | Utilities - Independent Power Producers,Talen Energy Corporation,TLN,United States,Utilities,US87422Q1094
931 | Medical Devices,Masimo Corporation,MASI,United States,Healthcare,US5747951003
932 | Software - Application,Unity Software Inc.,U,United States,Technology,US91332U1016
933 | Health Information Services,"HealthEquity, Inc.",HQY,United States,Healthcare,US42226A1079
934 | Apparel Retail,"The Gap, Inc.",GAP,United States,Consumer Discretionary,US3647601083
935 | Banks - Regional,Banco Santander-Chile,BSAC,Chile,Financials,US05965X1090
936 | Biotechnology,"Exelixis, Inc.",EXEL,United States,Healthcare,US30161Q1040
937 | Software - Application,"AppFolio, Inc.",APPF,United States,Technology,US03783C1009
938 | REIT - Retail,Federal Realty Investment Trust,FRT,United States,Real Estate,US3137451015
939 | Specialty Industrial Machinery,The Middleby Corporation,MIDD,United States,Industrials,US5962781010
940 | Gambling,Churchill Downs Incorporated,CHDN,United States,Consumer Discretionary,US1714841087
941 | Software - Application,"ServiceTitan, Inc.",TTAN,United States,Technology,US81764X1037
942 | Insurance - Property & Casualty,Old Republic International Corporation,ORI,United States,Financials,US6802231042
943 | Auto Manufacturers,VinFast Auto Ltd.,VFS,Vietnam,Consumer Discretionary,SGXZ55111462
944 | Semiconductors,"MACOM Technology Solutions Holdings, Inc.",MTSI,United States,Technology,US55405Y1001
945 | Software - Application,"Vertex, Inc.",VERX,United States,Technology,US92538J1060
946 | Building Materials,"Summit Materials, Inc.",SUM,United States,Materials,US86614U1007
947 | Resorts & Casinos,"Wynn Resorts, Limited",WYNN,United States,Consumer Discretionary,US9831341071
948 | Gold,"Royal Gold, Inc.",RGLD,United States,Materials,US7802871084
949 | Metal Fabrication,"Mueller Industries, Inc.",MLI,United States,Industrials,US6247561029
950 | Building Products & Equipment,"AAON, Inc.",AAON,United States,Industrials,US0003602069
951 | Auto Manufacturers,NIO Inc.,NIO,China,Consumer Discretionary,US62914V1061
952 | Semiconductor Equipment & Materials,Onto Innovation Inc.,ONTO,United States,Technology,US6833441057
953 | Building Products & Equipment,"Fortune Brands Innovations, Inc.",FBIN,United States,Industrials,US34964C1062
954 | Industrial Distribution,"WESCO International, Inc.",WCC,United States,Industrials,US95082P1057
955 | Leisure,"Planet Fitness, Inc.",PLNT,United States,Consumer Discretionary,US72703H1014
956 | Oil & Gas Exploration & Production,Range Resources Corporation,RRC,United States,Energy,US75281A1097
957 | Information Technology Services,Globant S.A.,GLOB,Luxembourg,Technology,LU0974299876
958 | Banks - Regional,"Cullen/Frost Bankers, Inc.",CFR,United States,Financials,US2298991090
959 | Engineering & Construction,Stantec Inc.,STN,Canada,Industrials,CA85472N1096
960 | Agricultural Inputs,The Mosaic Company,MOS,United States,Materials,US61945C1036
961 | Asset Management,Hamilton Lane Incorporated,HLNE,United States,Financials,US4074971064
962 | Banks - Regional,"Commerce Bancshares, Inc.",CBSH,United States,Financials,US2005251036
963 | Information Technology Services,"Kyndryl Holdings, Inc.",KD,United States,Technology,US50155Q1004
964 | Oil & Gas Midstream,Hess Midstream LP,HESM,United States,Energy,US4281031058
965 | Telecom Services,"Frontier Communications Parent, Inc.",FYBR,United States,Communication Services,US35909D1090
966 | Publishing,The New York Times Company,NYT,United States,Communication Services,US6501111073
967 | Internet Content & Information,"Match Group, Inc.",MTCH,United States,Communication Services,US57667L1070
968 | Specialty Industrial Machinery,Generac Holdings Inc.,GNRC,United States,Industrials,US3687361044
969 | REIT - Mortgage,AGNC Investment Corp.,AGNC,United States,Real Estate,US00123Q1040
970 | Aluminum,Alcoa Corporation,AA,United States,Materials,US0138721065
971 | Packaged Foods,Ingredion Incorporated,INGR,United States,Consumer Staples,US4571871023
972 | Medical Devices,Glaukos Corporation,GKOS,United States,Healthcare,US3773221029
973 | Airlines,"Alaska Air Group, Inc.",ALK,United States,Industrials,US0116591092
974 | Information Technology Services,CACI International Inc,CACI,United States,Technology,US1271903049
975 | Banks - Regional,Wintrust Financial Corporation,WTFC,United States,Financials,US97650W1080
976 | Tools & Accessories,The Toro Company,TTC,United States,Industrials,US8910921084
977 | Oil & Gas Midstream,"Viper Energy, Inc.",VNOM,United States,Energy,US9279591062
978 | Aerospace & Defense,"StandardAero, Inc.",SARO,United States,Industrials,US85423L1035
979 | REIT - Office,Vornado Realty Trust,VNO,United States,Real Estate,US9290421091
980 | Building Materials,Eagle Materials Inc.,EXP,United States,Materials,US26969P1084
981 | Asset Management,Invesco Ltd.,IVZ,United States,Financials,BMG491BT1088
982 | Specialty Industrial Machinery,"Chart Industries, Inc.",GTLS,United States,Industrials,US16115Q3083
983 | Restaurants,Wingstop Inc.,WING,United States,Consumer Discretionary,US9741551033
984 | Oil & Gas Exploration & Production,APA Corporation,APA,United States,Energy,US03743Q1085
985 | Gold,Alamos Gold Inc.,AGI,Canada,Materials,CA0115321089
986 | Packaged Foods,"Lamb Weston Holdings, Inc.",LW,United States,Consumer Staples,US5132721045
987 | Banks - Regional,"Zions Bancorporation, National Association",ZION,United States,Financials,US9897011071
988 | Medical Devices,Bruker Corporation,BRKR,United States,Healthcare,US1167941087
989 | Information Technology Services,Parsons Corporation,PSN,United States,Technology,US70202L1026
990 | Specialty Industrial Machinery,"Donaldson Company, Inc.",DCI,United States,Industrials,US2576511099
991 | Airlines,LATAM Airlines Group S.A.,LTM,Chile,Industrials,US51817R2058
992 | Utilities - Regulated Electric,OGE Energy Corp.,OGE,United States,Utilities,US6708371033
993 | REIT - Industrial,"EastGroup Properties, Inc.",EGP,United States,Real Estate,US2772761019
994 | Building Materials,"CEMEX, S.A.B. de C.V.",CX,Mexico,Materials,US1512908898
995 | Capital Markets,Freedom Holding Corp.,FRHC,Kazakhstan,Financials,US3563901046
996 | Capital Markets,MarketAxess Holdings Inc.,MKTX,United States,Financials,US57060D1081
997 | Medical Instruments & Supplies,Teleflex Incorporated,TFX,United States,Healthcare,US8793691069
998 | Real Estate Services,FirstService Corporation,FSV,Canada,Real Estate,CA33767E2024
999 | Solar,"Enphase Energy, Inc.",ENPH,United States,Technology,US29355A1079
1000 | Computer Hardware,"IonQ, Inc.",IONQ,United States,Technology,US46222L1089
1001 | Information Technology Services,Genpact Limited,G,Bermuda,Technology,BMG3922B1072
1002 | Airports & Air Services,"Grupo Aeroportuario del Sureste, S. A. B. de C. V.",ASR,Mexico,Industrials,US40051E2028
1003 | Medical Care Facilities,Chemed Corporation,CHE,United States,Healthcare,US16359R1032
1004 | Diagnostics & Research,"Charles River Laboratories International, Inc.",CRL,United States,Healthcare,US1598641074
1005 | Packaging & Containers,Graphic Packaging Holding Company,GPK,United States,Consumer Discretionary,US3886891015
1006 | Banks - Regional,Comerica Incorporated,CMA,United States,Financials,US2003401070
1007 | Software - Infrastructure,UiPath Inc.,PATH,United States,Technology,US90364P1057
1008 | Auto Manufacturers,"Lucid Group, Inc.",LCID,United States,Consumer Discretionary,US5494981039
1009 | Specialty Retail,"Bath & Body Works, Inc.",BBWI,United States,Consumer Discretionary,US0708301041
1010 | Metal Fabrication,ATI Inc.,ATI,United States,Industrials,US01741R1023
1011 | Lodging,"Wyndham Hotels & Resorts, Inc.",WH,United States,Consumer Discretionary,US98311A1051
1012 | Banks - Regional,Woori Financial Group Inc.,WF,South Korea,Financials,US9810641087
1013 | Steel,United States Steel Corporation,X,United States,Materials,US9129091081
1014 | Telecom Services,"SK Telecom Co., Ltd.",SKM,South Korea,Communication Services,US78440P3064
1015 | Leisure,"Hasbro, Inc.",HAS,United States,Consumer Discretionary,US4180561072
1016 | Biotechnology,Roivant Sciences Ltd.,ROIV,United Kingdom,Healthcare,BMG762791017
1017 | Semiconductors,"Qorvo, Inc.",QRVO,United States,Technology,US74736K1016
1018 | Telecom Services,KT Corporation,KT,South Korea,Communication Services,US48268K1016
1019 | Information Technology Services,"ExlService Holdings, Inc.",EXLS,United States,Technology,US3020811044
1020 | Specialty Chemicals,Axalta Coating Systems Ltd.,AXTA,United States,Materials,BMG0750C1082
1021 | Building Products & Equipment,Louisiana-Pacific Corporation,LPX,United States,Industrials,US5463471053
1022 | Specialty Industrial Machinery,Flowserve Corporation,FLS,United States,Industrials,US34354P1057
1023 | Health Information Services,"Tempus AI, Inc",TEM,United States,Healthcare,US88023B1035
1024 | REIT - Retail,Brixmor Property Group Inc.,BRX,United States,Real Estate,US11120U1051
1025 | Medical Care Facilities,"The Ensign Group, Inc.",ENSG,United States,Healthcare,US29358P1012
1026 | Engineering & Construction,Fluor Corporation,FLR,United States,Industrials,US3434121022
1027 | Gold,Pan American Silver Corp.,PAAS,Canada,Materials,CA6979001089
1028 | Apparel Manufacturing,Gildan Activewear Inc.,GIL,Canada,Consumer Discretionary,CA3759161035
1029 | Packaging & Containers,"Berry Global Group, Inc.",BERY,United States,Consumer Discretionary,US08579W1036
1030 | Specialty Retail,RH,RH,United States,Consumer Discretionary,US74967X1037
1031 | Software - Infrastructure,Informatica Inc.,INFA,United States,Technology,US45674M1018
1032 | Chemicals,Celanese Corporation,CE,United States,Materials,US1508701034
1033 | "Furnishings, Fixtures & Appliances","Mohawk Industries, Inc.",MHK,United States,Consumer Discretionary,US6081901042
1034 | Entertainment,Paramount Global,PARAA,United States,Communication Services,US92556H1077
1035 | Education & Training Services,TAL Education Group,TAL,China,Consumer Staples,US8740801043
1036 | Software - Infrastructure,"SentinelOne, Inc.",S,United States,Technology,US81730H1095
1037 | Farm & Heavy Construction Machinery,AGCO Corporation,AGCO,United States,Industrials,US0010841023
1038 | Utilities - Diversified,The AES Corporation,AES,United States,Utilities,US00130H1059
1039 | Communication Equipment,EchoStar Corporation,SATS,United States,Technology,US2787681061
1040 | Banks - Regional,Synovus Financial Corp.,SNV,United States,Financials,US87161C5013
1041 | Education & Training Services,New Oriental Education & Technology Group Inc.,EDU,China,Consumer Staples,US6475812060
1042 | Farm Products,"Smithfield Foods, Inc.",SFD,,Consumer Staples,
1043 | Auto Parts,"Autoliv, Inc.",ALV,Sweden,Consumer Discretionary,US0528001094
1044 | Semiconductors,Lattice Semiconductor Corporation,LSCC,United States,Technology,US5184151042
1045 | Aerospace & Defense,CAE Inc.,CAE,Canada,Industrials,CA1247651088
1046 | Packaged Foods,"Freshpet, Inc.",FRPT,United States,Consumer Staples,US3580391056
1047 | Biotechnology,Ascendis Pharma A/S,ASND,Denmark,Healthcare,US04351P1012
1048 | Building Products & Equipment,"Trex Company, Inc.",TREX,United States,Industrials,US89531P1057
1049 | Asset Management,StepStone Group Inc.,STEP,United States,Financials,US85914M1071
1050 | Software - Application,Open Text Corporation,OTEX,Canada,Technology,CA6837151068
1051 | Specialty Business Services,"Dolby Laboratories, Inc.",DLB,United States,Industrials,US25659T1079
1052 | Aerospace & Defense,"Huntington Ingalls Industries, Inc.",HII,United States,Industrials,US4464131063
1053 | Oil & Gas Refining & Marketing,Sunoco LP,SUN,United States,Energy,US86765K1097
1054 | Banks - Regional,"Prosperity Bancshares, Inc.",PB,United States,Financials,US7436061052
1055 | Gambling,"Light & Wonder, Inc.",LNW,United States,Consumer Discretionary,US80874P1093
1056 | Oil & Gas Midstream,Antero Midstream Corporation,AM,United States,Energy,US03676B1026
1057 | Internet Retail,Vipshop Holdings Limited,VIPS,China,Consumer Discretionary,US92763W1036
1058 | Resorts & Casinos,"Caesars Entertainment, Inc.",CZR,United States,Consumer Discretionary,US12769G1004
1059 | Department Stores,"Dillard's, Inc.",DDS,United States,Consumer Discretionary,US2540671011
1060 | Insurance - Specialty,AXIS Capital Holdings Limited,AXS,Bermuda,Financials,BMG0692U1099
1061 | REIT - Retail,Agree Realty Corporation,ADC,United States,Real Estate,US0084921008
1062 | Biotechnology,"Revolution Medicines, Inc.",RVMD,United States,Healthcare,US76155X1000
1063 | REIT - Retail,"NNN REIT, Inc.",NNN,United States,Real Estate,US6374171063
1064 | Agricultural Inputs,ICL Group Ltd,ICL,Israel,Materials,IL0002810146
1065 | Banks - Regional,Old National Bancorp,ONB,United States,Financials,US6800331075
1066 | Oil & Gas Exploration & Production,Matador Resources Company,MTDR,United States,Energy,US5764852050
1067 | Electronic Components,Fabrinet,FN,Cayman Islands,Technology,KYG3323L1005
1068 | Entertainment,Sirius XM Holdings Inc.,SIRI,United States,Communication Services,US82968B1035
1069 | Biotechnology,Jazz Pharmaceuticals plc,JAZZ,Ireland,Healthcare,IE00B4Q5ZN47
1070 | Auto & Truck Dealerships,"AutoNation, Inc.",AN,United States,Consumer Discretionary,US05329W1027
1071 | Personal Services,"H&R Block, Inc.",HRB,United States,Consumer Discretionary,US0936711052
1072 | Aerospace & Defense,Embraer S.A.,ERJ,Brazil,Industrials,US29082A1079
1073 | Aerospace & Defense,Loar Holdings Inc.,LOAR,United States,Industrials,US53947R1059
1074 | Metal Fabrication,ESAB Corporation,ESAB,United States,Industrials,US29605J1060
1075 | Industrial Distribution,"Beacon Roofing Supply, Inc.",BECN,United States,Industrials,US0736851090
1076 | Entertainment,Paramount Global,PARA,United States,Communication Services,US92556H2067
1077 | Software - Application,CCC Intelligent Solutions Holdings Inc.,CCCS,United States,Technology,US12510Q1004
1078 | Software - Application,"SPS Commerce, Inc.",SPSC,United States,Technology,US78463M1071
1079 | Building Products & Equipment,The AZEK Company Inc.,AZEK,United States,Industrials,US05478C1053
1080 | Software - Infrastructure,"OneStream, Inc.",OS,United States,Technology,US68278B1070
1081 | "Furnishings, Fixtures & Appliances",Whirlpool Corporation,WHR,United States,Consumer Discretionary,US9633201069
1082 | Apparel Manufacturing,Levi Strauss & Co.,LEVI,United States,Consumer Discretionary,US52736R1023
1083 | REIT - Industrial,"First Industrial Realty Trust, Inc.",FR,United States,Real Estate,US32054K1034
1084 | Engineering & Construction,"KBR, Inc.",KBR,United States,Industrials,US48242W1062
1085 | Biotechnology,Blueprint Medicines Corporation,BPMC,United States,Healthcare,US09627Y1091
1086 | Real Estate Services,Colliers International Group Inc.,CIGI,Canada,Real Estate,CA1946931070
1087 | Scientific & Technical Instruments,"MKS Instruments, Inc.",MKSI,United States,Technology,US55306N1046
1088 | Software - Infrastructure,WEX Inc.,WEX,United States,Technology,US96208T1043
1089 | Electronic Gaming & Multimedia,Bilibili Inc.,BILI,China,Communication Services,US0900401060
1090 | Banks - Regional,"Popular, Inc.",BPOP,United States,Financials,PR7331747001
1091 | Software - Application,"Clearwater Analytics Holdings, Inc.",CWAN,United States,Technology,US1851231068
1092 | Specialty Retail,MINISO Group Holding Limited,MNSO,China,Consumer Discretionary,US66981J1025
1093 | Capital Markets,XP Inc.,XP,Cayman Islands,Financials,KYG982391099
1094 | Biotechnology,"Madrigal Pharmaceuticals, Inc.",MDGL,United States,Healthcare,US5588681057
1095 | Staffing & Employment Services,Robert Half Inc.,RHI,United States,Industrials,US7703231032
1096 | Oil & Gas Exploration & Production,Chord Energy Corporation,CHRD,United States,Energy,US6742152076
1097 | Biotechnology,"Halozyme Therapeutics, Inc.",HALO,United States,Healthcare,US40637H1095
1098 | Auto Parts,BorgWarner Inc.,BWA,United States,Consumer Discretionary,US0997241064
1099 | Personal Services,Bright Horizons Family Solutions Inc.,BFAM,United States,Consumer Discretionary,US1091941005
1100 | Lumber & Wood Production,"UFP Industries, Inc.",UFPI,United States,Materials,US90278Q1085
1101 | Internet Content & Information,Nebius Group N.V.,NBIS,Netherlands,Communication Services,NL0009805522
1102 | Banks - Regional,BOK Financial Corporation,BOKF,United States,Financials,US05561Q2012
1103 | Lumber & Wood Production,"Simpson Manufacturing Co., Inc.",SSD,United States,Materials,US8290731053
1104 | Specialty Industrial Machinery,"Watts Water Technologies, Inc.",WTS,United States,Industrials,US9427491025
1105 | Lumber & Wood Production,West Fraser Timber Co. Ltd.,WFG,Canada,Materials,CA9528451052
1106 | Agricultural Inputs,FMC Corporation,FMC,United States,Materials,US3024913036
1107 | Software - Infrastructure,"HashiCorp, Inc.",HCP,United States,Technology,US4181001037
1108 | Health Information Services,Waystar Holding Corp.,WAY,United States,Healthcare,US9467841055
1109 | Software - Application,"Commvault Systems, Inc.",CVLT,United States,Technology,US2041661024
1110 | Insurance - Life,Jackson Financial Inc.,JXN,United States,Financials,US46817M1071
1111 | Discount Stores,"Ollie's Bargain Outlet Holdings, Inc.",OLLI,United States,Consumer Staples,US6811161099
1112 | Consulting Services,"FTI Consulting, Inc.",FCN,United States,Industrials,US3029411093
1113 | Credit Services,"OneMain Holdings, Inc.",OMF,United States,Financials,US68268W1036
1114 | Lodging,"Choice Hotels International, Inc.",CHH,United States,Consumer Discretionary,US1699051066
1115 | Oil & Gas Midstream,"EnLink Midstream, LLC",ENLC,United States,Energy,US29336T1007
1116 | Financial Conglomerates,"Voya Financial, Inc.",VOYA,United States,Financials,US9290891004
1117 | Electronic Components,Universal Display Corporation,OLED,United States,Technology,US91347P1057
1118 | Household & Personal Products,"Hims & Hers Health, Inc.",HIMS,United States,Consumer Staples,US4330001060
1119 | Asset Management,Janus Henderson Group plc,JHG,United Kingdom,Financials,JE00BYPZJM29
1120 | Residential Construction,Taylor Morrison Home Corporation,TMHC,United States,Consumer Discretionary,US87724P1066
1121 | Banks - Regional,Banco Macro S.A.,BMA,Argentina,Financials,US05961W1053
1122 | Restaurants,"Brinker International, Inc.",EAT,United States,Consumer Discretionary,US1096411004
1123 | Biotechnology,"BridgeBio Pharma, Inc.",BBIO,United States,Healthcare,US10806X1028
1124 | Oil & Gas Refining & Marketing,HF Sinclair Corporation,DINO,United States,Energy,US4039491000
1125 | Rental & Leasing Services,WillScot Holdings Corporation,WSC,United States,Industrials,US9713781048
1126 | Resorts & Casinos,Boyd Gaming Corporation,BYD,United States,Consumer Discretionary,US1033041013
1127 | Capital Markets,PJT Partners Inc.,PJT,United States,Financials,US69343T1079
1128 | Scientific & Technical Instruments,Cognex Corporation,CGNX,United States,Technology,US1924221039
1129 | Rental & Leasing Services,"Ryder System, Inc.",R,United States,Industrials,US7835491082
1130 | Security & Protection Services,ADT Inc.,ADT,United States,Industrials,US00090Q1031
1131 | Mortgage Finance,Mr. Cooper Group Inc.,COOP,United States,Financials,US62482R1077
1132 | Building Products & Equipment,"SPX Technologies, Inc.",SPXC,United States,Industrials,US78473E1038
1133 | Waste Management,"Casella Waste Systems, Inc.",CWST,United States,Industrials,US1474481041
1134 | Insurance - Property & Casualty,RLI Corp.,RLI,United States,Financials,US7496071074
1135 | Pollution & Treatment Controls,Zurn Elkay Water Solutions Corporation,ZWS,United States,Industrials,US98983L1089
1136 | Entertainment,Liberty Live Group,LLYVK,United States,Communication Services,US5312297220
1137 | Semiconductor Equipment & Materials,Nova Ltd.,NVMI,Israel,Technology,IL0010845571
1138 | Telecom Services,Turkcell Iletisim Hizmetleri A.S.,TKC,Turkey,Communication Services,US9001112047
1139 | Entertainment,Liberty Live Group,LLYVA,United States,Communication Services,US5312297485
1140 | Gold,Harmony Gold Mining Company Limited,HMY,South Africa,Materials,US4132163001
1141 | Biotechnology,Legend Biotech Corporation,LEGN,United States,Healthcare,US52490G1022
1142 | REIT - Industrial,Terreno Realty Corporation,TRNO,United States,Real Estate,US88146M1018
1143 | Specialty Industrial Machinery,JBT Marel Corporation,JBTM,United States,Industrials,
1144 | Internet Content & Information,Kanzhun Limited,BZ,China,Communication Services,US48553T1060
1145 | Conglomerates,"Valmont Industries, Inc.",VMI,United States,Industrials,US9202531011
1146 | Industrial Distribution,"SiteOne Landscape Supply, Inc.",SITE,United States,Industrials,US82982L1035
1147 | Utilities - Regulated Gas,UGI Corporation,UGI,United States,Utilities,US9026811052
1148 | Building Products & Equipment,"Armstrong World Industries, Inc.",AWI,United States,Industrials,US04247X1028
1149 | Internet Content & Information,Trump Media & Technology Group Corp.,DJT,United States,Communication Services,US25400Q1058
1150 | REIT - Mortgage,"Starwood Property Trust, Inc.",STWD,United States,Real Estate,US85571B1052
1151 | Insurance - Specialty,First American Financial Corporation,FAF,United States,Financials,US31847R1023
1152 | Insurance - Specialty,MGIC Investment Corporation,MTG,United States,Financials,US5528481030
1153 | Credit Services,"Qifu Technology, Inc.",QFIN,China,Financials,US88557W1018
1154 | Banks - Regional,Cadence Bank,CADE,United States,Financials,US12740C1036
1155 | Security & Protection Services,MSA Safety Incorporated,MSA,United States,Industrials,US5534981064
1156 | Asset Management,FS KKR Capital Corp.,FSK,United States,Financials,US3026352068
1157 | Semiconductors,Rambus Inc.,RMBS,United States,Technology,US7509171069
1158 | Airports & Air Services,"Joby Aviation, Inc.",JOBY,United States,Industrials,KYG651631007
1159 | Household & Personal Products,Coty Inc.,COTY,United States,Consumer Staples,US2220702037
1160 | Telecom Services,TIM S.A.,TIMB,Brazil,Communication Services,US88706T1088
1161 | Credit Services,Credit Acceptance Corporation,CACC,United States,Financials,US2253101016
1162 | Resorts & Casinos,"Vail Resorts, Inc.",MTN,United States,Consumer Discretionary,US91879Q1094
1163 | Biotechnology,Corcept Therapeutics Incorporated,CORT,United States,Healthcare,US2183521028
1164 | Medical Instruments & Supplies,"Merit Medical Systems, Inc.",MMSI,United States,Healthcare,US5898891040
1165 | REIT - Hotel & Motel,"Ryman Hospitality Properties, Inc.",RHP,United States,Real Estate,US78377T1079
1166 | Auto Parts,Gentex Corporation,GNTX,United States,Consumer Discretionary,US3719011096
1167 | Drug Manufacturers - Specialty & Generic,"Lantheus Holdings, Inc.",LNTH,United States,Healthcare,US5165441032
1168 | Software - Application,Sportradar Group AG,SRAD,Switzerland,Technology,CH1134239669
1169 | REIT - Industrial,"STAG Industrial, Inc.",STAG,United States,Real Estate,US85254J1025
1170 | REIT - Industrial,"Americold Realty Trust, Inc.",COLD,United States,Real Estate,US03064D1081
1171 | Leisure,"Mattel, Inc.",MAT,United States,Consumer Discretionary,US5770811025
1172 | Internet Retail,"Etsy, Inc.",ETSY,United States,Consumer Discretionary,US29786A1060
1173 | Insurance - Specialty,Essent Group Ltd.,ESNT,Bermuda,Financials,BMG3198U1027
1174 | Packaged Foods,"Post Holdings, Inc.",POST,United States,Consumer Staples,US7374461041
1175 | Farm & Heavy Construction Machinery,Oshkosh Corporation,OSK,United States,Industrials,US6882392011
1176 | Integrated Freight & Logistics,"Landstar System, Inc.",LSTR,United States,Industrials,US5150981018
1177 | Capital Markets,"MARA Holdings, Inc.",MARA,United States,Financials,US5657881067
1178 | Auto Manufacturers,ZEEKR Intelligent Technology Holding Limited,ZK,China,Consumer Discretionary,US98923K1034
1179 | Oil & Gas Integrated,National Fuel Gas Company,NFG,United States,Energy,US6361801011
1180 | Electronics & Computer Distribution,"Arrow Electronics, Inc.",ARW,United States,Technology,US0427351004
1181 | Internet Retail,Wayfair Inc.,W,United States,Consumer Discretionary,US94419L1017
1182 | Specialty Chemicals,Element Solutions Inc,ESI,United States,Materials,US28618M1062
1183 | Specialty Chemicals,Arcadium Lithium plc,ALTM,Ireland,Materials,JE00BM9HZ112
1184 | Packaged Foods,BRF S.A.,BRFS,Brazil,Consumer Staples,US10552T1079
1185 | Medical Instruments & Supplies,Bausch + Lomb Corporation,BLCO,Canada,Healthcare,CA0717051076
1186 | Leisure,"Life Time Group Holdings, Inc.",LTH,United States,Consumer Discretionary,US53190C1027
1187 | Scientific & Technical Instruments,"Badger Meter, Inc.",BMI,United States,Technology,US0565251081
1188 | Marine Shipping,Kirby Corporation,KEX,United States,Industrials,US4972661064
1189 | REIT - Healthcare Facilities,Healthcare Realty Trust Incorporated,HR,United States,Real Estate,US42226K1051
1190 | Apparel Retail,Abercrombie & Fitch Co.,ANF,United States,Consumer Discretionary,US0028962076
1191 | Credit Services,"Upstart Holdings, Inc.",UPST,United States,Financials,US91680M1071
1192 | Biotechnology,"Nuvalent, Inc.",NUVL,United States,Healthcare,US6707031075
1193 | Banks - Regional,"Home Bancshares, Inc. (Conway, AR)",HOMB,United States,Financials,US4368932004
1194 | Telecom Services,Telecom Argentina S.A.,TEO,Argentina,Communication Services,US8792732096
1195 | Footwear & Accessories,"Crocs, Inc.",CROX,United States,Consumer Discretionary,US2270461096
1196 | Capital Markets,"Virtu Financial, Inc.",VIRT,United States,Financials,US9282541013
1197 | Drug Manufacturers - Specialty & Generic,Elanco Animal Health Incorporated,ELAN,United States,Healthcare,US28414H1032
1198 | Credit Services,SLM Corporation,SLM,United States,Financials,US78442P1066
1199 | Specialty Industrial Machinery,"CSW Industrials, Inc.",CSWI,United States,Industrials,US1264021064
1200 | Pollution & Treatment Controls,Federal Signal Corporation,FSS,United States,Industrials,US3138551086
1201 | Biotechnology,Telix Pharmaceuticals Limited,TLX,Australia,Healthcare,
1202 | Software - Application,Freshworks Inc.,FRSH,United States,Technology,US3580541049
1203 | Household & Personal Products,"e.l.f. Beauty, Inc.",ELF,United States,Consumer Staples,US26856L1035
1204 | Auto & Truck Dealerships,"Group 1 Automotive, Inc.",GPI,United States,Consumer Discretionary,US3989051095
1205 | Diagnostics & Research,"Guardant Health, Inc.",GH,United States,Healthcare,US40131M1099
1206 | Capital Markets,Moelis & Company,MC,United States,Financials,US60786M1053
1207 | Utilities - Diversified,Companhia Energética de Minas Gerais - CEMIG,CIG,Brazil,Utilities,US2044096012
1208 | Utilities - Diversified,Companhia Energética de Minas Gerais - CEMIG,CIG.C,,Utilities,US2044098828
1209 | Insurance Brokers,CorVel Corporation,CRVL,United States,Financials,US2210061097
1210 | Steel,Gerdau S.A.,GGB,Brazil,Materials,US3737371050
1211 | Semiconductor Equipment & Materials,"Amkor Technology, Inc.",AMKR,United States,Technology,US0316521006
1212 | Banks - Regional,UMB Financial Corporation,UMBF,United States,Financials,US9027881088
1213 | REIT - Mortgage,Rithm Capital Corp.,RITM,United States,Real Estate,US64828T2015
1214 | Rental & Leasing Services,GATX Corporation,GATX,United States,Industrials,US3614481030
1215 | Software - Application,"Q2 Holdings, Inc.",QTWO,United States,Technology,US74736L1098
1216 | Asset Management,Blue Owl Capital Corporation,OBDC,United States,Financials,US69121K1043
1217 | Banks - Regional,"Columbia Banking System, Inc.",COLB,United States,Financials,US1972361026
1218 | Residential Construction,Meritage Homes Corporation,MTH,United States,Consumer Discretionary,US59001A1025
1219 | Beverages - Non-Alcoholic,"Celsius Holdings, Inc.",CELH,United States,Consumer Staples,US15118V2079
1220 | Communication Equipment,"AST SpaceMobile, Inc.",ASTS,United States,Technology,US00217D1000
1221 | Insurance - Life,Lincoln National Corporation,LNC,United States,Financials,US5341871094
1222 | Software - Application,"Lyft, Inc.",LYFT,United States,Technology,US55087P1049
1223 | Building Materials,Knife River Corporation,KNF,United States,Materials,US4988941047
1224 | Software - Application,Workiva Inc.,WK,United States,Technology,US98139A1051
1225 | Utilities - Regulated Electric,"IDACORP, Inc.",IDA,United States,Utilities,US4511071064
1226 | Insurance - Property & Casualty,"Selective Insurance Group, Inc.",SIGI,United States,Financials,US8163001071
1227 | Medical Devices,"Inspire Medical Systems, Inc.",INSP,United States,Healthcare,US4577301090
1228 | Packaging & Containers,Reynolds Consumer Products Inc.,REYN,United States,Consumer Discretionary,US76171L1061
1229 | Banks - Regional,Bank OZK,OZK,United States,Financials,US06417N1037
1230 | Solar,Nextracker Inc.,NXT,United States,Technology,US65290E1010
1231 | Biotechnology,"Cytokinetics, Incorporated",CYTK,United States,Healthcare,US23282W6057
1232 | Asset Management,"Affiliated Managers Group, Inc.",AMG,United States,Financials,US0082521081
1233 | Aerospace & Defense,Moog Inc.,MOG.A,United States,Industrials,US6153942023
1234 | Mortgage Finance,"PennyMac Financial Services, Inc.",PFSI,United States,Financials,US70932M1071
1235 | Steel,Commercial Metals Company,CMC,United States,Materials,US2017231034
1236 | Steel,Ternium S.A.,TX,Luxembourg,Materials,US8808901081
1237 | Aerospace & Defense,Moog Inc.,MOG.B,United States,Industrials,US6153943013
1238 | Scientific & Technical Instruments,Vontier Corporation,VNT,United States,Technology,US9288811014
1239 | Medical Instruments & Supplies,Stevanato Group S.p.A.,STVN,Italy,Healthcare,IT0005452658
1240 | Banks - Regional,Valley National Bancorp,VLY,United States,Financials,US9197941076
1241 | Packaging & Containers,Silgan Holdings Inc.,SLGN,United States,Consumer Discretionary,US8270481091
1242 | Software - Infrastructure,"ACI Worldwide, Inc.",ACIW,United States,Technology,US0044981019
1243 | Banks - Regional,"Glacier Bancorp, Inc.",GBCI,United States,Financials,US37637Q1058
1244 | Rental & Leasing Services,Herc Holdings Inc.,HRI,United States,Industrials,US42704L1044
1245 | Insurance - Property & Casualty,"The Hanover Insurance Group, Inc.",THG,United States,Financials,US4108671052
1246 | Insurance - Life,"F&G Annuities & Life, Inc.",FG,United States,Financials,US30190A1043
1247 | Banks - Regional,F.N.B. Corporation,FNB,United States,Financials,US3025201019
1248 | REIT - Diversified,"Essential Properties Realty Trust, Inc.",EPRT,United States,Real Estate,US29670E1073
1249 | Software - Application,"Intapp, Inc.",INTA,United States,Technology,US45827U1097
1250 | Packaged Foods,Darling Ingredients Inc.,DAR,United States,Consumer Staples,US2372661015
1251 | Oil & Gas Equipment & Services,NOV Inc.,NOV,United States,Energy,US62955J1034
1252 | Oil & Gas Equipment & Services,ChampionX Corporation,CHX,United States,Energy,US15872M1045
1253 | Drug Manufacturers - General,"Grifols, S.A.",GRFS,Spain,Healthcare,US3984384087
1254 | Oil & Gas Exploration & Production,"Comstock Resources, Inc.",CRK,United States,Energy,US2057683029
1255 | Electronic Components,"Littelfuse, Inc.",LFUS,United States,Technology,US5370081045
1256 | Residential Construction,"Installed Building Products, Inc.",IBP,United States,Consumer Discretionary,US45780R1014
1257 | Software - Application,"QXO, Inc.",QXO,United States,Technology,US82846H4056
1258 | Integrated Freight & Logistics,"GXO Logistics, Inc.",GXO,United States,Industrials,US36262G1013
1259 | Telecom Services,United States Cellular Corporation,USM,United States,Communication Services,US9116841084
1260 | Farm Products,"Cal-Maine Foods, Inc.",CALM,United States,Consumer Staples,US1280302027
1261 | Electronics & Computer Distribution,"Insight Enterprises, Inc.",NSIT,United States,Technology,US45765U1034
1262 | Banks - Regional,"First Financial Bankshares, Inc.",FFIN,United States,Financials,US32020R1095
1263 | Aerospace & Defense,Hexcel Corporation,HXL,United States,Industrials,US4282911084
1264 | Asset Management,Main Street Capital Corporation,MAIN,United States,Financials,US56035L1044
1265 | Recreational Vehicles,"THOR Industries, Inc.",THO,United States,Consumer Discretionary,US8851601018
1266 | Software - Infrastructure,"Qualys, Inc.",QLYS,United States,Technology,US74758T3032
1267 | Biotechnology,"Ionis Pharmaceuticals, Inc.",IONS,United States,Healthcare,US4622221004
1268 | Information Technology Services,Ingram Micro Holding Corporation,INGM,United States,Technology,US4571521065
1269 | Tools & Accessories,The Timken Company,TKR,United States,Industrials,US8873891043
1270 | Semiconductors,"Cirrus Logic, Inc.",CRUS,United States,Technology,US1727551004
1271 | Auto & Truck Dealerships,"Asbury Automotive Group, Inc.",ABG,United States,Consumer Discretionary,US0434361046
1272 | Specialty Industrial Machinery,NuScale Power Corporation,SMR,United States,Industrials,US67079K1007
1273 | Software - Infrastructure,"Tenable Holdings, Inc.",TENB,United States,Technology,US88025T1025
1274 | Communication Equipment,Lumentum Holdings Inc.,LITE,United States,Technology,US55024U1097
1275 | Scientific & Technical Instruments,Novanta Inc.,NOVT,United States,Technology,CA67000B1040
1276 | REIT - Retail,Kite Realty Group Trust,KRG,United States,Real Estate,US49803T3005
1277 | Apparel Retail,"Boot Barn Holdings, Inc.",BOOT,United States,Consumer Discretionary,US0994061002
1278 | Utilities - Regulated Gas,"Southwest Gas Holdings, Inc.",SWX,United States,Utilities,US8448951025
1279 | Software - Infrastructure,Cellebrite DI Ltd.,CLBT,Israel,Technology,IL0011794802
1280 | Specialty Retail,"Five Below, Inc.",FIVE,United States,Consumer Discretionary,US33829M1018
1281 | Entertainment,Madison Square Garden Sports Corp.,MSGS,United States,Communication Services,US55825T1034
1282 | Semiconductors,Semtech Corporation,SMTC,United States,Technology,US8168501018
1283 | Software - Application,"SoundHound AI, Inc.",SOUN,United States,Technology,US8361001071
1284 | REIT - Retail,The Macerich Company,MAC,United States,Real Estate,US5543821012
1285 | Financial Data & Stock Exchanges,"Dun & Bradstreet Holdings, Inc.",DNB,United States,Financials,US26484T1060
1286 | Medical Care Facilities,"Option Care Health, Inc.",OPCH,United States,Healthcare,US68404L2016
1287 | Engineering & Construction,"Dycom Industries, Inc.",DY,United States,Industrials,US2674751019
1288 | Trucking,"Schneider National, Inc.",SNDR,United States,Industrials,US80689H1023
1289 | Specialty Chemicals,Balchem Corporation,BCPC,United States,Materials,US0576652004
1290 | Insurance - Specialty,"Enact Holdings, Inc.",ACT,United States,Financials,US29249E1091
1291 | Auto Parts,Lear Corporation,LEA,United States,Consumer Discretionary,US5218652049
1292 | Banks - Regional,"United Bankshares, Inc.",UBSI,United States,Financials,US9099071071
1293 | Residential Construction,"Champion Homes, Inc.",SKY,United States,Consumer Discretionary,US8308301055
1294 | Information Technology Services,Science Applications International Corporation,SAIC,United States,Technology,US8086251076
1295 | Education & Training Services,"Stride, Inc.",LRN,United States,Consumer Staples,US86333M1080
1296 | Packaging & Containers,Sealed Air Corporation,SEE,United States,Consumer Discretionary,US81211K1007
1297 | ,Noble Corporation plc,NE.WSA,,,
1298 | Oil & Gas Drilling,Noble Corporation plc,NE,United States,Energy,GB00BMXNWH07
1299 | Specialty Industrial Machinery,Gates Industrial Corporation plc,GTES,United States,Industrials,GB00BD9G2S12
1300 | Telecom Services,"Lumen Technologies, Inc.",LUMN,United States,Communication Services,US5502411037
1301 | Semiconductors,Tower Semiconductor Ltd.,TSEM,Israel,Technology,IL0010823792
1302 | Software - Infrastructure,"Varonis Systems, Inc.",VRNS,United States,Technology,US9222801022
1303 | Apparel Manufacturing,"Kontoor Brands, Inc.",KTB,United States,Consumer Discretionary,US50050N1037
1304 | Banks - Regional,Hancock Whitney Corporation,HWC,United States,Financials,US4101201097
1305 | Apparel Manufacturing,Columbia Sportswear Company,COLM,United States,Consumer Discretionary,US1985161066
1306 | Apparel Retail,"Urban Outfitters, Inc.",URBN,United States,Consumer Discretionary,US9170471026
1307 | Apparel Manufacturing,PVH Corp.,PVH,United States,Consumer Discretionary,US6936561009
1308 | Insurance - Specialty,Radian Group Inc.,RDN,United States,Financials,US7502361014
1309 | Rental & Leasing Services,Air Lease Corporation,AL,United States,Industrials,US00912X3026
1310 | REIT - Healthcare Facilities,"CareTrust REIT, Inc.",CTRE,United States,Real Estate,US14174T1079
1311 | Resorts & Casinos,"Red Rock Resorts, Inc.",RRR,United States,Consumer Discretionary,US75700L1089
1312 | REIT - Office,Cousins Properties Incorporated,CUZ,United States,Real Estate,US2227955026
1313 | Oil & Gas Midstream,"Plains GP Holdings, L.P.",PAGP,United States,Energy,US72651A2078
1314 | Aerospace & Defense,"Kratos Defense & Security Solutions, Inc.",KTOS,United States,Industrials,US50077B2079
1315 | Drug Manufacturers - Specialty & Generic,Alkermes plc,ALKS,Ireland,Healthcare,IE00B56GVS15
1316 | Restaurants,Shake Shack Inc.,SHAK,United States,Consumer Discretionary,US8190471016
1317 | REIT - Retail,"Phillips Edison & Company, Inc.",PECO,United States,Real Estate,US71844V2016
1318 | Software - Application,"Asana, Inc.",ASAN,United States,Technology,US04342Y1047
1319 | Banks - Regional,"ServisFirst Bancshares, Inc.",SFBS,United States,Financials,US81768T1088
1320 | Steel,Cleveland-Cliffs Inc.,CLF,United States,Materials,US1858991011
1321 | Oil & Gas Equipment & Services,"Archrock, Inc.",AROC,United States,Energy,US03957W1062
1322 | Auto Parts,Modine Manufacturing Company,MOD,United States,Consumer Discretionary,US6078281002
1323 | Credit Services,"FirstCash Holdings, Inc.",FCFS,United States,Financials,US33768G1076
1324 | Biotechnology,"Axsome Therapeutics, Inc.",AXSM,United States,Healthcare,US05464T1043
1325 | Oil & Gas Refining & Marketing,Icahn Enterprises L.P.,IEP,United States,Energy,US4511001012
1326 | Oil & Gas Exploration & Production,"Vista Energy, S.A.B. de C.V.",VIST,Mexico,Energy,US92837L1098
1327 | Capital Markets,Piper Sandler Companies,PIPR,United States,Financials,US7240781002
1328 | Oil & Gas Exploration & Production,"Civitas Resources, Inc.",CIVI,United States,Energy,US17888H1032
1329 | ,South Bow Corporation,SOBO,Canada (Federal Level),,CA83671M1059
1330 | Oil & Gas Equipment & Services,"Cactus, Inc.",WHD,United States,Energy,US1272031071
1331 | Residential Construction,KB Home,KBH,United States,Consumer Discretionary,US48666K1097
1332 | Utilities - Independent Power Producers,Pampa Energía S.A.,PAM,Argentina,Utilities,US6976602077
1333 | Education & Training Services,"Grand Canyon Education, Inc.",LOPE,United States,Consumer Staples,US38526M1062
1334 | Building Materials,Boise Cascade Company,BCC,United States,Materials,US09739D1000
1335 | Aerospace & Defense,"AeroVironment, Inc.",AVAV,United States,Industrials,US0080731088
1336 | Utilities - Renewable,"Clearway Energy, Inc.",CWEN.A,United States,Utilities,US18539C2044
1337 | Oil & Gas Exploration & Production,Magnolia Oil & Gas Corporation,MGY,United States,Energy,US5596631094
1338 | Software - Application,"Braze, Inc.",BRZE,United States,Technology,US10576N1028
1339 | Diagnostics & Research,"RadNet, Inc.",RDNT,United States,Healthcare,US7504911022
1340 | Broadcasting,"Nexstar Media Group, Inc.",NXST,United States,Communication Services,US65336K1034
1341 | Insurance Brokers,"The Baldwin Insurance Group, Inc.",BWIN,United States,Financials,US05589G1022
1342 | Insurance - Property & Casualty,"White Mountains Insurance Group, Ltd.",WTM,Bermuda,Financials,BMG9618E1075
1343 | Utilities - Regulated Gas,Brookfield Infrastructure Corporation,BIPC,United States,Utilities,CA11275Q1072
1344 | REIT - Office,SL Green Realty Corp.,SLG,United States,Real Estate,US78440X8873
1345 | Capital Markets,"Lazard, Inc.",LAZ,United States,Financials,US52110M1099
1346 | Telecom Services,PLDT Inc.,PHI,Philippines,Communication Services,US69344D4088
1347 | Medical Devices,Integer Holdings Corporation,ITGR,United States,Healthcare,US45826H1095
1348 | REIT - Industrial,National Storage Affiliates Trust,NSA,United States,Real Estate,US6378701063
1349 | Specialty Business Services,"Amentum Holdings, Inc.",AMTM,United States,Industrials,US0239391016
1350 | Software - Infrastructure,"Box, Inc.",BOX,United States,Technology,US10316T1043
1351 | Specialty Chemicals,NewMarket Corporation,NEU,United States,Materials,US6515871076
1352 | Oil & Gas Equipment & Services,Weatherford International plc,WFRD,United States,Energy,IE00BLNN3691
1353 | Insurance - Specialty,Assured Guaranty Ltd.,AGO,Bermuda,Financials,BMG0585R1060
1354 | Biotechnology,"TG Therapeutics, Inc.",TGTX,United States,Healthcare,US88322Q1085
1355 | Insurance - Diversified,Enstar Group Limited,ESGR,Bermuda,Financials,BMG3075P1014
1356 | Engineering & Construction,"Arcosa, Inc.",ACA,United States,Industrials,US0396531008
1357 | Auto & Truck Dealerships,Valvoline Inc.,VVV,United States,Consumer Discretionary,US92047W1018
1358 | Conglomerates,Brookfield Business Partners L.P.,BBU,Bermuda,Industrials,BMG162341090
1359 | Specialty Chemicals,Cabot Corporation,CBT,United States,Materials,US1270551013
1360 | Scientific & Technical Instruments,"Itron, Inc.",ITRI,United States,Technology,US4657411066
1361 | Banks - Regional,Banco BBVA Argentina S.A.,BBAR,Argentina,Financials,US0589341009
1362 | Packaging & Containers,Sonoco Products Company,SON,United States,Consumer Discretionary,US8354951027
1363 | Utilities - Regulated Gas,New Jersey Resources Corporation,NJR,United States,Utilities,US6460251068
1364 | Auto & Truck Dealerships,"Rush Enterprises, Inc.",RUSHA,United States,Consumer Discretionary,US7818462092
1365 | Engineering & Construction,"Exponent, Inc.",EXPO,United States,Industrials,US30214U1025
1366 | Staffing & Employment Services,"TriNet Group, Inc.",TNET,United States,Industrials,US8962881079
1367 | Electronic Components,Pony AI Inc.,PONY,China,Technology,US7329081084
1368 | Packaged Foods,Lancaster Colony Corporation,LANC,United States,Consumer Staples,US5138471033
1369 | REIT - Office,Kilroy Realty Corporation,KRC,United States,Real Estate,US49427F1084
1370 | Oil & Gas Equipment & Services,LandBridge Company LLC,LB,United States,Energy,US5149521008
1371 | Auto & Truck Dealerships,"Rush Enterprises, Inc.",RUSHB,United States,Consumer Discretionary,US7818463082
1372 | Medical Devices,"Inari Medical, Inc.",NARI,United States,Healthcare,US45332Y1091
1373 | Communication Equipment,Belden Inc.,BDC,United States,Technology,US0774541066
1374 | Telecom Services,Millicom International Cellular S.A.,TIGO,Luxembourg,Communication Services,LU0038705702
1375 | Oil & Gas Exploration & Production,California Resources Corporation,CRC,United States,Energy,US13057Q3056
1376 | Electrical Equipment & Parts,Bloom Energy Corporation,BE,United States,Industrials,US0937121079
1377 | Other,Sunrise Communications AG,SNRE,Switzerland,,US8679751045
1378 | Software - Infrastructure,"Remitly Global, Inc.",RELY,United States,Technology,US75960P1049
1379 | Personal Services,"Frontdoor, Inc.",FTDR,United States,Consumer Discretionary,US35905A1097
1380 | Aerospace & Defense,Archer Aviation Inc.,ACHR,United States,Industrials,US03945R1023
1381 | Utilities - Diversified,Companhia Paranaense de Energia - COPEL,ELP,Brazil,Utilities,US20441B6056
1382 | Utilities - Diversified,Companhia Paranaense de Energia - COPEL,ELPC,Brazil,Utilities,US20441B7047
1383 | Airlines,"SkyWest, Inc.",SKYW,United States,Industrials,US8308791024
1384 | REIT - Healthcare Facilities,"American Healthcare REIT, Inc.",AHR,United States,Real Estate,US3981823038
1385 | Industrial Distribution,"MSC Industrial Direct Co., Inc.",MSM,United States,Industrials,US5535301064
1386 | Semiconductors,SiTime Corporation,SITM,United States,Technology,US82982T1060
1387 | Software - Application,"InterDigital, Inc.",IDCC,United States,Technology,US45867G1013
1388 | Biotechnology,"Krystal Biotech, Inc.",KRYS,United States,Healthcare,US5011471027
1389 | Marine Shipping,"Matson, Inc.",MATX,United States,Industrials,US57686G1058
1390 | Asset Management,AllianceBernstein Holding L.P.,AB,United States,Financials,US01881G1067
1391 | Oil & Gas Integrated,Transportadora de Gas del Sur S.A.,TGS,Argentina,Energy,US8938702045
1392 | Electronics & Computer Distribution,"Avnet, Inc.",AVT,United States,Technology,US0538071038
1393 | Asset Management,"Cohen & Steers, Inc.",CNS,United States,Financials,US19247A1007
1394 | Leisure,Six Flags Entertainment Corporation,FUN,United States,Consumer Discretionary,US1501851067
1395 | Oil & Gas Exploration & Production,SM Energy Company,SM,United States,Energy,US78454L1008
1396 | Specialty Industrial Machinery,Kadant Inc.,KAI,United States,Industrials,US48282T1043
1397 | Specialty Industrial Machinery,"Franklin Electric Co., Inc.",FELE,United States,Industrials,US3535141028
1398 | Household & Personal Products,"Interparfums, Inc.",IPAR,United States,Consumer Staples,US4583341098
1399 | Recreational Vehicles,Brunswick Corporation,BC,United States,Consumer Discretionary,US1170431092
1400 | Capital Markets,"BGC Group, Inc.",BGC,United States,Financials,US0889291045
1401 | Banks - Regional,Ameris Bancorp,ABCB,United States,Financials,US03076K1088
1402 | Engineering & Construction,"Construction Partners, Inc.",ROAD,United States,Industrials,US21044C1071
1403 | Infrastructure Operations,Verra Mobility Corporation,VRRM,United States,Industrials,US92511U1025
1404 | Electronic Components,Sanmina Corporation,SANM,United States,Technology,US8010561020
1405 | Utilities - Regulated Electric,Portland General Electric Company,POR,United States,Utilities,US7365088472
1406 | REIT - Residential,"Independence Realty Trust, Inc.",IRT,United States,Real Estate,US45378A1060
1407 | Specialty Business Services,"Maximus, Inc.",MMS,United States,Industrials,US5779331041
1408 | Biotechnology,Verona Pharma plc,VRNA,United Kingdom,Healthcare,US9250501064
1409 | Agricultural Inputs,The Scotts Miracle-Gro Company,SMG,United States,Materials,US8101861065
1410 | Department Stores,"Macy's, Inc.",M,United States,Consumer Discretionary,US55616P1049
1411 | Household & Personal Products,Newell Brands Inc.,NWL,United States,Consumer Staples,US6512291062
1412 | Semiconductors,Silicon Laboratories Inc.,SLAB,United States,Technology,US8269191024
1413 | Software - Infrastructure,"Euronet Worldwide, Inc.",EEFT,United States,Technology,US2987361092
1414 | Electrical Equipment & Parts,"Advanced Energy Industries, Inc.",AEIS,United States,Industrials,US0079731008
1415 | Telecom Services,Liberty Global Ltd.,LBTYB,Bermuda,Communication Services,BMG611881191
1416 | Telecom Services,Liberty Global Ltd.,LBTYK,Bermuda,Communication Services,BMG611881274
1417 | Asset Management,"Victory Capital Holdings, Inc.",VCTR,United States,Financials,US92645B1035
1418 | Engineering & Construction,"Sterling Infrastructure, Inc.",STRL,United States,Industrials,US8592411016
1419 | Software - Infrastructure,Zeta Global Holdings Corp.,ZETA,United States,Technology,US98956A1051
1420 | Specialty Business Services,"CBIZ, Inc.",CBZ,United States,Industrials,US1248051021
1421 | Information Technology Services,GDS Holdings Limited,GDS,China,Technology,US36165L1089
1422 | Insurance - Property & Casualty,Kemper Corporation,KMPR,United States,Financials,US4884011002
1423 | Utilities - Regulated Electric,"TXNM Energy, Inc.",TXNM,United States,Utilities,US69349H1077
1424 | Engineering & Construction,"IES Holdings, Inc.",IESC,United States,Industrials,US44951W1062
1425 | Software - Application,"C3.ai, Inc.",AI,United States,Technology,US12468P1049
1426 | Oil & Gas Exploration & Production,Murphy Oil Corporation,MUR,United States,Energy,US6267171022
1427 | Telecom Services,Liberty Global Ltd.,LBTYA,Bermuda,Communication Services,BMG611881019
1428 | Software - Application,"Global Business Travel Group, Inc.",GBTG,United States,Technology,US37890B1008
1429 | Utilities - Regulated Gas,Black Hills Corporation,BKH,United States,Utilities,US0921131092
1430 | Auto & Truck Dealerships,"CarGurus, Inc.",CARG,United States,Consumer Discretionary,US1417881091
1431 | Scientific & Technical Instruments,Sensata Technologies Holding plc,ST,United States,Technology,GB00BFMBMT84
1432 | Trucking,"RXO, Inc.",RXO,United States,Industrials,US74982T1034
1433 | Oil & Gas Equipment & Services,"Kodiak Gas Services, Inc.",KGS,United States,Energy,US50012A1088
1434 | Utilities - Regulated Electric,Oklo Inc.,OKLO,United States,Utilities,US02156V1098
1435 | Asset Management,"Golub Capital BDC, Inc.",GBDC,United States,Financials,US38173M1027
1436 | Specialty Business Services,UniFirst Corporation,UNF,United States,Industrials,US9047081040
1437 | Medical Instruments & Supplies,"ICU Medical, Inc.",ICUI,United States,Healthcare,US44930G1076
1438 | Banks - Regional,International Bancshares Corporation,IBOC,United States,Financials,US4590441030
1439 | Oil & Gas Exploration & Production,CNX Resources Corporation,CNX,United States,Energy,US12653C1080
1440 | Resorts & Casinos,Hilton Grand Vacations Inc.,HGV,United States,Consumer Discretionary,US43283X1054
1441 | Drug Manufacturers - General,Organon & Co.,OGN,United States,Healthcare,US68622V1061
1442 | Security & Protection Services,The Brink's Company,BCO,United States,Industrials,US1096961040
1443 | Banks - Regional,"Axos Financial, Inc.",AX,United States,Financials,US05465C1009
1444 | Packaged Foods,"Flowers Foods, Inc.",FLO,United States,Consumer Staples,US3434981011
1445 | Information Technology Services,ASGN Incorporated,ASGN,United States,Technology,US00191U1025
1446 | Real Estate Services,"Compass, Inc.",COMP,United States,Real Estate,US20464U1007
1447 | Insurance - Life,"CNO Financial Group, Inc.",CNO,United States,Financials,US12621E1038
1448 | Leisure,Acushnet Holdings Corp.,GOLF,United States,Consumer Discretionary,US0050981085
1449 | Security & Protection Services,"The GEO Group, Inc.",GEO,United States,Industrials,US36162J1060
1450 | Semiconductors,"Allegro MicroSystems, Inc.",ALGM,United States,Technology,US01749D1054
1451 | Utilities - Regulated Gas,Spire Inc.,SR,United States,Utilities,US84857L1017
1452 | Auto Parts,"Dorman Products, Inc.",DORM,United States,Consumer Discretionary,US2582781009
1453 | Utilities - Regulated Electric,Enel Chile S.A.,ENIC,Chile,Utilities,US29278D1054
1454 | Oil & Gas Midstream,Golar LNG Limited,GLNG,Bermuda,Energy,BMG9456A1009
1455 | Telecom Services,"Telephone and Data Systems, Inc.",TDS,United States,Communication Services,US8794338298
1456 | Software - Application,"BlackLine, Inc.",BL,United States,Technology,US09239B1098
1457 | Gambling,Super Group (SGHC) Limited,SGHC,Guernsey,Consumer Discretionary,GG00BMG42V42
1458 | Aerospace & Defense,"Spirit AeroSystems Holdings, Inc.",SPR,United States,Industrials,US8485741099
1459 | Medical Care Facilities,"Acadia Healthcare Company, Inc.",ACHC,United States,Healthcare,US00404A1097
1460 | Banks - Regional,Associated Banc-Corp,ASB,United States,Financials,US0454871056
1461 | Software - Application,"nCino, Inc.",NCNO,United States,Technology,US63947X1019
1462 | Credit Services,"Nelnet, Inc.",NNI,United States,Financials,US64031N1081
1463 | REIT - Healthcare Facilities,"Sabra Health Care REIT, Inc.",SBRA,United States,Real Estate,US78573L1061
1464 | Healthcare Plans,"Oscar Health, Inc.",OSCR,United States,Healthcare,US6877931096
1465 | Banks - Regional,"United Community Banks, Inc.",UCB,United States,Financials,US90984P3038
1466 | Software - Application,"Paycor HCM, Inc.",PYCR,United States,Technology,US70435P1021
1467 | Insurance - Diversified,"Goosehead Insurance, Inc",GSHD,United States,Financials,US38267D1090
1468 | Banks - Regional,"Flagstar Financial, Inc.",FLG,United States,Financials,US6494454001
1469 | Utilities - Regulated Gas,New Fortress Energy Inc.,NFE,United States,Utilities,US6443931000
1470 | Department Stores,"Nordstrom, Inc.",JWN,United States,Consumer Discretionary,US6556641008
1471 | Auto Manufacturers,WeRide Inc.,WRD,China,Consumer Discretionary,US94859U1034
1472 | Software - Application,JFrog Ltd.,FROG,United States,Technology,IL0011684185
1473 | Beverages - Non-Alcoholic,National Beverage Corp.,FIZZ,United States,Consumer Staples,US6350171061
1474 | REIT - Specialty,Rayonier Inc.,RYN,United States,Real Estate,US7549071030
1475 | Banks - Regional,BancFirst Corporation,BANF,United States,Financials,US05945F1030
1476 | Biotechnology,Scholar Rock Holding Corporation,SRRK,United States,Healthcare,US80706P1030
1477 | Utilities - Regulated Gas,"ONE Gas, Inc.",OGS,United States,Utilities,US68235P1084
1478 | Health Information Services,"BrightSpring Health Services, Inc.",BTSG,United States,Healthcare,US10950A1060
1479 | Education & Training Services,Graham Holdings Company,GHC,United States,Consumer Staples,US3846371041
1480 | Information Technology Services,Clarivate Plc,CLVT,United Kingdom,Technology,JE00BJJN4441
1481 | Medical Devices,PROCEPT BioRobotics Corporation,PRCT,United States,Healthcare,US74276L1052
1482 | Biotechnology,Ultragenyx Pharmaceutical Inc.,RARE,United States,Healthcare,US90400D1081
1483 | Drug Manufacturers - Specialty & Generic,Prestige Consumer Healthcare Inc.,PBH,United States,Healthcare,US74112D1019
1484 | Semiconductor Equipment & Materials,Camtek Ltd.,CAMT,Israel,Technology,IL0010952641
1485 | Oil & Gas Integrated,Crescent Energy Company,CRGY,United States,Energy,US44952J1043
1486 | Electronic Components,Plexus Corp.,PLXS,United States,Technology,US7291321005
1487 | Specialty Chemicals,Avient Corporation,AVNT,United States,Materials,US05368V1061
1488 | Medical Instruments & Supplies,DENTSPLY SIRONA Inc.,XRAY,United States,Healthcare,US24906P1093
1489 | Diagnostics & Research,Sotera Health Company,SHC,United States,Healthcare,US83601L1026
1490 | Engineering & Construction,Primoris Services Corporation,PRIM,United States,Industrials,US74164F1030
1491 | Biotechnology,Biohaven Ltd.,BHVN,United States,Healthcare,VGG1110E1079
1492 | Information Technology Services,DXC Technology Company,DXC,United States,Technology,US23355L1061
1493 | Software - Infrastructure,"DigitalOcean Holdings, Inc.",DOCN,United States,Technology,US25402D1028
1494 | Airlines,"Copa Holdings, S.A.",CPA,Panama,Industrials,PAP310761054
1495 | Packaged Foods,The Simply Good Foods Company,SMPL,United States,Consumer Staples,US82900L1026
1496 | Steel,"Grupo Simec, S.A.B. de C.V.",SIM,Mexico,Materials,US4004911065
1497 | Drug Manufacturers - Specialty & Generic,Alvotech,ALVO,Luxembourg,Healthcare,LU2458332611
1498 | Software - Application,"Blackbaud, Inc.",BLKB,United States,Technology,US09227Q1004
1499 | Specialty Retail,"Academy Sports and Outdoors, Inc.",ASO,United States,Consumer Discretionary,US00402L1070
1500 | REIT - Retail,Tanger Inc.,SKT,United States,Real Estate,US8754651060
1501 | Electrical Equipment & Parts,EnerSys,ENS,United States,Industrials,US29275Y1029
1502 | Biotechnology,"Avidity Biosciences, Inc.",RNA,United States,Healthcare,US05370A1088
1503 | Biotechnology,"Viking Therapeutics, Inc.",VKTX,United States,Healthcare,US92686J1060
1504 | Residential Construction,"Cavco Industries, Inc.",CVCO,United States,Consumer Discretionary,US1495681074
1505 | Biotechnology,"ADMA Biologics, Inc.",ADMA,United States,Healthcare,US0008991046
1506 | Specialty Industrial Machinery,Enpro Inc.,NPO,United States,Industrials,US29355X1072
1507 | Chemicals,Olin Corporation,OLN,United States,Materials,US6806652052
1508 | Airports & Air Services,"Grupo Aeroportuario del Centro Norte, S.A.B. de C.V.",OMAB,Mexico,Industrials,US4005011022
1509 | Utilities - Diversified,"ALLETE, Inc.",ALE,United States,Utilities,US0185223007
1510 | Software - Infrastructure,"Paymentus Holdings, Inc.",PAY,United States,Technology,US70439P1084
1511 | Lodging,Atour Lifestyle Holdings Limited,ATAT,China,Consumer Discretionary,US04965M1062
1512 | Utilities - Renewable,"Ormat Technologies, Inc.",ORA,United States,Utilities,US6866881021
1513 | REIT - Hotel & Motel,"Apple Hospitality REIT, Inc.",APLE,United States,Real Estate,US03784Y2000
1514 | Real Estate - Diversified,Howard Hughes Holdings Inc.,HHH,United States,Real Estate,US44267T1025
1515 | Semiconductors,"Impinj, Inc.",PI,United States,Technology,US4532041096
1516 | Software - Infrastructure,Payoneer Global Inc.,PAYO,United States,Technology,US70451X1046
1517 | Medical Instruments & Supplies,Envista Holdings Corporation,NVST,United States,Healthcare,US29415F1049
1518 | Biotechnology,"Immunovant, Inc.",IMVT,United States,Healthcare,US45258J1025
1519 | Engineering & Construction,Granite Construction Incorporated,GVA,United States,Industrials,US3873281071
1520 | Travel Services,Travel + Leisure Co.,TNL,United States,Consumer Discretionary,US8941641024
1521 | Banks - Regional,Fulton Financial Corporation,FULT,United States,Financials,US3602711000
1522 | Software - Application,"Alight, Inc.",ALIT,United States,Technology,US01626W1018
1523 | Oil & Gas Exploration & Production,"Northern Oil and Gas, Inc.",NOG,United States,Energy,US6655313079
1524 | Conglomerates,Griffon Corporation,GFF,United States,Industrials,US3984331021
1525 | Recreational Vehicles,BRP Inc.,DOOO,Canada,Consumer Discretionary,CA05577W2004
1526 | Staffing & Employment Services,Korn Ferry,KFY,United States,Industrials,US5006432000
1527 | Internet Content & Information,IAC Inc.,IAC,United States,Communication Services,US44891N2080
1528 | Residential Construction,"M/I Homes, Inc.",MHO,United States,Consumer Discretionary,US55305B1017
1529 | Building Materials,Tecnoglass Inc.,TGLS,Colombia,Materials,KYG872641009
1530 | Restaurants,"Sweetgreen, Inc.",SG,United States,Consumer Discretionary,US87043Q1085
1531 | Education & Training Services,Adtalem Global Education Inc.,ATGE,United States,Consumer Staples,US00737L1035
1532 | Computer Hardware,"Rigetti Computing, Inc.",RGTI,United States,Technology,US76655K1034
1533 | Banks - Regional,"Eastern Bankshares, Inc.",EBC,United States,Financials,US27627N1054
1534 | Oil & Gas Midstream,Frontline plc,FRO,Cyprus,Energy,CY0200352116
1535 | Specialty Industrial Machinery,"Crane NXT, Co.",CXT,United States,Industrials,US2244411052
1536 | Biotechnology,"Apellis Pharmaceuticals, Inc.",APLS,United States,Healthcare,US03753U1060
1537 | Capital Markets,"Riot Platforms, Inc.",RIOT,United States,Financials,US7672921050
1538 | Specialty Industrial Machinery,"Mueller Water Products, Inc.",MWA,United States,Industrials,US6247581084
1539 | Security & Protection Services,Brady Corporation,BRC,United States,Industrials,US1046741062
1540 | Telecom Services,"Globalstar, Inc.",GSAT,United States,Communication Services,US3789734080
1541 | Conglomerates,"MDU Resources Group, Inc.",MDU,United States,Industrials,US5526901096
1542 | Software - Application,"Alkami Technology, Inc.",ALKT,United States,Technology,US01644J1088
1543 | Software - Application,ZoomInfo Technologies Inc.,ZI,United States,Technology,US98980F1049
1544 | Software - Infrastructure,DLocal Limited,DLO,Uruguay,Technology,KYG290181018
1545 | Banks - Regional,"Texas Capital Bancshares, Inc.",TCBI,United States,Financials,US88224Q1076
1546 | Uranium,NexGen Energy Ltd.,NXE,Canada,Energy,CA65340P1062
1547 | Biotechnology,"Akero Therapeutics, Inc.",AKRO,United States,Healthcare,US00973Y1082
1548 | Information Technology Services,Concentrix Corporation,CNXC,United States,Technology,US20602D1019
1549 | Asset Management,Artisan Partners Asset Management Inc.,APAM,United States,Financials,US04316A1088
1550 | Software - Application,Rumble Inc.,RUM,United States,Technology,US78137L1052
1551 | Auto & Truck Dealerships,ACV Auctions Inc.,ACVA,United States,Consumer Discretionary,US00091G1040
1552 | REIT - Office,"Douglas Emmett, Inc.",DEI,United States,Real Estate,US25960P1093
1553 | Biotechnology,CRISPR Therapeutics AG,CRSP,Switzerland,Healthcare,CH0334081137
1554 | Utilities - Renewable,Brookfield Renewable Corporation,BEPC,United States,Utilities,CA11284V1058
1555 | REIT - Specialty,EPR Properties,EPR,United States,Real Estate,US26884U1097
1556 | Thermal Coal,"Alliance Resource Partners, L.P.",ARLP,United States,Energy,US01877R1086
1557 | Banks - Regional,TFS Financial Corporation,TFSL,United States,Financials,US87240R1077
1558 | Biotechnology,"Crinetics Pharmaceuticals, Inc.",CRNX,United States,Healthcare,US22663K1079
1559 | Telecom Services,"Cogent Communications Holdings, Inc.",CCOI,United States,Communication Services,US19239V3024
1560 | Software - Application,"Life360, Inc.",LIF,United States,Technology,
1561 | Residential Construction,"Tri Pointe Homes, Inc.",TPH,United States,Consumer Discretionary,US87265H1095
1562 | Medical Devices,"iRhythm Technologies, Inc.",IRTC,United States,Healthcare,US4500561067
1563 | Apparel Manufacturing,"Under Armour, Inc.",UAA,United States,Consumer Discretionary,US9043111072
1564 | Software - Application,"DoubleVerify Holdings, Inc.",DV,United States,Technology,US25862V1052
1565 | Recreational Vehicles,"Harley-Davidson, Inc.",HOG,United States,Consumer Discretionary,US4128221086
1566 | Biotechnology,"Rhythm Pharmaceuticals, Inc.",RYTM,United States,Healthcare,US76243J1051
1567 | Gold,Osisko Gold Royalties Ltd,OR,Canada,Materials,CA68827L1013
1568 | Capital Markets,StoneX Group Inc.,SNEX,United States,Financials,US8618961085
1569 | Biotechnology,"PTC Therapeutics, Inc.",PTCT,United States,Healthcare,US69366J2006
1570 | Pollution & Treatment Controls,Atmus Filtration Technologies Inc.,ATMU,United States,Industrials,US04956D1072
1571 | Internet Content & Information,Autohome Inc.,ATHM,China,Communication Services,US05278C1071
1572 | Banks - Regional,"First Interstate BancSystem, Inc.",FIBK,United States,Financials,US32055Y2019
1573 | Biotechnology,"Arcellx, Inc.",ACLX,United States,Healthcare,US03940C1009
1574 | Asset Management,"Hercules Capital, Inc.",HTGC,United States,Financials,US4270965084
1575 | Credit Services,The Western Union Company,WU,United States,Financials,US9598021098
1576 | Software - Infrastructure,"AvePoint, Inc.",AVPT,United States,Technology,US0536041041
1577 | Engineering & Construction,"Everus Construction Group, Inc.",ECG,United States,Industrials,US3004261034
1578 | Insurance - Life,"Brighthouse Financial, Inc.",BHF,United States,Financials,US10922N1037
1579 | Medical Instruments & Supplies,Haemonetics Corporation,HAE,United States,Healthcare,US4050241003
1580 | Entertainment,"Cinemark Holdings, Inc.",CNK,United States,Communication Services,US17243V1026
1581 | Gambling,International Game Technology PLC,IGT,United Kingdom,Consumer Discretionary,GB00BVG7F061
1582 | Oil & Gas Drilling,Transocean Ltd.,RIG,Switzerland,Energy,CH0048265513
1583 | Banks - Regional,"Community Financial System, Inc.",CBU,United States,Financials,US2036071064
1584 | Specialty Chemicals,H.B. Fuller Company,FUL,United States,Materials,US3596941068
1585 | Oil & Gas Refining & Marketing,PBF Energy Inc.,PBF,United States,Energy,US69318G1067
1586 | Telecom Services,Iridium Communications Inc.,IRDM,United States,Communication Services,US46269C1027
1587 | Gold,IAMGOLD Corporation,IAG,Canada,Materials,CA4509131088
1588 | Utilities - Renewable,Algonquin Power & Utilities Corp.,AQN,Canada,Utilities,CA0158571053
1589 | Banks - Regional,"First Hawaiian, Inc.",FHB,United States,Financials,US32051X1081
1590 | Other Industrial Metals & Mining,MP Materials Corp.,MP,United States,Materials,US5533681012
1591 | Real Estate Services,"Newmark Group, Inc.",NMRK,United States,Real Estate,US65158N1028
1592 | Discount Stores,BBB Foods Inc.,TBBB,Mexico,Consumer Staples,VGG0896C1032
1593 | Other Precious Metals & Mining,Hecla Mining Company,HL,United States,Materials,US4227041062
1594 | Banks - Regional,First BanCorp.,FBP,United States,Financials,PR3186727065
1595 | Diagnostics & Research,"Veracyte, Inc.",VCYT,United States,Healthcare,US92337F1075
1596 | Biotechnology,Denali Therapeutics Inc.,DNLI,United States,Healthcare,US24823R1059
1597 | Drug Manufacturers - Specialty & Generic,Perrigo Company plc,PRGO,Ireland,Healthcare,IE00BGH1M568
1598 | Oil & Gas Equipment & Services,Valaris Limited,VAL,Bermuda,Energy,BMG9460G1015
1599 | Scientific & Technical Instruments,ESCO Technologies Inc.,ESE,United States,Technology,US2963151046
1600 | Banks - Regional,Atlantic Union Bankshares Corporation,AUB,United States,Financials,US04911A1079
1601 | REIT - Office,COPT Defense Properties,CDP,United States,Real Estate,US22002T1088
1602 | Specialty Chemicals,Ashland Inc.,ASH,United States,Materials,US0441861046
1603 | Industrial Distribution,"Resideo Technologies, Inc.",REZI,United States,Industrials,US76118Y1047
1604 | Software - Application,"Clear Secure, Inc.",YOU,United States,Technology,US18467V1098
1605 | Banks - Regional,Cathay General Bancorp,CATY,United States,Financials,US1491501045
1606 | Apparel Manufacturing,"Under Armour, Inc.",UA,United States,Consumer Discretionary,US9043112062
1607 | Semiconductors,"Power Integrations, Inc.",POWI,United States,Technology,US7392761034
1608 | REIT - Specialty,PotlatchDeltic Corporation,PCH,United States,Real Estate,US7376301039
1609 | Banks - Regional,Intercorp Financial Services Inc.,IFS,Peru,Financials,PAL2400671A3
1610 | Insurance - Property & Casualty,"Hagerty, Inc.",HGTY,United States,Financials,US4051661092
1611 | Utilities - Regulated Electric,"NorthWestern Energy Group, Inc.",NWE,United States,Utilities,US6680743050
1612 | Oil & Gas Drilling,"Helmerich & Payne, Inc.",HP,United States,Energy,US4234521015
1613 | Building Products & Equipment,GMS Inc.,GMS,United States,Industrials,US36251C1036
1614 | Chemicals,Methanex Corporation,MEOH,Canada,Materials,CA59151K1084
1615 | Electronic Components,"OSI Systems, Inc.",OSIS,United States,Technology,US6710441055
1616 | Specialty Business Services,ABM Industries Incorporated,ABM,United States,Industrials,US0009571003
1617 | Building Materials,"United States Lime & Minerals, Inc.",USLM,United States,Materials,US9119221029
1618 | Oil & Gas Equipment & Services,Liberty Energy Inc.,LBRT,United States,Energy,US53115L1044
1619 | Real Estate Services,"HA Sustainable Infrastructure Capital, Inc.",HASI,United States,Real Estate,US41068X1000
1620 | Software - Application,"RingCentral, Inc.",RNG,United States,Technology,US76680R2067
1621 | Paper & Paper Products,Sylvamo Corporation,SLVM,United States,Materials,US8713321029
1622 | Banks - Regional,WSFS Financial Corporation,WSFS,United States,Financials,US9293281021
1623 | Electrical Equipment & Parts,"Hayward Holdings, Inc.",HAYW,United States,Industrials,US4212981009
1624 | Medical Care Facilities,"Surgery Partners, Inc.",SGRY,United States,Healthcare,US86881A1007
1625 | Specialty Business Services,First Advantage Corporation,FA,United States,Industrials,US31846B1089
1626 | Aerospace & Defense,"Intuitive Machines, Inc.",LUNR,United States,Industrials,US46125A1007
1627 | Medical Instruments & Supplies,Warby Parker Inc.,WRBY,United States,Healthcare,US93403J1060
1628 | Mortgage Finance,"Walker & Dunlop, Inc.",WD,United States,Financials,US93148P1021
1629 | Rental & Leasing Services,"Avis Budget Group, Inc.",CAR,United States,Industrials,US0537741052
1630 | Oil & Gas Drilling,"Patterson-UTI Energy, Inc.",PTEN,United States,Energy,US7034811015
1631 | Utilities - Diversified,Otter Tail Corporation,OTTR,United States,Utilities,US6896481032
1632 | "Furnishings, Fixtures & Appliances","Patrick Industries, Inc.",PATK,United States,Consumer Discretionary,US7033431039
1633 | Specialty Chemicals,Sensient Technologies Corporation,SXT,United States,Materials,US81725T1007
1634 | Rental & Leasing Services,"H&E Equipment Services, Inc.",HEES,United States,Industrials,US4040301081
1635 | Oil & Gas Midstream,"Excelerate Energy, Inc.",EE,United States,Energy,US30069T1016
1636 | Gambling,"Rush Street Interactive, Inc.",RSI,United States,Consumer Discretionary,US7820111000
1637 | Oil & Gas Exploration & Production,Gulfport Energy Corporation,GPOR,United States,Energy,US4026355028
1638 | Specialty Chemicals,WD-40 Company,WDFC,United States,Materials,US9292361071
1639 | Asset Management,Burford Capital Limited,BUR,Guernsey,Financials,GG00BMGYLN96
1640 | Apparel Retail,"American Eagle Outfitters, Inc.",AEO,United States,Consumer Discretionary,US02553E1064
1641 | Packaging & Containers,Pactiv Evergreen Inc.,PTVE,United States,Consumer Discretionary,US69526K1051
1642 | Leisure,"YETI Holdings, Inc.",YETI,United States,Consumer Discretionary,US98585X1046
1643 | Utilities - Regulated Electric,"MGE Energy, Inc.",MGEE,United States,Utilities,US55277P1049
1644 | Telecom Services,VEON Ltd.,VEON,Netherlands,Communication Services,US91822M5022
1645 | REIT - Diversified,"Broadstone Net Lease, Inc.",BNL,United States,Real Estate,US11135E2037
1646 | Oil & Gas Exploration & Production,Sitio Royalties Corp.,STR,United States,Energy,US82983N1081
1647 | Other Precious Metals & Mining,Triple Flag Precious Metals Corp.,TFPM,Canada,Materials,CA89679M1041
1648 | Software - Application,Grindr Inc.,GRND,United States,Technology,US39854F1012
1649 | Leisure,"Peloton Interactive, Inc.",PTON,United States,Consumer Discretionary,US70614W1009
1650 | Consumer Electronics,"LG Display Co., Ltd.",LPL,South Korea,Technology,US50186V1026
1651 | Utilities - Independent Power Producers,TransAlta Corporation,TAC,Canada,Utilities,CA89346D1078
1652 | REIT - Office,"Highwoods Properties, Inc.",HIW,United States,Real Estate,US4312841087
1653 | REIT - Healthcare Facilities,"National Health Investors, Inc.",NHI,United States,Real Estate,US63633D1046
1654 | Software - Infrastructure,"Core Scientific, Inc.",CORZ,United States,Technology,US21873J1088
1655 | Copper,Hudbay Minerals Inc.,HBM,Canada,Materials,CA4436281022
1656 | Semiconductors,Synaptics Incorporated,SYNA,United States,Technology,US87157D1090
1657 | Oil & Gas Exploration & Production,Veren Inc.,VRN,Canada,Energy,CA92340V1076
1658 | Other Precious Metals & Mining,Compañía de Minas Buenaventura S.A.A.,BVN,Peru,Materials,US2044481040
1659 | Farm & Heavy Construction Machinery,Terex Corporation,TEX,United States,Industrials,US8807791038
1660 | Real Estate Services,Cushman & Wakefield plc,CWK,United Kingdom,Real Estate,GB00BFZ4N465
1661 | Gold,B2Gold Corp.,BTG,Canada,Materials,CA11777Q2099
1662 | Airports & Air Services,Corporación América Airports S.A.,CAAP,Luxembourg,Industrials,LU1756447840
1663 | Software - Infrastructure,Teradata Corporation,TDC,United States,Technology,US88076W1036
1664 | Credit Services,"Bread Financial Holdings, Inc.",BFH,United States,Financials,US0185811082
1665 | REIT - Mortgage,"Blackstone Mortgage Trust, Inc.",BXMT,United States,Real Estate,US09257W1009
1666 | Medical Care Facilities,"LifeStance Health Group, Inc.",LFST,United States,Healthcare,US53228F1012
1667 | Oil & Gas Exploration & Production,"Black Stone Minerals, L.P.",BSM,United States,Energy,US09225M1018
1668 | Software - Infrastructure,"Five9, Inc.",FIVN,United States,Technology,US3383071012
1669 | Railroads,"Trinity Industries, Inc.",TRN,United States,Industrials,US8965221091
1670 | Insurance - Life,"Genworth Financial, Inc.",GNW,United States,Financials,US37247D1063
1671 | Gold,Eldorado Gold Corporation,EGO,Canada,Materials,CA2849025093
1672 | Diagnostics & Research,Twist Bioscience Corporation,TWST,United States,Healthcare,US90184D1000
1673 | Insurance - Specialty,"NMI Holdings, Inc.",NMIH,United States,Financials,US6292093050
1674 | Software - Application,"Alarm.com Holdings, Inc.",ALRM,United States,Technology,US0116421050
1675 | Semiconductor Equipment & Materials,IPG Photonics Corporation,IPGP,United States,Technology,US44980X1090
1676 | Medical Devices,QuidelOrtho Corporation,QDEL,United States,Healthcare,US2197981051
1677 | Asset Management,"Federated Hermes, Inc.",FHI,United States,Financials,US3142111034
1678 | Semiconductor Equipment & Materials,"Ambarella, Inc.",AMBA,United States,Technology,KYG037AX1015
1679 | Biotechnology,ACADIA Pharmaceuticals Inc.,ACAD,United States,Healthcare,US0042251084
1680 | Resorts & Casinos,Marriott Vacations Worldwide Corporation,VAC,United States,Consumer Discretionary,US57164Y1073
1681 | Banks - Regional,"BankUnited, Inc.",BKU,United States,Financials,US06652K1034
1682 | Biotechnology,Xenon Pharmaceuticals Inc.,XENE,Canada,Healthcare,CA98420N1050
1683 | Specialty Industrial Machinery,"Mirion Technologies, Inc.",MIR,United States,Industrials,US60471A1016
1684 | REIT - Specialty,OUTFRONT Media Inc.,OUT,United States,Real Estate,US69007J1060
1685 | Resorts & Casinos,"PENN Entertainment, Inc.",PENN,United States,Consumer Discretionary,US7075691094
1686 | Oil & Gas Refining & Marketing,Ultrapar Participações S.A.,UGP,Brazil,Energy,US90400P1012
1687 | Chemicals,Huntsman Corporation,HUN,United States,Materials,US4470111075
1688 | Medical Care Facilities,"Amedisys, Inc.",AMED,United States,Healthcare,US0234361089
1689 | Luxury Goods,Capri Holdings Limited,CPRI,United Kingdom,Consumer Discretionary,VGG1890L1076
1690 | Rental & Leasing Services,McGrath RentCorp,MGRC,United States,Industrials,US5805891091
1691 | Banks - Regional,Bank of Hawaii Corporation,BOH,United States,Financials,US0625401098
1692 | Footwear & Accessories,"Steven Madden, Ltd.",SHOO,United States,Consumer Discretionary,US5562691080
1693 | Staffing & Employment Services,"Insperity, Inc.",NSP,United States,Industrials,US45778Q1076
1694 | Medical Care Facilities,"Concentra Group Holdings Parent, Inc.",CON,United States,Healthcare,US20603L1026
1695 | Apparel Retail,Victoria's Secret & Co.,VSCO,United States,Consumer Discretionary,US9264001028
1696 | Restaurants,The Wendy's Company,WEN,United States,Consumer Discretionary,US95058W1009
1697 | Packaging & Containers,"Greif, Inc.",GEF.B,United States,Consumer Discretionary,US3976242061
1698 | Biotechnology,Vericel Corporation,VCEL,United States,Healthcare,US92346J1088
1699 | Utilities - Renewable,"Clearway Energy, Inc.",CWEN,United States,Utilities,US18539C2044
1700 | Credit Services,"Enova International, Inc.",ENVA,United States,Financials,US29357K1034
1701 | Oil & Gas Equipment & Services,"USA Compression Partners, LP",USAC,United States,Energy,US90290N1090
1702 | Uranium,Uranium Energy Corp.,UEC,United States,Energy,US9168961038
1703 | Semiconductor Equipment & Materials,"FormFactor, Inc.",FORM,United States,Technology,US3463751087
1704 | Apparel Manufacturing,Hanesbrands Inc.,HBI,United States,Consumer Discretionary,US4103451021
1705 | Biotechnology,"Recursion Pharmaceuticals, Inc.",RXRX,United States,Healthcare,US75629V1044
1706 | Broadcasting,TEGNA Inc.,TGNA,United States,Communication Services,US87901J1051
1707 | Banks - Regional,CVB Financial Corp.,CVBF,United States,Financials,US1266001056
1708 | Healthcare Plans,"Alignment Healthcare, Inc.",ALHC,United States,Healthcare,US01625V1044
1709 | Packaging & Containers,"Greif, Inc.",GEF,United States,Consumer Discretionary,US3976241071
1710 | Biotechnology,Zai Lab Limited,ZLAB,China,Healthcare,US98887Q1040
1711 | Specialty Retail,"Advance Auto Parts, Inc.",AAP,United States,Consumer Discretionary,US00751Y1064
[TRUNCATED]
```

src/diagram.md
```
1 | ```mermaid
2 | flowchart TD
3 | 
4 |     A@{ shape: sl-rect, label: "*Company Identifier* <br> <sub><sup>Name, Ticker, or ISIN </sub></sup>"}
5 |     A --> B@{ shape: rect, label: "Create Company Profile <br> <sub><sup> *retrieve company name if not provided* </sub></sup>"}
6 |     B --> BB@{ shape: fr-rect, label: "Search for Latest News"}
7 |     BB --> BB1@{ shape: stadium, label: "Display News"}
8 |     B --> C@{ shape: lin-cyl, label: "Query Database <br> <sub><sup> *search for cached tables* </sub></sup>"}
9 |     C --> D@{ shape: hexagon, label: "Is Data Recent? <br> <sub><sup> *check for viability of data* </sub></sup>"}
10 |     D -->|*Yes*| E@{ shape: stadium, label: "Display Emissions Data"}
11 |     D -->|*No*| F@{ shape: fr-rect, label: "Search for ESG Report"}
12 |     F --> G@{ shape: lin-cyl, label: "Download Latest Report"}
13 |     G --> H@{ shape: fr-rect, label: "Parse PDF with Docling"}
14 |     H --> I@{ shape: fr-rect, label: "Filter parsed PDF <br> <sub><sup> *search for Scope 1 & 2 figures* </sub></sup>"}
15 |     I --> II@{ shape: hexagon, label: "Is Scope 1 & 2 Data Present?"}
16 |     II --> |*Yes*| J@{ shape: lin-cyl, label: "Save emissions data"}
17 |     II --> |*No*| JJ@{ shape: fr-rect, label: "Parse PDF with LlamaParse"}
18 |     J --> K@{ shape: stadium, label: "Display Emissions Data"}
19 |     JJ --> L@{ shape: fr-rect, label: "Filter parsed PDF <br> <sub><sup> *search for Scope 1 & 2 figures* </sub></sup>"}
20 |     L --> M@{ shape: lin-cyl, label: "Save emissions data"}
21 |     M --> N@{ shape: stadium, label: "Display Emissions Data"}
22 | ```
```

src/emissimap3.csv
```
1 | Latitude,Longitude,Company,Emissions
2 | 47°64,-122°00,Apple,16.8
3 | 47°64,-122°13,Microsoft,15.4
4 | 37°42,-122°08,Alphabet,24.9
5 | 18°28,42°53,Saudi Aramco,47
6 | 37°37,-121°96,Nvidia,12.2
7 | 47°61,-122°34,Amazon ,26.1
8 | 24°76,120° 998,Taiwan Semiconductor Company,13.7
9 | 30°2,120°19,Alibaba,13.23
10 | 51°51,-0°02,HSBC,24.2
11 | 37°78,-122°41,Visa,15.4
12 | 37°45,-122°18,Meta,32.7
13 | 30°22,-97°62,Tesla ,24.7
14 | 37°34,-121°89,Broadcom,19.2
15 | 39°77,-86°16,Eli Lilly,23.6
16 | 41°26,-95°93,Berkshire Hathaway,26.2
17 | 36°37,-94°21,Walmart,25
18 | 22°53,113°93,Tencent,18.8
19 | 37°53,-122°27,Oracle,14.9
20 | 30°07,-95°42,Exxon Mobil ,43.7
21 | 33°87,-84°34,Home Depot,12.6
22 | 37°77,-122°42,Wells Fargo,34.4
23 | 37°24,-121°96,Netflix ,15.6
24 | 37°50,127°03,Samsung,15
25 | 40°76,-73°98,Bank of America,24.3
26 | 40°76,7°59,Roche ,23.8
27 | 33°75,-84°39,Coca Cola ,24.2
28 | 51°41,5°41,ASML,8.5
29 | 49°29,8°64,SAP,14.4
30 | 48°87,2°31,LVMH,13.9
31 | 55°76,12°46,Novo Nordisk ,23.2
32 | 39°10,-84°51,Procter & Gamble ,24.9
33 | 47°55,-122°05,Costco ,29.1
34 | 41°03,-73°72,Mastercard,16.1
35 | 37°79,-122°40,Salesforce,15.2
36 | 40°76,-73°96,JP Morgan Chase,27.3
37 | 44°90,-93°40,UnitedHealth,16.6
38 | 40°49,-74°45,Johnson&Johnson ,20.1
39 | 42°34,-87°83,AbbVie,26.1
40 | 48°87,2°31,Hermes,16.6
```

src/main.py
```
1 | import csv
2 | import logging
3 | import os
4 | import re
5 | import sys
6 | import threading
7 | from io import BytesIO
8 | from threading import Event
9 | 
10 | import folium
11 | import pandas as pd
12 | import yfinance as yf
13 | from dotenv import load_dotenv
14 | from flask import (
15 |     Flask,
16 |     Response,
17 |     jsonify,
18 |     redirect,
19 |     render_template,
20 |     request,
21 |     send_file,
22 |     send_from_directory,
23 |     url_for,
24 | )
25 | from flask_socketio import SocketIO
26 | 
27 | load_dotenv()
28 | # append path
29 | sys.path.append(f"{os.getenv('ROOT_DIR')}")
30 | logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
31 | 
32 | import src.utils.rag_utils as rag_utils  # noqa: E402
33 | from src.find.company_profile import CompanyProfile  # noqa: E402
34 | from src.find.esg_reports import ESGReports  # noqa: E402
35 | from src.scripts.retrieve_emissions_data import get_emissions_data  # noqa: E402
36 | 
37 | # LLM-based table extraction
38 | from src.scripts.retrieve_emissions_data_pro import get_emissions_data_pro  # noqa: E402
39 | from src.utils.data_models import TableParsers  # noqa: E402
40 | 
41 | # Globals for RAG
42 | rag_chain = None
43 | rag_initialized = False
44 | pdf_path_global = None
45 | 
46 | app = Flask(__name__)
47 | socketio = SocketIO(app, cors_allowed_origins="*")  # Allows cross-origin requests
48 | 
49 | for rule in app.url_map.iter_rules():
50 |     print(rule)
51 | 
52 | # Get the absolute path of the correct static folder
53 | BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
54 | STATIC_FOLDER = os.path.join(BASE_DIR, "static", "images")
55 | 
56 | # Ensure the correct static/images directory exists
57 | os.makedirs(STATIC_FOLDER, exist_ok=True)
58 | 
59 | 
60 | def dms_to_decimal(dms):
61 |     match = re.match(r"(-?\d+)°(\d+)?", dms)  # Support negative values
62 |     if match:
63 |         degrees = int(match.group(1))  # Handle negative degrees
64 |         minutes = int(match.group(2)) if match.group(2) else 0
65 |         return degrees + (minutes / 60)
66 |     return None  # Return None if format is incorrect
67 | 
68 | 
69 | df = pd.read_csv("src/emissimap3.csv")
70 | # Ensure required columns exist
71 | print(df.head())
72 | df["Latitude"] = df["Latitude"].apply(dms_to_decimal)
73 | df["Longitude"] = df["Longitude"].apply(dms_to_decimal)
74 | print(df)
75 | 
76 | # Create a base map
77 | m = folium.Map(location=[20, 0], zoom_start=2)
78 | 
79 | 
80 | # Define a color scale based on emissions level
81 | def get_color(emissions):
82 |     if emissions < 1000:
83 |         return "green"
84 |     elif 1000 <= emissions < 5000:
85 |         return "orange"
86 |     else:
87 |         return "red"
88 | 
89 | 
90 | # Add markers for each company
91 | for _, row in df.iterrows():
92 |     print(
93 |         f"Adding marker: {row['Company']} ({row['Latitude']}, {row['Longitude']}) - {row['Emissions']} CO2"
94 |     )
95 | 
96 |     folium.CircleMarker(
97 |         location=[row["Latitude"], row["Longitude"]],
98 |         radius=5 + (row["Emissions"] / 1000),
99 |         color="red",
100 |         fill=True,
101 |         fill_color="red",
102 |         fill_opacity=0.7,
103 |         popup=f"{row['Company']} - {row['Emissions']} CO2",
104 |     ).add_to(m)
105 | 
106 | # Save map to an HTML file
107 | map_path = os.path.join(STATIC_FOLDER, "emissions_map.html")
108 | m.save(map_path)
109 | 
110 | print(f"Map saved as {map_path}")
111 | 
112 | 
113 | @app.route("/static/images/emissions_map.html")
114 | def serve_emissions_map():
115 |     return send_from_directory("static/images", "emissions_map.html")
116 | 
117 | 
118 | @app.route("/emissions_map")
119 | def emissions_map():
120 |     return render_template("maps.html")
121 | 
122 | 
123 | @app.route("/firstpage")
124 | def firstpage():
125 |     return render_template("firstpage.html")
126 | 
127 | 
128 | @app.route("/instructions")
129 | def instructions():
130 |     return render_template("instructions.html")
131 | 
132 | 
133 | @app.route("/instructionspremium")
134 | def instructionspremium():
135 |     return render_template("instructionspremium.html")
136 | 
137 | 
138 | def normalize_name(name):
139 |     """Normalize company name for better matching."""
140 |     name = name.strip().upper()
141 | 
142 |     # Remove common suffixes
143 |     name = re.sub(r"[.,'’]", "", name)  # Remove punctuation
144 |     name = re.sub(
145 |         r"\b(INC|LTD|CO|CORPORATION|CORP|LLC|GROUP|HOLDINGS|PLC)\b", "", name
146 |     )  # Remove suffixes
147 |     name = re.sub(r"\s+", " ", name).strip()  # Remove extra spaces
148 | 
149 |     print(f"[DEBUG] Normalized name: '{name}'")  # Debugging output
150 |     return name
151 | 
152 | 
153 | @app.route("/get_news", methods=["POST"])
154 | def get_news_route():
155 |     company_name = request.form.get("company_name")
156 |     if not company_name:
157 |         return jsonify({"error": "Please enter a company name."}), 400
158 | 
159 |     news_data = get_news(company_name)
160 | 
161 |     print(f"News data for {company_name}: {news_data}")
162 | 
163 |     return jsonify(
164 |         {
165 |             "company_name": company_name,
166 |             "news_data": news_data,
167 |         }
168 |     )
169 | 
170 | 
171 | def format_news(raw_news):
172 |     """Helper function to format news data correctly, including images."""
173 |     if not raw_news or not isinstance(raw_news, list):
174 |         print("[ERROR] News data is empty or not a list")
175 |         return []
176 | 
177 |     news_data = []
178 |     for article in raw_news:
179 |         try:
180 |             content = article.get("content", {})
181 |             if not isinstance(content, dict):
182 |                 print(f"[ERROR] Invalid content format: {content}")
183 |                 continue
184 | 
185 |             title = content.get("title", "No title available")
186 |             publisher = content.get("provider", {}).get("displayName", "Unknown source")
187 | 
188 |             # Extract the news link
189 |             link_data = content.get("clickThroughUrl") or content.get("canonicalUrl")
190 |             link = link_data.get("url") if isinstance(link_data, dict) else "#"
191 | 
192 |             # Extract the image URL
193 |             image_url = (
194 |                 content.get("thumbnail", {}).get("resolutions", [{}])[0].get("url", "")
195 |             )
196 | 
197 |             news_data.append(
198 |                 {
199 |                     "title": title,
200 |                     "publisher": publisher,
201 |                     "link": link,
202 |                     "image": image_url,  # Add image URL
203 |                 }
204 |             )
205 |         except Exception as e:
206 |             print(f"[ERROR] Error formatting news article: {e}")
207 | 
208 |     return news_data
209 | 
210 | 
211 | TICKER_CSV_PATH = "src/company_names_tickers_news.csv"
212 | 
213 | 
214 | # Function to load tickers from CSV file
215 | def load_ticker_map(csv_path):
216 |     ticker_map = {}
217 |     isin_map = {}
218 | 
219 |     try:
220 |         with open(csv_path, mode="r", encoding="utf-8") as file:
221 |             reader = csv.DictReader(file)
222 |             headers = [header.strip().upper() for header in reader.fieldnames]
223 | 
224 |             if (
225 |                 not headers
226 |                 or "COMPANY NAME" not in headers
227 |                 or "SYMBOL" not in headers
228 |                 or "ISIN NUMBER" not in headers
229 |             ):
230 |                 print(f"[ERROR] CSV file is missing required headers: {headers}")
231 |                 return {}, {}
232 | 
233 |             for row in reader:
234 |                 company = normalize_name(
235 |                     row["Company Name"]
236 |                 )  # Normalize before storing
237 |                 ticker = row["Symbol"].strip().upper()
238 |                 isin = row["ISIN Number"].strip().upper()
239 | 
240 |                 if company and ticker:
241 |                     ticker_map[company] = ticker
242 |                 if isin and ticker:
243 |                     isin_map[isin] = ticker
244 | 
245 |         print(f"[DEBUG] Ticker map loaded with {len(ticker_map)} entries")
246 |         print(f"[DEBUG] ISIN map loaded with {len(isin_map)} entries")
247 | 
248 |     except Exception as e:
249 |         print(f"[ERROR] Failed to load ticker map: {e}")
250 | 
251 |     return ticker_map, isin_map
252 | 
253 | 
254 | # Load at startup
255 | MANUAL_TICKER_MAP, MANUAL_ISIN_MAP = load_ticker_map(TICKER_CSV_PATH)
256 | 
257 | 
258 | def get_ticker(identifier):
259 |     """Retrieve the stock ticker symbol for a given company name or ISIN."""
260 |     identifier = normalize_name(identifier)  # Normalize user input
261 | 
262 |     print(f"[DEBUG] Normalized identifier: '{identifier}'")
263 | 
264 |     # First, check if it's an ISIN
265 |     if identifier in MANUAL_ISIN_MAP:
266 |         print(f"[DEBUG] Found ticker in ISIN map: {MANUAL_ISIN_MAP[identifier]}")
267 |         return MANUAL_ISIN_MAP[identifier]
268 | 
269 |     # Second, check if it's an exact company name match
270 |     if identifier in MANUAL_TICKER_MAP:
271 |         print(f"[DEBUG] Found ticker in company map: {MANUAL_TICKER_MAP[identifier]}")
272 |         return MANUAL_TICKER_MAP[identifier]
273 | 
274 |     # Third, try to find a close match in the manual map
275 |     for stored_name, ticker in MANUAL_TICKER_MAP.items():
276 |         if identifier in stored_name or stored_name in identifier:
277 |             print(f"[DEBUG] Found ticker by fuzzy match: {stored_name} -> {ticker}")
278 |             return ticker
279 | 
280 |     print(f"[DEBUG] {identifier} not found in manual maps, searching Yahoo Finance...")
281 | 
282 |     # If no match, try to query Yahoo Finance
283 |     try:
284 |         search_results = yf.Ticker(identifier)
285 |         if search_results.history(period="1d").empty:
286 |             print(f"[DEBUG] No historical data found for: {identifier}")
287 |             return None
288 | 
289 |         print(f"[DEBUG] Found ticker dynamically: {search_results.ticker}")
290 |         return search_results.ticker
291 |     except Exception as e:
292 |         print(f"[ERROR] Error retrieving ticker: {e}")
293 |         return None
294 | 
295 | 
296 | def get_news(company_name):
297 |     try:
298 |         ticker_symbol = get_ticker(company_name)
299 |         if not ticker_symbol:
300 |             print(f"[DEBUG] No ticker found for {company_name}")
301 |             return []
302 | 
303 |         ticker = yf.Ticker(ticker_symbol)
304 |         raw_news = ticker.news
305 | 
306 |         if not isinstance(
307 |             raw_news, list
308 |         ):  # Ensure raw_news is a list before processing
309 |             print(
310 |                 f"[ERROR] Unexpected news format for {ticker_symbol}: {type(raw_news)}"
311 |             )
312 |             return []
313 | 
314 |         print(f"[DEBUG] Raw news data for {ticker_symbol}: {raw_news}")
315 | 
316 |         return format_news(raw_news)
317 | 
318 |     except Exception as e:
319 |         print(f"[ERROR] Error retrieving news: {e}")
320 |         return []
321 | 
322 | 
323 | print(get_news("Apple"))
324 | 
325 | 
326 | @app.route("/download_table")
327 | def download_table():
328 |     """Generate and serve the emissions data as a CSV file for download."""
329 |     company_name = request.args.get("company_name")
330 |     parser = TableParsers.DOCLING
331 | 
332 |     if not company_name:
333 |         return "Company name is required!", 400
334 | 
335 |     data, report_url = get_emissions_data(company_name, idType="name", parser=parser)
336 | 
337 |     if not isinstance(data, pd.DataFrame) or data.empty:
338 |         return "No data available for download.", 404
339 | 
340 |     csv_buffer = BytesIO()
341 |     data.to_csv(csv_buffer, index=False)
342 |     csv_buffer.seek(0)
343 | 
344 |     return send_file(
345 |         csv_buffer,
346 |         mimetype="text/csv",
347 |         as_attachment=True,
348 |         download_name=f"{company_name}_emissions.csv",
349 |     )
350 | 
351 | 
352 | stop_rag_event = Event()
353 | 
354 | 
355 | ################################################################
356 | # 1) Tables on the left
357 | ################################################################
358 | @app.route("/index", methods=["GET", "POST"])
359 | def home():
360 |     """
361 |     Updated route to handle form submissions for a new company,
362 |     re-run LLM extraction, and pass data to index.html for the
363 |     chatbot, chart, and extracted tables.
364 |     """
365 |     company_name = None
366 |     report_url = None
367 |     llm_markdown = ""
368 |     pdf_path = None
369 | 
370 |     if request.method == "POST":
371 |         # Force-stop any old RAG job
372 |         rag_utils.stop_rag_event.set()
373 | 
374 |         # Clear out old chain
375 |         rag_utils.rag_chain = None
376 |         rag_utils.rag_initialized = False
377 | 
378 |         # Normal "search" logic
379 |         company_name = request.form.get("company_name", "").strip()
380 |         selected_id_type = request.form.get("idType", "name")
381 | 
382 |         if company_name:
383 |             parser = TableParsers.DOCLING
384 |             df, pdf_path = get_emissions_data_pro(
385 |                 company_name, selected_id_type, parser
386 |             )
387 |             if not df.empty and "LLM_Output" in df.columns:
388 |                 llm_markdown = df["LLM_Output"].iloc[0]
389 |             else:
390 |                 llm_markdown = "No emissions data found for this company."
391 | 
392 |             # Store the PDF path in rag_utils
393 |             rag_utils.pdf_path_global = pdf_path
394 | 
395 |             esg_reports = ESGReports(CompanyProfile(company_name, selected_id_type))
396 |             print(f"DEBUG: ESGReports URLs -> {esg_reports.urls}")  # Debugging
397 | 
398 |             # Extract the first available report URL
399 |             if esg_reports.urls:
400 |                 report_url = next(
401 |                     iter(esg_reports.urls.values())
402 |                 )  # Get first URL dynamically
403 | 
404 |             print(f"DEBUG: Selected Report URL -> {report_url}")
405 | 
406 |     return render_template(
407 |         "index.html",
408 |         company_name=company_name,
409 |         report_url=report_url,
410 |         llm_markdown=llm_markdown,
411 |     )
412 | 
413 | 
414 | ################################################################
415 | # 3) RAG Endpoints
416 | ################################################################
417 | @app.route("/rag_init", methods=["POST"])
418 | def rag_init():
419 |     """
420 |     Trigger RAG building in a background thread so it doesn't block.
421 |     """
422 |     if rag_utils.rag_chain is not None or rag_utils.rag_initialized:
423 |         return jsonify({"status": "RAG already initialized"})
424 | 
425 |     if not rag_utils.pdf_path_global or not os.path.isfile(rag_utils.pdf_path_global):
426 |         return jsonify({"status": "No valid original PDF to build RAG from."})
427 | 
428 |     # Clear the stop event
429 |     rag_utils.stop_rag_event.clear()
430 | 
431 |     def init_rag_in_background(path):
432 |         logging.info("Starting RAG initialization in background...")
433 |         try:
434 |             if rag_utils.stop_rag_event.is_set():
435 |                 logging.info("Stop event was set before starting RAG initialization")
436 |                 return
437 |             chain = rag_utils.build_final_system(path)
438 |             if rag_utils.stop_rag_event.is_set() or chain is None:
439 |                 logging.info(
440 |                     "Stop event was set during RAG initialization or chain creation failed"
441 |                 )
442 |                 return
443 |             rag_utils.rag_chain = chain
444 |             rag_utils.rag_initialized = True
445 |             logging.info("RAG system successfully initialized.")
446 |         except Exception as e:
447 |             logging.error(f"Failed to build RAG: {e}")
448 |             rag_utils.rag_chain = None
449 |             rag_utils.rag_initialized = False
450 | 
451 |     thread = threading.Thread(
452 |         target=init_rag_in_background, args=(rag_utils.pdf_path_global,)
453 |     )
454 |     thread.start()
455 | 
456 |     return jsonify({"status": "RAG initialization started"})
457 | 
458 | 
459 | @app.route("/ask", methods=["POST"])
460 | def ask_question():
461 |     """
462 |     POST route for user queries to the RAG.
463 |     """
464 |     question = request.form.get("question", "")
465 |     if not question:
466 |         return jsonify({"answer": "No question provided."})
467 | 
468 |     if not rag_utils.rag_chain or not rag_utils.rag_initialized:
469 |         return jsonify({"answer": "RAG is not initialized yet. Please wait."})
470 | 
471 |     try:
472 |         answer = rag_utils.rag_chain.invoke(question)
473 |         return jsonify({"answer": answer})
474 |     except Exception as e:
475 |         logging.error(f"Error in RAG QA: {e}")
476 |         return jsonify({"answer": f"Error: {str(e)}"})
477 | 
478 | 
479 | @app.route("/reset_rag", methods=["POST"])
480 | def reset_rag():
481 |     rag_utils.stop_rag_event.set()
482 |     rag_utils.rag_chain = None
483 |     rag_utils.rag_initialized = False
484 |     return jsonify({"status": "RAG reset"})
485 | 
486 | 
487 | df = pd.read_csv("src/company_names_tickers.csv")
488 | 
489 | unique_countries = sorted(df["Country"].dropna().astype(str).unique().tolist())
490 | unique_sectors = sorted(df["Sector"].dropna().astype(str).unique().tolist())
491 | unique_industries = sorted(df["Industry"].dropna().astype(str).unique().tolist())
492 | 
493 | 
494 | @app.route("/advanced_search")
495 | def advanced_search():
496 |     return render_template(
497 |         "advanced_search.html",
498 |         countries=unique_countries,
499 |         sectors=unique_sectors,
500 |         industries=unique_industries,
501 |         companies=[],
502 |         selected_company=None,
503 |         emissions_data=None,
504 |         report_url=None,
505 |     )
506 | 
507 | 
508 | @app.route("/submit", methods=["POST"])
509 | def submit():
510 |     # Retrieve form data
511 |     sector = request.form["sector"]
512 |     country = request.form["country"]
513 |     industry = request.form["industry"]
514 |     selected_company = request.form.get("company")  # Get the selected company
515 | 
516 |     filtered_df = df
517 |     if sector != "all":
518 |         filtered_df = filtered_df[filtered_df["Sector"] == sector]
519 |     if country != "all":
520 |         filtered_df = filtered_df[filtered_df["Country"] == country]
521 |     if industry != "all":
522 |         filtered_df = filtered_df[filtered_df["Industry"] == industry]
523 | 
524 |     selected_companies = filtered_df["Company Name"].drop_duplicates().tolist()
525 | 
526 |     report_url = None
527 |     emissions_data = None
528 |     if selected_company:
529 |         try:
530 |             parser = TableParsers.DOCLING
531 |             emissions_data, report_url = get_emissions_data(
532 |                 selected_company, idType="name", parser=parser
533 |             )
534 | 
535 |         except Exception as e:
536 |             print(f"Error retrieving emissions data for {selected_company}: {e}")
537 |             emissions_data = None
538 | 
539 |             esg_reports = ESGReports(CompanyProfile(selected_company, idType="name"))
540 |             print(f"DEBUG: ESGReports URLs -> {esg_reports.urls}")  # Debugging
541 | 
542 |             # Extract the first available report URL
543 |             if esg_reports.urls:
544 |                 report_url = next(
545 |                     iter(esg_reports.urls.values())
546 |                 )  # Get first URL dynamically
547 | 
548 |             print(f"DEBUG: Selected Report URL -> {report_url}")
549 | 
550 |     return render_template(
551 |         "advanced_search.html",
552 |         companies=selected_companies,
553 |         countries=unique_countries,
554 |         sectors=unique_sectors,
555 |         industries=unique_industries,
556 |         selected_company=selected_company,
557 |         report_url=report_url,
558 |         emissions_data=(
559 |             emissions_data.to_html(index=False) if emissions_data is not None else None
560 |         ),
561 |     )
562 | 
563 | 
564 | @app.route("/test", methods=["GET", "POST"])
565 | def test():
566 |     table_html = ""
567 |     report_url = None
568 |     company_name = ""
569 |     news_data = []
570 | 
571 |     if request.method == "POST":
572 |         company_name = request.form.get("company_name")  # Get the text input
573 |         parser = TableParsers.DOCLING
574 |         selected_id_type = request.form.get("idType", "name")
575 | 
576 |         if company_name:
577 |             result = get_emissions_data(
578 |                 company_name, idType=selected_id_type, parser=parser
579 |             )
580 | 
581 |             if isinstance(result, tuple) and len(result) == 2:
582 |                 data, report_url = result
583 |                 table_html = (
584 |                     data.to_html(index=False)
585 |                     if isinstance(data, pd.DataFrame) and not data.empty
586 |                     else "<p>No data found.</p>"
587 |                 )
588 |             else:
589 |                 # Handle cases where no data is returned
590 |                 data, report_url = None, None
591 |                 table_html = "<p>No data found.</p>"
592 | 
593 |     news_data = get_news(company_name)
594 | 
595 |     return render_template(
596 |         "test.html",
597 |         table_html=table_html,
598 |         report_url=report_url,
599 |         company_name=company_name,
600 |         news_data=news_data,
601 |     )
602 | 
603 | 
604 | @app.route("/progress/<socketid>", methods=["POST"])
605 | def progress(socketid):
606 |     def background_task():
607 |         for x in range(1, 6):  # Updates from 20% to 100%
608 |             socketio.emit("update_progress", {"progress": x * 20}, room=socketid)
609 |             socketio.sleep(5)  # Wait 5 seconds before sending the next update
610 | 
611 |         # Emit event when progress reaches 100%
612 |         socketio.emit("progress_complete", room=socketid)
613 | 
614 |     socketio.start_background_task(background_task)
615 |     return Response(status=204)
616 | 
617 | 
618 | @app.route("/register")
619 | def register():
620 |     return render_template("register.html")
621 | 
622 | 
623 | VALID_USERS = {"test@example.com": "password123"}
624 | 
625 | 
626 | @app.route("/login", methods=["GET", "POST"])
627 | def login():
628 |     if request.method == "POST":
629 |         email = request.form.get("email")
630 |         password = request.form.get("password")
631 | 
632 |         # Check credentials
633 |         if email in VALID_USERS and VALID_USERS[email] == password:
634 |             return redirect(url_for("home"))  # Redirects to the index page
635 | 
636 |         return render_template("login.html", error="Invalid email or password")
637 | 
638 |     return render_template("login.html")
639 | 
640 | 
641 | @app.route("/rag_status", methods=["GET"])
642 | def rag_status():
643 |     """
644 |     Returns whether the RAG system is initialized yet.
645 |     The front end can poll this to update the UI.
646 |     """
647 |     return jsonify({"initialized": rag_utils.rag_initialized})
648 | 
649 | 
650 | if __name__ == "__main__":
651 |     socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
```

.github/workflows/python-lint-and-test.yml
```
1 | # This workflow will install Python dependencies, run tests and lint with a single version of Python
2 | # For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python
3 | 
4 | name: esg-data-retrieval
5 | 
6 | on:
7 |   push:
8 |     branches: [ "main" ]
9 |   pull_request:
10 |     branches: [ "main" ]
11 | 
12 | permissions:
13 |   contents: read
14 | 
15 | jobs:
16 |   build:
17 | 
18 |     runs-on: ubuntu-latest
19 | 
20 |     steps:
21 |     - uses: actions/checkout@v4
22 |     - name: Set up Python 3.10
23 |       uses: actions/setup-python@v3
24 |       with:
25 |         python-version: "3.10"
26 |     - name: Install dependencies
27 |       run: |
28 |         python -m pip install --upgrade pip
29 |         pip install isort black flake8 pytest
30 |         if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
31 |     - name: Lint with black
32 |       run: |
33 |         # stop build if any black errors spotted
34 |         black . --check
35 |     - name: Lint with flake8
36 |       run: |
37 |         # stop the build if there are Python syntax errors or undefined names
38 |         flake8 . --ignore=E501,W503
39 |     - name: Lint with isort
40 |       run: |
41 |         # stop build if any isort errors spotted
42 |         isort .
43 |     # - name: Test with pytest
44 |     #   run: |
45 |     #     pytest tests/ --verbose
```

tests/src/__init__.py
```
```

src/extract/__init__.py
```
```

src/extract/filtered_data.py
```
1 | import os
2 | import re
3 | import sys
4 | 
5 | import pandas as pd
6 | from dotenv import load_dotenv
7 | from loguru import logger
8 | from pydantic import BaseModel
9 | 
10 | load_dotenv()
11 | sys.path.append(os.getenv("ROOT_DIR"))
12 | 
13 | from src.utils.data_models import TableParsers  # noqa: E402
14 | from src.utils.standardize_table import standardize_table  # noqa: E402
15 | from src.utils.units import get_units_raw_input, infer_units_for_rows  # noqa: E402
16 | 
17 | if not sys.warnoptions:
18 |     import warnings
19 | 
20 |     warnings.simplefilter("ignore")
21 | 
22 | 
23 | class Filter(BaseModel):
24 |     # Regex to match 'Scope 1', 'Scope 2', and 'Scope 3'
25 |     regex_scope1: str = r"Scope\s1"
26 |     regex_scope2: str = r"Scope\s2"
27 |     regex_scope3: str = r"Scope\s3"
28 | 
29 |     # Regex to exclude rows with words like 'excluded' or 'avoided'
30 |     regex_exclude: str = (
31 |         r"(excluded|Excluded|avoided|Avoided|aim|Aim|goal|Goal|target|Target|forecast|Forecast|estimate|Estimate|projection|Projection|expectation|Expectation)"
32 |     )
33 | 
34 |     # Regex to match columns with various date formats
35 |     regex_date: str = r"(\bFY\d{2}\b|\b20\d{2}\b|\b[Ff]iscal\s[Yy]ear\b)"
36 | 
37 |     directory_path: str
38 |     parser: TableParsers
39 | 
40 |     filtered_df: pd.DataFrame = None
41 | 
42 |     class Config:
43 |         arbitrary_types_allowed = True
44 | 
45 |     def _load_dfs(self):
46 |         dfs = []
47 |         for filename in os.listdir(
48 |             os.path.join(self.directory_path, self.parser.value)
49 |         ):
50 |             if filename.endswith(".csv"):
51 |                 file_path = os.path.join(
52 |                     self.directory_path, self.parser.value, filename
53 |                 )
54 |                 df = pd.read_csv(file_path)
55 |                 dfs.append(df)
56 |         return dfs
57 | 
58 |     def extract_filtered_df(self):
59 |         docling_tables = self._load_dfs()
60 |         dfs = self._append_units_column(docling_tables)
61 |         filtered_dfs = self._filter_data_v2(dfs)
62 |         # dfs_to_concat = [df for df in filtered_dfs if df is not None]
63 |         # filtered_dfs = self._filter_for_scope(dfs)
64 |         # concatenated_df = self._filter_for_figures(filtered_dfs)
65 |         inferred_df = self._infer_units(pd.concat(filtered_dfs, ignore_index=True))
66 |         final_df = self._standardise_df(inferred_df)
67 | 
68 |         self.filtered_df = final_df
69 | 
70 |     def _append_units_column(self, docling_tables: list[pd.DataFrame]):
71 |         dfs = []
72 |         for df in docling_tables:
73 |             dfs.append(get_units_raw_input(df))
74 |         return dfs
75 | 
76 |     def _filter_data_v2(self, dfs: list[pd.DataFrame]):
77 |         scope_data = []
78 |         for idx, df in enumerate(dfs):
79 |             try:
80 |                 # Checks if scope 1 exists in table
81 |                 contains_scope1 = df.apply(
82 |                     lambda row: row.str.contains(
83 |                         self.regex_scope1, regex=True, na=False
84 |                     ).any(),
85 |                     axis=1,
86 |                 ).any()
87 |                 # Checks if scope 2 exists in table
88 |                 contains_scope2 = df.apply(
89 |                     lambda row: row.str.contains(
90 |                         self.regex_scope3, regex=True, na=False
91 |                     ).any(),
92 |                     axis=1,
93 |                 ).any()
94 | 
95 |                 if not (contains_scope1 and contains_scope2):
96 |                     print(
97 |                         f"Skipping file {idx} - does not contain both Scope 1 and Scope 2."
98 |                     )
99 |                     continue
100 | 
101 |                 # **Step 2: Remove rows where both 'Scope 1' and 'Scope 3' appear in the same row**
102 |                 scope1_and_scope3 = df.apply(
103 |                     lambda row: row.str.contains(
104 |                         self.regex_scope1, regex=True, na=False
105 |                     ).any()
106 |                     and row.str.contains(self.regex_scope3, regex=True, na=False).any(),
107 |                     axis=1,
108 |                 )
109 |                 df = df[~scope1_and_scope3]  # Remove those rows
110 | 
111 |                 # Checks if scope 3 exists in table
112 |                 contains_scope3 = df.apply(
113 |                     lambda row: row.str.contains(
114 |                         self.regex_scope3, regex=True, na=False
115 |                     ).any(),
116 |                     axis=1,
117 |                 ).any()
118 | 
119 |                 # Check if the table has a date column in the header
120 |                 date_columns = [
121 |                     col for col in df.columns if re.search(self.regex_date, str(col))
122 |                 ]
123 |                 if not date_columns:
124 |                     print(
125 |                         f"Skipping file {idx} as it has no date-related columns in the header."
126 |                     )
127 |                     continue
128 | 
129 |                 # Remove rows that contain excluded words
130 |                 df = df[
131 |                     ~df.astype(str).apply(
132 |                         lambda row: row.str.contains(
133 |                             self.regex_exclude, regex=True, na=False
134 |                         ).any(),
135 |                         axis=1,
136 |                     )
137 |                 ]
138 | 
139 |                 # Convert all columns to strings to avoid dtype issues
140 |                 df = df.astype(str)
141 | 
142 |                 if contains_scope3:
143 |                     # Find the index where 'Scope 3' appears and remove it and all rows below
144 |                     scope3_index = df.apply(
145 |                         lambda row: row.str.contains(
146 |                             self.regex_scope3, regex=True, na=False
147 |                         ).any(),
148 |                         axis=1,
149 |                     )
150 |                     if contains_scope3 and scope3_index.any():
151 |                         first_scope3_idx = scope3_index[scope3_index].index[
152 |                             0
153 |                         ]  # First occurrence
154 |                         df = df.loc[: first_scope3_idx - 1]  # Keep only rows above it
155 | 
156 |                 if contains_scope1:
157 |                     # Find the index where 'Scope 1' appears and remove all rows above it (excluding date rows)
158 |                     scope1_index = df.apply(
159 |                         lambda row: row.str.contains(
160 |                             self.regex_scope1, regex=True, na=False
161 |                         ).any(),
162 |                         axis=1,
163 |                     )
164 |                     if contains_scope1 and scope1_index.any():
165 |                         first_scope1_idx = scope1_index[scope1_index].index[
166 |                             0
167 |                         ]  # First occurrence
168 |                         df = df.loc[first_scope1_idx:]  # Keep 'Scope 1' row and below
169 | 
170 |                 # Store processed data
171 |                 scope_data.append(df)
172 | 
173 |             except Exception as e:
174 |                 logger.warning(f"Error processing df {idx}: {e}")
175 |                 continue
176 |         return scope_data
177 | 
178 |     def _filter_for_scope(self, dfs: list[pd.DataFrame]):
179 |         filtered_dfs = []
180 |         for df in dfs:
181 |             # Check if the table has a date column in the header
182 |             date_columns = [
183 |                 col for col in df.columns if re.search(self.regex_date, str(col))
184 |             ]
185 |             if not date_columns:
186 |                 continue  # Skip files without date columns
187 | 
188 |             filtered_df = df[
189 |                 df.apply(
190 |                     lambda row: row.astype(str)
191 |                     .str.contains(self.regex_scope, regex=True)
192 |                     .any(),
193 |                     axis=1,
194 |                 )
195 |             ]
196 |             filtered_df = filtered_df[
197 |                 ~filtered_df.apply(
198 |                     lambda row: row.astype(str)
199 |                     .str.contains(self.regex_exclude, regex=True)
200 |                     .any(),
201 |                     axis=1,
202 |                 )
203 |             ]
204 |             filtered_dfs.append(filtered_df)
205 |         return filtered_dfs
206 | 
207 |     def _filter_for_figures(self, dfs: list[pd.DataFrame]):
208 |         concatenated_df = pd.concat(dfs)
209 | 
210 |         # Identify the last column containing date-like information
211 |         date_columns = [
212 |             col
213 |             for col in concatenated_df.columns
214 |             if re.search(self.regex_date, str(col))
215 |         ]
216 | 
217 |         if date_columns:
218 |             # Find the index of the last date column
219 |             last_date_col_index = concatenated_df.columns.get_loc(date_columns[-1])
220 |             # Keep only columns up to and including the last date column
221 |             combined_scope_data = concatenated_df.iloc[:, : last_date_col_index + 1]
222 |             # add units column
223 |             combined_scope_data["Units"] = concatenated_df["Units"]
224 | 
225 |         # Drop the first column if necessary
226 |         if not combined_scope_data.empty and len(combined_scope_data.columns) > 0:
227 |             if combined_scope_data.columns[0] == "Unnamed: 0":
228 |                 combined_scope_data = combined_scope_data.iloc[:, 1:]
229 | 
230 |         # Drop empty columns
231 |         combined_scope_data = combined_scope_data.dropna(axis=1, how="all")
232 |         # Drop empty rows
233 |         combined_scope_data = combined_scope_data.dropna(how="all")
234 |         return combined_scope_data
235 | 
236 |     def _infer_units(self, df: pd.DataFrame):
237 |         inferred_df = infer_units_for_rows(df)
238 |         return inferred_df
239 | 
240 |     def _standardise_df(self, df: pd.DataFrame):
241 |         standard = standardize_table(df)
242 |         return standard
243 | 
244 | 
245 | if __name__ == "__main__":
246 |     ROOT_DIR = os.getenv("ROOT_OUTPUT_PATH")
247 |     filter_obj = Filter(
248 |         directory_path=os.path.join(ROOT_DIR, "META_PLATFORMS_INC-CLASS_A"),
249 |         parser=TableParsers.DOCLING,
250 |     )
251 |     filter_obj.extract_filtered_df()
252 | 
253 |     filter_obj.filtered_df.to_csv(os.path.join(ROOT_DIR, "testing_meta.csv"))
```

src/extract/llama.py
```
1 | """
2 | Scope 1 and 2 (location and market based) Emissions Extractor (llama)
3 | """
4 | 
5 | import json
6 | import os
7 | import re
8 | import sys
9 | from datetime import datetime
10 | 
11 | import pandas as pd
12 | from dotenv import load_dotenv
13 | from llama_parse import LlamaParse
14 | from loguru import logger
15 | from pydantic import BaseModel
16 | 
17 | # Load environment variables from .env file
18 | load_dotenv()
19 | sys.path.append(f"{os.getenv('ROOT_DIR')}")
20 | LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")
21 | 
22 | 
23 | class LlamaExtractor(BaseModel):
24 |     api_key: str = LLAMA_API_KEY
25 | 
26 |     company_name: str
27 |     filtered_pdf_path: str
28 |     output_path: str
29 | 
30 |     def process_company(self):
31 |         # Main entry point: downloads PDF, identifies relevant pages, parses them, saves raw output, updates CSV.
32 |         logger.info(f"Processing company: {self.company_name}")
33 | 
34 |         emissions_data = self.extract_emissions_data(
35 |             self.filtered_pdf_path, self.company_name
36 |         )
37 |         if not emissions_data:
38 |             logger.warning(f"Parsing returned no data for {self.company_name}")
39 |             return
40 | 
41 |         output_path = f"{self.output_path}/esg_data.csv"
42 |         logger.info("Writing to CSV...")
43 |         # 5) Update CSV with extracted data
44 |         df = self.update_csv(self.company_name, emissions_data, output_path)
45 |         return df
46 | 
47 |     # Actually runs the LlamaParse logic on the relevant pages,
48 |     # and merges JSON blocks to find the best data
49 |     def extract_emissions_data(
50 |         self, pdf_file: str, company_name: str
51 |     ):  # -> tuple[dict | None, list]:
52 | 
53 |         try:
54 |             parser = LlamaParse(
55 |                 api_key=self.api_key,
56 |                 result_type="markdown",
57 |                 verbose=False,
58 |                 language="en",
59 |                 num_workers=4,
60 |                 table_extraction_mode="full",
61 |                 # target_pages=page_indices_str,
62 |                 parsing_instruction="""
63 |                 This is a company sustainability report. Extract Scope 1 and Scope 2 emissions data for all available years with units.
64 |                 For Scope 2, note if it's "market-based" or "location-based."
65 |                 If no data is available for a category, use null.
66 |                 Return a single JSON object:
67 |                 {
68 |                   "scope1": {"year": [value, unit]},
69 |                   "scope2_market": {"year": [value, unit]},
70 |                   "scope2_location": {"year": [value, unit]}
71 |                 }
72 |                 """,
73 |                 is_formatting_instruction=True,
74 |             )
75 | 
76 |             documents = parser.load_data(
77 |                 pdf_file,
78 |                 extra_info={
79 |                     "file_name": f"{company_name}.pdf",
80 |                     "processed_date": datetime.now().isoformat(),
81 |                 },
82 |             )
83 | 
84 |             final_data = self._combine_document_data(documents)
85 |             return final_data
86 | 
87 |         except Exception as exc:
88 |             logger.error(f"extract_emissions_data error for {company_name}: {exc}")
89 |             return None, []
90 | 
91 |     # Walks through each LlamaParse "document" output,
92 |     # looking for JSON code blocks and scoring them
93 |     def _combine_document_data(self, documents: list) -> dict:
94 |         best_data = None
95 |         max_points = 0
96 |         code_fence_pattern = re.compile(
97 |             r"```json\s*(.*?)```", re.DOTALL | re.IGNORECASE
98 |         )
99 |         year_pattern = re.compile(
100 |             r"^(?:FY)?\d{2,4}$"
101 |         )  # Matches FY20, 20, 2020, 1980, etc.
102 | 
103 |         for doc in documents:
104 |             content = doc.get_content()
105 |             if not content:
106 |                 continue
107 | 
108 |             blocks = code_fence_pattern.findall(content)
109 |             for block in blocks:
110 |                 try:
111 |                     data = json.loads(block.strip())
112 |                 except Exception as exc:
113 |                     logger.error(f"Failed to parse JSON block: {exc}")
114 |                     continue
115 | 
116 |                 # Skip if any keys contain non-year data
117 |                 is_year_based = True
118 |                 for scope_key in ["scope1", "scope2_market", "scope2_location"]:
119 |                     scope_dict = data.get(scope_key, {})
120 |                     if isinstance(scope_dict, dict):
121 |                         for year in scope_dict.keys():
122 |                             if not year_pattern.match(str(year)):
123 |                                 is_year_based = False
124 |                                 break
125 |                     if not is_year_based:
126 |                         break
127 | 
128 |                 if not is_year_based:
129 |                     continue
130 | 
131 |                 # Score the data by counting entries with valid numeric value + unit pairs
132 |                 current_points = 0
133 |                 for scope_key in ["scope1", "scope2_market", "scope2_location"]:
134 |                     scope_dict = data.get(scope_key, {})
135 |                     if isinstance(scope_dict, dict):
136 |                         for year_data in scope_dict.values():
137 |                             if (
138 |                                 isinstance(year_data, list)
139 |                                 and len(year_data) == 2
140 |                                 and year_data[0] is not None
141 |                                 and year_data[1] is not None
142 |                             ):
143 |                                 current_points += 1
144 | 
145 |                 if current_points > max_points:
146 |                     best_data = data
147 |                     max_points = current_points
148 |                     logger.debug(f"New best data found with {current_points} points")
149 | 
150 |         if not best_data:
151 |             return {"scope1": {}, "scope2_market": {}, "scope2_location": {}}
152 |         return best_data
153 | 
154 |     # Appends emissions data (company, year, scope1_value, scope1_unit, scope2_location_value, scope2_location_unit, scope2_market_value, scope2_market_unit) to CSV
155 |     def update_csv(self, company_name: str, emissions_data: dict, csv_path: str):
156 |         try:
157 |             s1_dict = emissions_data.get("scope1", {})
158 |             s2m_dict = emissions_data.get("scope2_market", {})
159 |             s2l_dict = emissions_data.get("scope2_location", {}) or {}
160 | 
161 |             standard_df = pd.DataFrame()
162 |             standard_df["Metric"] = [
163 |                 "Scope 1",
164 |                 "Scope 2 (market-based)",
165 |                 "Scope 2 (location-based)",
166 |             ]
167 |             # Gather all years
168 |             all_years = (
169 |                 set(s1_dict.keys()) | set(s2m_dict.keys()) | set(s2l_dict.keys())
170 |             )
171 |             logger.info(all_years)
172 |             # Crete empty dataframe with columns metric, all years units
173 |             for year in sorted(all_years):
174 |                 s1 = s1_dict.get(year, [None, None])
175 |                 s2m = s2m_dict.get(year, [None, None])
176 |                 s2l = s2l_dict.get(year, [None, None])
177 | 
178 |                 # Ensure each is [val, unit]
179 |                 if not isinstance(s1, list) or len(s1) != 2:
180 |                     s1 = [None, None]
181 |                 if not isinstance(s2m, list) or len(s2m) != 2:
182 |                     s2m = [None, None]
183 |                 if not isinstance(s2l, list) or len(s2l) != 2:
184 |                     s2l = [None, None]
185 | 
186 |                 standard_df[year] = [s1[0], s2m[0], s2l[0]]
187 | 
188 |             try:
189 |                 standard_df["Units"] = [
190 |                     (s1_dict.get(max(all_years)))[1],
191 |                     s2m_dict.get(max(all_years))[1],
192 |                     s2l_dict.get(max(all_years))[1],
193 |                 ]
194 |             except Exception:
195 |                 if s1_dict.get(max(all_years))[1] is not None:
196 |                     standard_df["Units"] = s1_dict.get(max(all_years))[1]
197 |                 else:
198 |                     standard_df["Units"] = None
199 |             standard_df.to_csv(csv_path, index=False)
200 | 
201 |             logger.info(f"Appended new results to {csv_path}")
202 | 
203 |             return standard_df
204 |         except Exception:
205 |             logger.info("Error parsing with LlamaParse. Returning empty dataframe.")
206 |             return pd.DataFrame()
207 | 
208 | 
209 | # Main script entry point
210 | if __name__ == "__main__":
211 |     if not LLAMA_API_KEY:
212 |         raise ValueError("Missing LLAMA_API_KEY in environment variables.")
213 | 
214 |     company_arg = "META"
215 |     pdf_url_arg = "https://sustainability.fb.com/wp-content/uploads/2023/07/Meta-2023-Sustainability-Report-1.pdf"
216 | 
217 |     extractor = LlamaExtractor(LLAMA_API_KEY)
218 |     extractor.process_company(company_arg, pdf_url_arg)
```

src/extract/news.py
```
1 | """
2 | # TODO (iman / esther)
3 | - use yfinance OR serpapi to get latest news for company (use name or ISIN)
4 | """
```

src/extract/pdf.py
```
1 | """
2 | Methods for parsing full pdf documents
3 | 
4 | NOTE: NOT TESTED YET!
5 | DOCUMENTATION: https://docs.cloud.llamaindex.ai/llamaparse/getting_started/python
6 | """
7 | 
8 | import os
9 | import sys
10 | 
11 | from dotenv import load_dotenv
12 | from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
13 | from llama_parse import LlamaParse
14 | from loguru import logger
15 | 
16 | load_dotenv()
17 | 
18 | sys.path.append(f"{os.getenv('ROOT_DIR')}")
19 | 
20 | from src.utils.data_models import PDFParsers  # noqa: E402
21 | 
22 | 
23 | class PDFAgent:
24 | 
25 |     def __init__(self, file_path: str, parser: PDFParsers = PDFParsers.LLAMA_PARSE):
26 |         self.file_path = file_path
27 |         self.parser = parser.value
28 |         self.llama_api_key = os.getenv("LLAMA_API_KEY")  # get from .env
29 |         self.parsed_pdf = None
30 | 
31 |     def parse(self):
32 |         if self.parser == PDFParsers.LLAMA_PARSE.value:
33 |             parsed_pdf = self._parse_with_llama()
34 |             self.parsed_pdf = parsed_pdf
35 |             return parsed_pdf
36 |         else:
37 |             logger.warning(f"Invalid parser specified: {self.parser}. Returning None.")
38 |             return None
39 | 
40 |     def query(self, query: str):
41 |         if self.parser == PDFParsers.LLAMA_PARSE.value:
42 |             response = self._query_with_llama(query)
43 |             return response
44 |         else:
45 |             logger.warning(f"Invalid parser specified: {self.parser}. Returning None.")
46 |             return None
47 | 
48 |     def _parse_with_llama(self) -> str | None:
49 |         try:
50 |             # set up parser
51 |             parser = LlamaParse(
52 |                 api_key=self.api_key,
53 |                 language="en",
54 |                 result_type="markdown",
55 |             )
56 | 
57 |             # use SimpleDirectoryReader to parse file
58 |             file_extractor = {".pdf": parser}
59 |             documents = SimpleDirectoryReader(
60 |                 input_files=[self.file_path], file_extractor=file_extractor
61 |             ).load_data()
62 | 
63 |             parsed_content = "\n\n---\n\n".join(
64 |                 [doc.get_content() for doc in documents]
65 |             )
66 |             return parsed_content
67 | 
68 |         except Exception as exc:
69 |             logger.error(
70 |                 f"Unable to parse document with Llama - {self.file_path}: {exc}"
71 |             )
72 |             return None
73 | 
74 |     def _query_with_llama(self, query: str):
75 |         parsed_pdf = self.parsed_pdf if self.parsed_pdf is not None else self.parse()
76 |         if parsed_pdf is not None:
77 |             index = VectorStoreIndex.from_documents(parsed_pdf)
78 |             query_engine = index.as_query_engine()
79 |             response = query_engine.query(query)
80 |             return response
81 |         else:
82 |             return f"Unable to parse file {self.file_path}. Try again later!"
```

src/extract/tables.py
```
1 | """
2 | Methods for extracting emissions tables from ESG report using PyPDF and Docling
3 | """
4 | 
5 | import os
6 | import re
7 | import sys
8 | from datetime import datetime
9 | from pathlib import Path
10 | from typing import List, Union
11 | 
12 | import pandas as pd
13 | import tabula
14 | from docling.document_converter import DocumentConverter
15 | from dotenv import load_dotenv
16 | from loguru import logger
17 | from PyPDF2 import PdfReader, PdfWriter
18 | 
19 | from src.find.company_profile import CompanyProfile
20 | 
21 | load_dotenv()
22 | 
23 | sys.path.append(f"{os.getenv('ROOT_DIR')}")
24 | 
25 | from src.utils.data_models import Company, RegexPatterns, TableParsers  # noqa: E402
26 | 
27 | 
28 | class TableExtractor:
29 |     """
30 |     Methods for extracting tables from PDF using docling or tabula
31 |     """
32 | 
33 |     def __init__(
34 |         self,
35 |         company: CompanyProfile,
36 |         file_path: str,
37 |         parser: Union[TableParsers, List[TableParsers]],
38 |         output_path: str,
39 |     ):
40 |         self.company = company
41 |         self.file_path = file_path
42 |         self.file_name = os.path.basename(file_path).replace(".pdf", "")
43 |         self.output_dir = output_path
44 |         self.parser = parser.value
45 | 
46 |         # create output dir
47 |         os.makedirs(self.output_dir, exist_ok=True)
48 | 
49 |     def extract(self):
50 |         """
51 |         1. Returns list of extracted tables as pandas dataframes
52 |         2. Saves tables to cache
53 |         """
54 | 
55 |         if isinstance(self.parser, List):
56 |             all_tables = []
57 |             for parser in self.parser:
58 |                 logger.info(f"Extracting data for {parser.value}")
59 |                 logger.info(datetime.now())
60 |                 # create output dir (if it doesn't exist)
61 |                 output_dir_parser = Path(f"{self.output_dir}/{parser}")
62 |                 output_dir_parser.mkdir(parents=True, exist_ok=True)
63 |                 # extract and save tables
64 |                 tables = self._extract(parser)
65 |                 self._save_tables(tables, output_dir_parser)
66 |                 all_tables.append(tables)
67 |         else:
68 |             # extract tables
69 |             all_tables = self._extract(self.parser)
70 |             output_dir_parser = Path(f"{self.output_dir}/{self.parser}")
71 |             output_dir_parser.mkdir(parents=True, exist_ok=True)
72 |             # save tables
73 |             self._save_tables(all_tables, output_dir_parser)
74 | 
75 |         return all_tables
76 | 
77 |     def _extract(self, parser):
78 |         """
79 |         Method for extracting tables for specified parser.
80 | 
81 |         Returns
82 |             emissions_tables (list[pd.DataFrame]): list of extracted tables
83 |         """
84 |         # Identify relevant pages
85 |         pdf = self._read_pdf()
86 |         pages, indeces = self._filter_pdf_pages(pdf)
87 |         if not pages:
88 |             logger.error(
89 |                 f"No relevant pages found for {self.company.name}. Returning None."
90 |             )
91 |             return None
92 | 
93 |         # parse document
94 |         if parser == TableParsers.DOCLING.value:
95 |             # write filtered pdf to cache
96 |             filtered_file_path = f"{self.output_dir}/{self.file_name}-filtered.pdf"
97 |             self._write_pages_to_pdf(pages, filtered_file_path)
98 |             # extract from filtered pdf
99 |             emissions_tables = self._extract_with_docling(filtered_file_path)
100 |             return emissions_tables
101 |         elif parser == TableParsers.TABULA.value:
102 |             emissions_tables = self._extract_with_tabula(indeces)
103 |             return emissions_tables
104 |         else:
105 |             logger.error(f"Invalid parsesr {self.parser} specified.")
106 |             return None
107 | 
108 |     def _extract_with_docling(self, file_path):
109 |         """
110 |         Extract tables using docling.
111 |         """
112 |         # parse document using docling
113 |         doc_converter = DocumentConverter()
114 |         conv_res = doc_converter.convert(file_path)
115 |         tables = [table.export_to_dataframe() for table in conv_res.document.tables]
116 |         return tables
117 | 
118 |     def _extract_with_tabula(self, page_indeces):
119 |         """
120 |         Extract tables using tabula.
121 |         """
122 |         tables = tabula.read_pdf(
123 |             self.file_path, pages=page_indeces, multiple_tables=True
124 |         )
125 |         return tables
126 | 
127 |     def _read_pdf(self):
128 |         """
129 |         Read PDF using PyPDF2.
130 | 
131 |         Returns
132 |             pages (list[PageObject]): list of page objects returned by PyPDF2
133 |         """
134 |         reader = PdfReader(self.file_path, strict=False)
135 |         return reader.pages
136 | 
137 |     def _write_pages_to_pdf(self, pages, path):
138 |         """
139 |         Write pages to pdf file.
140 | 
141 |         Args
142 |             pages (list[PageObject]): list of page objects to write to file
143 |             path (str): output file path to write pages to
144 |         """
145 |         writer = PdfWriter()
146 |         for page in pages:
147 |             writer.add_page(page)
148 |         with open(path, "wb") as file:
149 |             writer.write(file)
150 | 
151 |     def _save_tables(self, tables: Union[List[pd.DataFrame], None], output_dir):
152 |         """
153 |         Save tables to output dir
154 | 
155 |         Args
156 |             tables (list[pd.DataFrame]): list of tables to write to folder
157 |         """
158 |         if tables is None:
159 |             logger.error(f"No tables found for {self.company.isin}")
160 |             return None
161 | 
162 |         for idx, table in enumerate(tables):
163 |             # Save the table as csv
164 |             element_csv_filepath = os.path.join(
165 |                 output_dir, f"{self.file_name}-table-{idx + 1}.csv"
166 |             )
167 |             table.to_csv(element_csv_filepath)
168 | 
169 |     def _filter_pdf_pages(self, pdf_pages):
170 |         """
171 |         Locate pages that include relevant information.
172 | 
173 |         Args
174 |             pdf_pages (List[PageObject]): list of pages to filter
175 | 
176 |         Return
177 |             pages (List[PageObject]): list of pages that could include relevant information
178 |             indexed (List[int]): index of each page returned in pages list
179 |         """
180 |         pages = []
181 |         indeces = []
182 |         for idx, page in enumerate(pdf_pages):
183 |             try:
184 |                 page_text = page.extract_text().lower()
185 |                 if (
186 |                     re.search(RegexPatterns.SCOPE1.value, page_text, re.IGNORECASE)
187 |                     and re.search(RegexPatterns.SCOPE2.value, page_text, re.IGNORECASE)
188 |                     and any(
189 |                         [
190 |                             re.search(
191 |                                 RegexPatterns.YEAR_1.value, page_text, re.IGNORECASE
192 |                             ),
193 |                             re.search(
194 |                                 RegexPatterns.YEAR_2.value, page_text, re.IGNORECASE
195 |                             ),
196 |                         ]
197 |                     )
198 |                     and all(
199 |                         [
200 |                             re.search(
201 |                                 RegexPatterns.UNITS_1.value, page_text, re.IGNORECASE
202 |                             ),
203 |                             re.search(
204 |                                 RegexPatterns.UNITS_2.value, page_text, re.IGNORECASE
205 |                             ),
206 |                         ]
207 |                     )
208 |                 ):
209 |                     pages.append(page)
210 |                     indeces.append(idx)
211 |                     logger.debug(f"Page {idx} is relevant.")
212 |             except Exception as e:
213 |                 logger.warning(f"Unable to process page {idx}: {e}")
214 |         return pages, indeces
215 | 
216 | 
217 | if __name__ == "__main__":
218 |     company = Company(isin="US5949181045")
219 |     file_path = "data/cache/US5949181045/RW1lmju.pdf"
220 | 
221 |     extractor = TableExtractor(company, file_path, TableParsers.TABULA)
222 |     tables = extractor.extract()
223 |     logger.info(f"Emissions tables for {company.identifier} extracted!")
```

src/find/__init__.py
```
```

src/find/company_profile.py
```
1 | import os
2 | import sys
3 | import time
4 | 
5 | import requests
6 | from dotenv import load_dotenv
7 | from loguru import logger
8 | 
9 | load_dotenv()
10 | sys.path.append(os.getenv("ROOT_DIR"))
11 | 
12 | ROOT_DIR = os.getenv("ROOT_DIR")
13 | ROOT_OUTPUT_PATH = os.getenv("ROOT_OUTPUT_PATH")
14 | # OPENFIGI variables
15 | OPENFIGI_API_KEY = os.getenv("OPENFIGI_API_KEY")
16 | OPENFIGI_URL = os.getenv("OPENFIGI_URL")
17 | 
18 | 
19 | class CompanyProfile:
20 | 
21 |     def __init__(
22 |         self,
23 |         identifier,
24 |         idType,
25 |     ):  # idType is TICKER, NAME or ISIN
26 |         # initialise default attributes
27 |         self.identifier = identifier
28 |         self.idType = idType.lower()
29 |         self.isin = (
30 |             identifier
31 |             if self.idType.lower() == "isin" and self.is_valid_isin(identifier)
32 |             else None
33 |         )
34 | 
35 |         self.name = identifier if self.idType.lower() == "name" else None
36 |         self.ticker = identifier if self.idType.lower() == "ticker" else None
37 |         self.description = None
38 | 
39 |         # invoke company details function to retrieve missing attributes
40 |         self._complete_company_profile()
41 |         self.output_path = os.path.join(
42 |             ROOT_OUTPUT_PATH, self.name.replace(" ", "_").upper()
43 |         )
44 |         logger.debug(f"Company Identifier: {self.identifier}")
45 | 
46 |     @staticmethod
47 |     def is_valid_isin(ISIN):
48 |         """
49 |         Function to check if the input is a valid ISIN.
50 |             2 letters followed by any combination of letters or digits
51 |             for the next 10 characters (12 characters in total)
52 | 
53 |         Params:
54 |             ISIN (str): The input string to validate
55 | 
56 |         Returns:
57 |             bool: True if the ISIN is valid, False otherwise
58 |         """
59 |         if (
60 |             len(ISIN) == 12
61 |             and ISIN[:2].isalpha()
62 |             and all(c.isalnum() for c in ISIN[2:])
63 |         ):
64 |             return True
65 |         return False
66 | 
67 |     def get_profile_from_identifier(self, identifier, idType):
68 |         """
69 |         Function to fetch the ticker symbol from OpenFIGI API using the ISIN code.
70 |         """
71 |         # Send a POST request to the OpenFIGI API
72 |         openfigi_response = None
73 | 
74 |         if idType == "isin":
75 |             openfigi_response = self._openfigi_post_request(
76 |                 [{"idType": "ID_ISIN", "idValue": identifier}]
77 |             )
78 |         elif idType == "ticker":
79 |             openfigi_response = self._openfigi_post_request(
80 |                 [{"idType": "TICKER", "idValue": identifier}]
81 |             )
82 | 
83 |         if openfigi_response is not None:
84 |             try:
85 |                 comp_dict = dict(openfigi_response[0]["data"][0])
86 |                 return comp_dict
87 |             except Exception as e:
88 |                 logger.error(
89 |                     f"Error fetching details for identifier{identifier}: {e}. Returning None."
90 |                 )
91 |                 return None
92 | 
93 |     def _complete_company_profile(self) -> None:
94 |         """
95 |         Function to get corresponding details if ISIN provided.
96 |         """
97 |         if self.name is not None:  # for names keep user input
98 |             return
99 |             # Check if identifier is an ISIN
100 |         if self.identifier is not None:
101 | 
102 |             profile = self.get_profile_from_identifier(self.identifier, self.idType)
103 |             if profile is not None:
104 |                 self.name = profile.get("name")
105 |                 self.ticker = profile.get("ticker")
106 |                 self.description = profile.get("securityDescription")
107 |             else:
108 |                 logger.warning(
109 |                     f"ISIN {self.isin} not found. Unable to fetch the corresponding details."
110 |                 )
111 |                 sys.exit()
112 | 
113 |     @staticmethod
114 |     def _openfigi_post_request(data):
115 |         """
116 |         Function to send a POST request to the OpenFIGI API with the given data.
117 | 
118 |         Args:
119 |             data (list): List of dictionaries containing the data to send in the request
120 | 
121 |         Returns:
122 |             dict: Dictionary containing the response from the OpenFIGI API
123 |         """
124 |         headers = {
125 |             "Content-Type": "application/json",
126 |             "X-OPENFIGI-APIKEY": OPENFIGI_API_KEY,
127 |         }
128 |         try:
129 |             # Make the POST request to OpenFIGI API
130 |             response = requests.post(OPENFIGI_URL, json=data, headers=headers)
131 | 
132 |             # Handle rate-limiting with retries
133 |             while response.status_code == 429:
134 |                 logger.warning(
135 |                     "Rate limit reached for OPENFIGI, retrying in 3 seconds..."
136 |                 )
137 |                 time.sleep(3)
138 |                 response = requests.post(OPENFIGI_URL, json=data, headers=headers)
139 | 
140 |             # Return the JSON response
141 |             return response.json()
142 |         except Exception as e:
143 |             logger.error(f"Error sending POST request to OpenFIGI API: {e}")
144 |             return None
145 | 
146 | 
147 | # Main script to fetch company information
148 | if __name__ == "__main__":
149 |     # Ask the user for input
150 |     id_type = input("Enter idType (TICKER, NAME, ISIN): ").strip()
151 |     identifier = input("Enter ISIN, Ticker, or Company Name: ").strip()
152 |     company = CompanyProfile(identifier, id_type)
153 |     logger.info(f"Company Name: {company.name}, Ticker: {company.ticker}")
```

src/find/esg_reports.py
```
1 | import datetime as dt
2 | import json
3 | import os
4 | import re
5 | import sys
6 | from typing import List
7 | 
8 | import requests
9 | from dotenv import load_dotenv
10 | from loguru import logger
11 | from pydantic import BaseModel
12 | 
13 | from src.utils.data_models import SearchKeyWords
14 | 
15 | load_dotenv()
16 | sys.path.append(os.getenv("ROOT_DIR"))
17 | 
18 | ROOT_DIR = os.getenv("ROOT_DIR")
19 | ROOT_OUTPUT_PATH = os.getenv("ROOT_OUTPUT_PATH")
20 | API_KEY = os.getenv("GOOGLE_API_KEY")
21 | SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")
22 | 
23 | if not any([API_KEY, SEARCH_ENGINE_ID]):
24 |     raise ValueError(
25 |         "Environment variables GOOGLE_API_KEY or GOOGLE_SEARCH_ENGINE_ID are not set."
26 |     )
27 | 
28 | from src.find.company_profile import CompanyProfile  # noqa: E402
29 | 
30 | 
31 | class ESGReports:
32 | 
33 |     def __init__(self, company: CompanyProfile):
34 |         self.company = company
35 |         self.urls = self._get_report_search_results()
36 | 
37 |         # set output path
38 |         try:
39 |             # set output path
40 |             self.output_path = os.path.join(
41 |                 ROOT_OUTPUT_PATH,
42 |                 str(self.company.name).upper().replace(" ", "_").replace("/", "_"),
43 |             )
44 |         except Exception:
45 |             self.output_path = os.path.join(
46 |                 ROOT_OUTPUT_PATH,
47 |                 str(self.company.name).upper().replace(" ", "_").replace("/", "_"),
48 |             )
49 |         os.makedirs(self.output_path, exist_ok=True)
50 |         # dump company profile to json
51 |         self.save_profile()
52 | 
53 |     def _get_report_search_results(self) -> dict:
54 |         """
55 |         Retrieve the top 3 URLs of the company's ESG reports using Google Custom Search.
56 |         """
57 |         # Search parameters
58 |         current_year = str(dt.datetime.now().year)
59 |         search_query = f"{self.company.name} {current_year} ESG report filetype:pdf"
60 |         url = "https://www.googleapis.com/customsearch/v1"
61 |         params = {
62 |             "q": search_query,
63 |             "key": API_KEY,
64 |             "cx": SEARCH_ENGINE_ID,
65 |         }
66 | 
67 |         # Make the search request
68 |         response = requests.get(url, params=params)
69 |         response.raise_for_status()
70 |         search_results = response.json().get("items", [])[:5]  # Get top 5 results
71 | 
72 |         if not search_results:
73 |             logger.warning(f"No ESG reports found for {self.name}")
74 |             # TODO - return response to display in UI
75 |             sys.exit()
76 | 
77 |         sorted_results = self._sort_search_reults(
78 |             self.company.name, search_results
79 |         )  # Invoke function to get proper order of keywords
80 |         esg_urls = {
81 |             index: value.get("link", "") for index, value in enumerate(sorted_results)
82 |         }
83 |         logger.debug(f"ESG report urls for {self.company.name}: {esg_urls}")
84 |         return esg_urls
85 | 
86 |     @staticmethod
87 |     def _sort_search_reults(company_name: str, search_results: List[dict]):
88 | 
89 |         for result in search_results:
90 |             result_obj = SearchResult(
91 |                 company_name=company_name,
92 |                 url=result.get("link", ""),
93 |                 title=result.get("title", ""),
94 |                 description=result.get("snippet", ""),
95 |             )
96 |             result["score"] = result_obj.score_search()
97 | 
98 |         sorted_results = sorted(
99 |             search_results,
100 |             key=lambda item: item.get("score"),
101 |             reverse=True,
102 |         )
103 | 
104 |         return sorted_results
105 | 
106 |     def save_profile(self):
107 |         """Dumps the company profile as a JSON file into the specified folder."""
108 |         if not ROOT_DIR:
109 |             raise ValueError("ROOT_DIR is not set in the .env file.")
110 |         try:
111 |             # get attributes as dictionary
112 |             data = {
113 |                 "company": self.company.__dict__,
114 |                 "esg_reports": self.urls,
115 |             }
116 | 
117 |             file_path = f"{self.output_path}/profile.json"
118 |             with open(file_path, "w") as json_file:
119 |                 json.dump(data, json_file, indent=4)
120 |             logger.info(f"Company profile JSON saved to {file_path}")
121 |         except Exception as e:
122 |             print(f"Failed to save company profile JSON: {e}")
123 | 
124 | 
125 | class SearchResult(BaseModel):
126 |     company_name: str
127 |     url: str
128 |     title: str
129 |     description: str
130 | 
131 |     def score_search(self):
132 |         stripped_name = self.company_name.split(" ")[0].lower()
133 | 
134 |         text_score = (
135 |             self.score_text(self.title.lower())
136 |             + self.score_text(self.description.lower())
137 |             + (
138 |                 -5
139 |                 if (
140 |                     stripped_name not in self.title.lower()
141 |                     and stripped_name not in self.description.lower()
142 |                     and stripped_name not in self.url.lower()
143 |                 )
144 |                 else 1
145 |             )  # strongly penalize if name is not there
146 |         )
147 |         url_score = self.score_text(self.url) + (1 if self.company_name_lookup() else 0)
148 |         year_score = self.score_year(
149 |             self.title.lower() + self.description.lower() + self.url.lower()
150 |         )
151 |         return text_score + url_score + year_score
152 | 
153 |     @staticmethod
154 |     def score_text(text: str):
155 |         count = sum(keyword.value.lower() in text.lower() for keyword in SearchKeyWords)
156 |         return count
157 | 
158 |     def company_name_lookup(self):
159 |         # get the site name from url
160 |         url_index = re.search(
161 |             r"(?:https?://)?(?:www\.)?([a-zA-Z0-9]+)", self.url
162 |         ).group()
163 |         stripped_name = self.company_name.split(" ")[0].lower()
164 |         # check if company name starts with site name
165 |         if stripped_name in url_index:
166 |             return 2
167 |         else:
168 |             return 0
169 | 
170 |     @staticmethod
171 |     def score_year(text):
172 |         current_year = dt.datetime.now().year
173 |         year_lag = current_year - 1
174 |         two_year_lag = current_year - 2
175 |         three_year_lag = current_year - 3
176 | 
177 |         # Extract all years from the text
178 |         years_in_text = [int(year) for year in re.findall(r"\b\d{4}\b", text)]
179 | 
180 |         # Check for years that are 3 years older than the current year or older
181 |         if any(year < three_year_lag for year in years_in_text):
182 |             return -2
183 | 
184 |         # Check if the text contains the current year, year lag, or two-year lag
185 |         if current_year in years_in_text:
186 |             return 2
187 |         if any(
188 |             year in {current_year, year_lag, two_year_lag} for year in years_in_text
189 |         ):
190 |             return 1
191 | 
192 |         return -1
```

src/find/filters.py
```
1 | """
2 | https://ranaroussi.github.io/yfinance/reference/yfinance.sector_industry.html
3 | https://finance.yahoo.com/research-hub/screener/sec-ind_sec-largest-equities_industrials/?start=0&count=25
4 | 
5 | TODO - (iman / balazs)
6 | - get list of companies by sectors / countries / indeces
7 | - get aggregated figures (cache monthly) for top companies in each filter type
8 | """
```

src/scripts/__init__.py
```
```

src/scripts/retrieve_company_profile.py
```
1 | import os
2 | import sys
3 | 
4 | from dotenv import load_dotenv
5 | from loguru import logger
6 | 
7 | load_dotenv()
8 | sys.path.append(os.getenv("ROOT_DIR"))
9 | 
10 | from src.find.company_profile import CompanyProfile  # noqa: E402
11 | 
12 | # temporarily hardcoding variables here
13 | # TODO - switch to retrieve from inputs to flask app
14 | ROOT_DATA_DIR = os.getenv("ROOT_DIR")
15 | COMPANY_IDENTIFIER = (
16 |     "GB00BNC5T391"  # note: src/extract/tables.py requires ISIN currently
17 | )
18 | 
19 | if __name__ == "__main__":
20 |     # get the ticker symbol and company name from ISIN
21 |     company = CompanyProfile(COMPANY_IDENTIFIER, "ISIN")
22 |     logger.info(f"Retrieved details for {company.name}")
```

src/scripts/retrieve_emissions_data.py
```
1 | import json
2 | import os
3 | import sys
4 | import time
5 | from datetime import datetime, timedelta
6 | 
7 | import pandas as pd
8 | from dotenv import load_dotenv
9 | from loguru import logger
10 | 
11 | # Load environment variables from .env file
12 | load_dotenv()
13 | # Get ROOT_DIR from the environment variables
14 | ROOT_DIR = os.getenv("ROOT_DIR")
15 | OUTPUT_DIR = os.getenv("ROOT_OUTPUT_PATH")
16 | # append path
17 | sys.path.append(f"{os.getenv('ROOT_DIR')}")
18 | 
19 | from src.extract.filtered_data import Filter  # noqa: E402
20 | from src.extract.llama import LlamaExtractor  # noqa: E402
21 | from src.extract.tables import TableExtractor  # noqa: E402
22 | from src.find.company_profile import CompanyProfile  # noqa: E402
23 | from src.find.esg_reports import ESGReports  # noqa: E402
24 | from src.utils.data import download_pdf_from_urls  # noqa: E402
25 | from src.utils.data_models import TableParsers  # noqa: E402
26 | 
27 | 
28 | def get_emissions_data(identifier, idType, parser):
29 |     company = CompanyProfile(identifier, idType)
30 | 
31 |     # check cache for data
32 |     try:
33 |         cache_dir = os.path.join(OUTPUT_DIR)
34 |         if not os.path.exists(cache_dir):
35 |             logger.error(f"Cache directory does not exist: {cache_dir}")
36 |             return None
37 | 
38 |         esg_file_path = None
39 | 
40 |         def is_recent_file(file_path, days=30):
41 |             """Checks if a file was modified within the last `days` days."""
42 |             if os.path.exists(file_path):
43 |                 file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
44 |                 return file_mtime >= (datetime.now() - timedelta(days=days))
45 |             return False
46 | 
47 |         if idType == "name":
48 |             # Get all folder names in the cache directory
49 |             folder_names = [
50 |                 folder
51 |                 for folder in os.listdir(cache_dir)
52 |                 if os.path.isdir(os.path.join(cache_dir, folder))
53 |             ]
54 | 
55 |             # Find matching folder
56 |             matching_folder = next(
57 |                 (
58 |                     folder
59 |                     for folder in folder_names
60 |                     if company.name.upper().replace(" ", "_") in folder.upper()
61 |                     or folder.upper() in company.name.upper()
62 |                 ),
63 |                 None,
64 |             )
65 | 
66 |             if matching_folder:
67 |                 folder_path = os.path.join(cache_dir, matching_folder)
68 |                 esg_file_path = os.path.join(folder_path, "esg_data.csv")
69 | 
70 |         else:
71 |             # For other idTypes, check the standard company output path
72 |             folder_path = company.output_path
73 |             esg_file_path = os.path.join(company.output_path, "esg_data.csv")
74 | 
75 |         # If the ESG file exists and is recent, load it
76 |         if esg_file_path and os.path.exists(esg_file_path):
77 |             if is_recent_file(esg_file_path):
78 |                 try:
79 |                     data = pd.read_csv(esg_file_path)
80 |                     logger.info(f"data for company: {data}")
81 |                     logger.info(
82 |                         f"Loaded ESG data from {esg_file_path} for company {company.name}"
83 |                     )
84 |                     profile_path = os.path.join(folder_path, "profile.json")
85 | 
86 |                     # get report path
87 |                     if os.path.exists(profile_path):
88 |                         with open(os.path.join(folder_path, "profile.json")) as f:
89 |                             profile = json.load(f)
90 |                         logger.info(f"Loaded profile for {company.name}")
91 |                         report = next(
92 |                             iter(profile.get("esg_reports").values())
93 |                         )  # Get first URL dynamically
94 |                         # report = list(profile.get("esg_reports").values())[0]
95 |                     else:
96 |                         esg_reports = ESGReports(company)
97 |                         report = next(iter(esg_reports.urls.values()))
98 |                         # report = list(esg_reports.urls.values())[0]
99 | 
100 |                     logger.info(f"loaded data: {data} {report}")
101 |                     return data, report
102 |                 except Exception as e:
103 |                     logger.error(f"Error reading ESG data from {esg_file_path}: {e}")
104 |             else:
105 |                 logger.warning(
106 |                     f"ESG data file {esg_file_path} is older than one month, ignoring cache."
107 |                 )
108 | 
109 |         logger.info(f"No recent cached data found for {company.name}")
110 | 
111 |         # Load fresh data
112 |         # esg_file_path = os.path.join(company.output_path, "esg_data.csv")
113 |         # if is_recent_file(esg_file_path):
114 |         #     if os.path.exists(esg_file_path):
115 |         #         try:
116 |         #             data = pd.read_csv(esg_file_path)
117 |         #             logger.info(f"Loaded ESG data for {company.name}")
118 |         #             return data
119 |         #         except Exception as e:
120 |         #             logger.error(f" {esg_file_path}: {e}")
121 | 
122 |     except Exception:
123 |         logger.warning(
124 |             "Unable to retrieve recent cached data. Retrieving emissions data from web..."
125 |         )
126 | 
127 |     esg_reports = ESGReports(company)
128 |     # Loop over urls until emissions data retrieved
129 |     for url in esg_reports.urls.values():
130 |         logger.info(f"Trying extraction with {url}")
131 |         try:
132 |             # Download pdf file
133 |             path = download_pdf_from_urls([url], esg_reports.output_path)
134 |             # get emissions data
135 |             output = TableExtractor(
136 |                 company, path, parser, esg_reports.output_path
137 |             ).extract()
138 |             if output not in [None, [], False]:
139 |                 break
140 |             else:
141 |                 # delete file before moving on to next
142 |                 for file in os.listdir(esg_reports.output_path):
143 |                     if os.path.basename(path).replace(".pdf", "") in file:
144 |                         os.remove(os.path.join(esg_reports.output_path, file))
145 |                         logger.info(f"Deleted {file}")
146 |         except Exception as e:
147 |             logger.debug(f"Unable to parse data from {url}: {e}")
148 |             # delete file before moving on to next
149 |             for file in os.listdir(esg_reports.output_path):
150 |                 if isinstance(path, str) and (
151 |                     os.path.basename(path).replace(".pdf", "") in file
152 |                 ):
153 |                     os.remove(os.path.join(esg_reports.output_path, file))
154 |                     logger.info(f"Deleted {file}")
155 |             continue
156 | 
157 |     try:
158 |         # TODO - pass tables as objects
159 |         data_filter = Filter(directory_path=esg_reports.output_path, parser=parser)
160 |         data_filter.extract_filtered_df()
161 |         data = data_filter.filtered_df
162 |         data.to_csv(os.path.join(esg_reports.output_path, "esg_data.csv"))
163 |         # get filtered pdf path
164 | 
165 |         for file in os.listdir(esg_reports.output_path):
166 |             if file.endswith("filtered.pdf"):
167 |                 pdf_path = os.path.join(esg_reports.output_path, file)
168 |             else:
169 |                 pdf_path = None
170 | 
171 |         # if any column is completely null, run llama parse instead
172 |         if any([all(data[col].isna()) for col in data.columns]) or data is None:
173 |             logger.info("Retrieving via LlamaParse...")
174 |             if pdf_path is None:
175 |                 return pd.DataFrame()
176 |             extractor = LlamaExtractor(
177 |                 company_name=company.name,
178 |                 filtered_pdf_path=pdf_path,
179 |                 output_path=esg_reports.output_path,
180 |             )
181 |             data = extractor.process_company()
182 |     except Exception as e:
183 |         logger.warning(f"Retrieveing via LlamaParse...: {e}")
184 | 
185 |         for file in os.listdir(esg_reports.output_path):
186 |             logger.info(file)
187 |             if file.endswith("filtered.pdf"):
188 |                 pdf_path = os.path.join(esg_reports.output_path, file)
189 |             else:
190 |                 pdf_path = None
191 |         if pdf_path is None:
192 |             return pd.DataFrame()
193 |         extractor = LlamaExtractor(
194 |             company_name=company.name,
195 |             filtered_pdf_path=pdf_path,
196 |             output_path=esg_reports.output_path,
197 |         )
198 |         data = extractor.process_company()
199 | 
200 |     top_report = list(esg_reports.urls.values())[0]
201 |     return data, top_report
202 | 
203 | 
204 | if __name__ == "__main__":
205 |     start = time.time()
206 | 
207 |     identifier = "US5949181045"
208 |     idType = "isin"
209 |     parser = TableParsers.DOCLING
210 |     data = get_emissions_data(identifier, idType, parser)
211 | 
212 |     end = time.time()
213 |     total = end - start
214 | 
215 |     logger.info(f"time taken: {total}")
```

src/scripts/retrieve_emissions_data_pro.py
```
1 | import os
2 | import sys
3 | 
4 | import pandas as pd
5 | from dotenv import load_dotenv
6 | from loguru import logger
7 | 
8 | # Load environment variables
9 | load_dotenv()
10 | # Get ROOT_DIR from environment variables
11 | ROOT_DIR = os.getenv("ROOT_DIR")
12 | OUTPUT_DIR = os.getenv("ROOT_OUTPUT_PATH")
13 | 
14 | 
15 | # Ensure project root is on sys.path
16 | sys.path.append(f"{os.getenv('ROOT_DIR')}")
17 | 
18 | 
19 | from src.extract.tables import TableExtractor  # noqa: E402
20 | from src.find.company_profile import CompanyProfile  # noqa: E402
21 | from src.find.esg_reports import ESGReports  # noqa: E402
22 | 
23 | # Use the LLM-based table filtering
24 | from src.utils import llm_table_data_filtering  # noqa: E402
25 | from src.utils.data import download_pdf_from_urls  # noqa: E402
26 | 
27 | 
28 | def get_emissions_data_pro(identifier, idType, parser):
29 |     """
30 |     Retrieve ESG emissions data using an LLM-based table filter.
31 |     Returns both the LLM output and path to the relevant PDF.
32 |     """
33 |     company = CompanyProfile(identifier, idType)
34 |     esg_reports = ESGReports(company)
35 | 
36 |     # Check for cached LLM data
37 |     llm_output_file = os.path.join(esg_reports.output_path, "esg_data_llm.md")
38 |     if os.path.isfile(llm_output_file):
39 |         logger.info(f"Found cached LLM data for {company.name} at {llm_output_file}")
40 |         with open(llm_output_file, "r", encoding="utf-8") as f:
41 |             llm_markdown = f.read()
42 |         # Look for PDFs but exclude ones with 'filtered' in the name
43 |         pdf_files = [
44 |             f
45 |             for f in os.listdir(esg_reports.output_path)
46 |             if f.endswith(".pdf") and "filtered" not in f.lower()
47 |         ]
48 |         pdf_path = None
49 |         if pdf_files:
50 |             pdf_path = os.path.join(esg_reports.output_path, pdf_files[0])
51 |         else:
52 |             logger.warning(
53 |                 f"No PDF found in {esg_reports.output_path} for cached data."
54 |             )
55 |         return pd.DataFrame({"LLM_Output": [llm_markdown]}), pdf_path
56 | 
57 |     logger.warning("No cached LLM data found. Retrieving emissions data from web...")
58 | 
59 |     # Attempt to download & parse ESG PDFs
60 |     successful_pdf_path = None
61 |     for url in esg_reports.urls.values():
62 |         logger.info(f"Trying extraction with {url}")
63 |         try:
64 |             local_pdf_path = download_pdf_from_urls([url], esg_reports.output_path)
65 |             output = TableExtractor(
66 |                 company, local_pdf_path, parser, esg_reports.output_path
67 |             ).extract()
68 |             if output not in [None, [], False]:
69 |                 successful_pdf_path = local_pdf_path
70 |                 break
71 |         except Exception as e:
72 |             logger.debug(f"Unable to parse data from {url}: {e}")
73 |             continue
74 | 
75 |     # Use the LLM-based filter
76 |     data = llm_table_data_filtering.filter_tables(esg_reports.output_path, parser)
77 | 
78 |     # Cache the LLM output as Markdown
79 |     if not data.empty and "LLM_Output" in data.columns:
80 |         llm_markdown = data["LLM_Output"].iloc[0]
81 |         with open(llm_output_file, "w", encoding="utf-8") as f:
82 |             f.write(llm_markdown)
83 |         logger.info(f"Cached LLM data to {llm_output_file}")
84 | 
85 |     return data, successful_pdf_path
```

src/static/style.css
```
1 | 
2 | h2 {
3 |     color: red;
4 |     text-align: center;
5 | }
```

src/templates/advanced_search.html
```
1 | <!DOCTYPE html>
2 | <html lang="en">
3 | <head>
4 |   <meta charset="UTF-8">
5 |   <meta http-equiv="X-UA-Compatible" content="IE=edge">
6 |   <meta name="viewport" content="width=device-width, initial-scale=1.0">
7 |   <title>Advanced Search</title>
8 |   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
9 |   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
10 |    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
11 |   <style>
12 |           body {
13 |           font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
14 |           background-color: #F5F5F5;
15 |           color: #333333;
16 |           margin: 0;
17 |           padding: 0;
18 |       }
19 |       table, th, td {
20 |           border: 1px solid black;
21 |      }
22 | 
23 |     .logo-header-container {
24 |        z-index: 10;
25 |        position: relative;
26 |        height: 160px;
27 |        width: 100%;
28 |        background-color: #063800;
29 |        display: flex;
30 |        align-items: center; /* Align items vertically */
31 |        justify-content: center; /* Center items horizontally */
32 |        gap: 20px; /* Add spacing between logo and text */
33 |        box-shadow: 0px 4px 15px rgba(20, 80, 20, 0.6);
34 |        text-align: center;
35 |     }
36 | 
37 | 
38 |     .logo {
39 |        max-height: 100px;
40 |        width: auto;
41 |     }
42 | 
43 | 
44 |     .div1 {
45 |        display: flex;
46 |        flex-direction: column; /* Stack heading and phrase */
47 |        align-items: center;
48 |        justify-content: center;
49 |     }
50 | 
51 | 
52 |     .catchy-phrase {
53 |        color: white;
54 |        font-size: 20px;
55 |        margin-top: 5px; /* Adjust spacing between header and phrase */
56 |     }
57 | 
58 |     .footer {
59 |           background-color: #2E8B57;
60 |           color: #FFFFFF;
61 |           text-align: center;
62 |           padding: 10px;
63 |           position: fixed;
64 |           left: 0;
65 |           bottom: 0;
66 |           width: 100%;
67 |           font-size: 0.9rem;
68 |       }
69 | 
70 |     .dropdown-container {
71 |           background-color: white;
72 |           display: flex;
73 |           padding: 10px;
74 |           gap: 30px;
75 |           align-items: center;
76 |           justify-content: center;
77 |           box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
78 |       }
79 | 
80 | 
81 |     .dropdown-container label{
82 |           color: #1C1C1C;
83 |       }
84 | 
85 | 
86 |     .dropdown-container label,
87 | 
88 |     .dropdown-container select {
89 |           margin-right: 10px;
90 |       }
91 | 
92 |     .dropdown-container select {
93 |           width: 200px;
94 |           padding: 5px;
95 |           border: 1px solid #ccc;
96 |           border-radius: 4px;
97 |           background-color: #fff;
98 |           color: #333;
99 |           font-size: 16px;
100 |           box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
101 |       }
102 | 
103 | 
104 |     .title-container {
105 |           text-align: center;
106 |           margin-bottom: 10px;
107 |       }
108 | 
109 |     .company-container {
110 |           display: flex;
111 |           gap: 10px;
112 |           align-items: center;
113 |           margin-top: 20px;
114 |           justify-content: center;
115 |           width: 100%;
116 |           margin-bottom: 20px;
117 |       }
118 | 
119 |     .company-container select {
120 |           width: 400px;
121 |           padding: 5px;
122 |           border: 1px solid #ccc;
123 |           border-radius: 4px;
124 |           background-color: #fff;
125 |           color: #333;
126 |           font-size: 16px;
127 |           box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
128 |       }
129 | 
130 |     .submit-button {
131 |           background-color: #063800;
132 |           color: #FFFFFF;
133 |           border: none;
134 |           padding: 10px 20px;
135 |           border-radius: 4px;
136 |           font-size: 16px;
137 |           cursor: pointer;
138 |       }
139 | 
140 | 
141 |     .submit-button:hover {
142 |           background-color: #1E6B47;
143 |       }
144 | 
145 |     .report-container{
146 |       background-color: #F5F5F5;
147 |       color: #1C1C1C;
148 |       display: flex;
149 |       padding: 10px;
150 |       gap: 30px;
151 |       align-items: center;
152 |       justify-content: center;
153 |       margin-bottom: 30px;
154 |     }
155 | 
156 |     .selected-company {
157 |       background-color: white;
158 |       padding: 20px;
159 |       margin: 20px auto;
160 |       align-items: center;
161 |       justify-content: center;
162 |       box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
163 |       border: 2px solid black;
164 |       display: inline-block;
165 |       width: 90%; /* Adjust width for better layout */
166 |       max-width: 1400px;
167 |     }
168 | 
169 |     /* Table Styling */
170 |     .selected-company table {
171 |       width: 100%;
172 |       border-collapse: collapse;
173 |     }
174 | 
175 |     .selected-company th, .selected-company td {
176 |       border: 1px solid black;
177 |       padding: 8px;
178 |       text-align: center;
179 |     }
180 | 
181 | 
182 |     .selected-company th {
183 |       background-color: #063800;
184 |       color: white;
185 |     }
186 | 
187 | 
188 |     /* Style the Download Button */
189 |     .selected-company a.btn-success {
190 |       display: block;
191 |       margin: 10px auto;
192 |       text-align: center;
193 |       background-color: #063800;
194 |       color: white;
195 |       padding: 10px 15px;
196 |       font-size: 16px;
197 |       border-radius: 5px;
198 |       text-decoration: none;
199 |       transition: background-color 0.3s ease;
200 |     }
201 | 
202 | 
203 |     .selected-company a.btn-success:hover {
204 |       background-color: #1E6B47;
205 |     }
206 | 
207 | 
208 |     .navigation {
209 |           position: absolute;
210 |           left:0;
211 |           width:100px;
212 |           height:100%;
213 |           background:  #063800;
214 |           box-shadow: 25px 25px 75px rgba(0,0,0,0.25), 10px 10px 70px rgba(0,0,0,0.25), inset 5px 5px 10px rgba(0,0,0,0.5), inset 5px 5px 20px rgba(255,255,255,0.2) , inset -5px -5px 15px rgba(0,0,0,0.75);
215 |           display:center;
216 |           justify-content:center;
217 |           align-items:center;
218 |           flex-direction:column;
219 |           gap:10px;
220 |           transform: translateX(-100%);
221 |           transition: transform 0.3s ease;
222 | 
223 |       }
224 | 
225 | 
226 |     /* Class to toggle menu visibility */
227 |     .navigation.show {
228 |           transform: translateX(0);
229 |       }
230 | 
231 | 
232 | 
233 |     .navigation li {
234 |           position:relative;
235 |           list-style:none;
236 |           width:80px;
237 |           height: 80px;
238 |           display:flex;
239 |           justify-content:center;
240 |           margin: 0 5px;
241 |       }
242 | 
243 | 
244 | 
245 | 
246 |     .navigation li::before {
247 |           content: '';
248 |           position: absolute;
249 |           top:calc(50% - 2.5px);
250 |           left: 20px;
251 |           width:5px;
252 |           height: 5px;
253 |           border-radius:50%;
254 |           transition:0.5s;
255 | 
256 |       }
257 | 
258 | 
259 | 
260 | 
261 |     .navigation li.active::before {
262 |           background:white;
263 |           box-shadow:0 0 5px white,
264 |           0 0 10px white,
265 |           0 0 20px white,
266 |           0 0 30px white,
267 |           0 0 40px white;
268 |       }
269 | 
270 | 
271 |     .navigation li a {
272 |           display:flex;
273 |           justify-content:center;
274 |           align-items:center;
275 |           flex-direction:column;
276 |           text-decoration:none;
277 |       }
278 | 
279 | 
280 |     .navigation li a .icon {
281 |           color: white;
282 |           transition: 0.5s;
283 |           transition-delay: 0.2s;
284 |           font-size: 1.5em;
285 |       }
286 | 
287 |     .navigation li.active a .icon::before{
288 |           transform:scale(1);
289 |       }
290 | 
291 | 
292 |     .navigation li a .text{
293 |           position: absolute;
294 |           left:130px;
295 |           font-size:1.25em;
296 |           color:white;
297 |           visibility:hidden;
298 |           transition:0.5s;
299 |       }
300 | 
301 | 
302 |     .navigation li a .text::before {
303 |           content: '';
304 |           position: absolute;
305 |           top: 50%
306 |           left: -4px;
307 |           transform:translateY(-50%) rotate(45deg);
308 |           width:10px;
309 |           height:10px;
310 |       }
311 | 
312 |     .navigation li:hover a .text {
313 |           visibility: visible;
314 |       }
315 | 
316 |     .hamburger-icon {
317 |           font-size: 30px;
318 |           color: white;
319 |           cursor: pointer;
320 |           position: absolute;
321 |           top: 20px;
322 |           left: 20px;
323 |           z-index: 100;
324 |       }
325 | 
326 | 
327 |     .sidebar1 {
328 |           display: flex;
329 |           flex-direction: column;
330 |           align-items: center;
331 |           justify-content: center;
332 |           border: 1px solid #ccc;
333 |           border-radius: 8px;
334 |           margin-left: 50px;
335 |           margin-top: 40px;
336 |           float: left;
337 |           width: 250px;
338 |           height: 150px;
339 |           padding: 20px;
340 |           background-color: white;
341 |           color: white;
342 |           z-index: 1000;
343 |       }
344 | 
345 | 
346 |       .dropdown {
347 |             z-index: 15;
348 |             position: absolute;
349 |             top: 20px;
350 |             right: 20px;
351 |             display: inline-block;
352 |             border: 1px solid white;
353 |             background-color: white;
354 |             border-radius: 12px;
355 |             padding: 4px 7px;
356 |             font-size: 16px;
357 |             cursor: pointer;
358 |             align-items: center;
359 |       }
360 | 
361 | 
362 |       .dropdown-content {
363 |         display: none;
364 |         position: absolute;
365 |         padding: 5px 15px;
366 |         font-size: 16px;
367 |         background-color: white;
368 |         min-width: 100px;
369 |         box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
370 |         z-index: 1;
371 |       }
372 | 
373 | 
374 |       .dropdown-content a {
375 |         color: black;
376 |         padding: 12px 16px;
377 |         text-decoration: none;
378 |         display: block;
379 |       }
380 | 
381 | 
382 |       .dropdown-content a:hover {background-color: #2e8b563d;}
383 | 
384 | 
385 |       .dropdown:hover .dropdown-content {display: block;}
386 | 
387 | 
388 |       .dropdown:hover .dropbtn {background-color: rgba(255, 255, 255, 0.607);}
389 |       .dropbtn {
390 |         background-color: white;
391 |         color:  #063800;
392 |         padding: 16px;
393 |         font-size: 16px;
394 |         border: none;
395 |         cursor: pointer;
396 |       }
397 | 
398 | 
399 |       .nav-tabs .nav-link {
400 |          background-color: #063800 !important;
401 |          color: white !important; /* Ensure text is readable */
402 |          border: none !important; /* Optional: remove default border */
403 |      }
404 | 
405 | 
406 |      .nav-tabs .nav-link.active {
407 |          background-color: #045000 !important; /* Slightly darker shade for active tab */
408 |          color: white !important;
409 |      }
410 | 
411 | 
412 |     .nav-tabs {
413 |       border-bottom: none !important;
414 |       margin-bottom: 0 !important;
415 |       padding-bottom: 0 !important;
416 |     }
417 | 
418 |     .tab-content {
419 |       color:#F5F5F5;
420 |       background-color: #1C1C1C !important;
421 |       margin-top: -1px !important;
422 |       border-radius: 0 0 8px 8px;
423 |       border: none !important;
424 |     }
425 | 
426 | 
427 |     .tab-pane {
428 |       background-color: #1C1C1C !important;
429 |       margin: 0 !important;
430 |       border: none !important;
431 |     }
432 | 
433 | 
434 |     .tab-pane > div {
435 |       background-color: #1C1C1C !important;
436 |       border: none !important;
437 |       margin: 0 !important;
438 |       padding: 20px;
439 |     }
440 |     .page-bottom {
441 |       background-color: #1C1C1C !important;
442 |       padding: 50px 0; /* Adds spacing */
443 |       min-height: 1000px; /* Adjust as needed */
444 |     }
445 | 
446 |     #loading-spinner {
447 |                  display: none;
448 |                  width: 24px;
449 |                  height: 24px;
450 |                  border: 4px solid rgba(46, 139, 87, 0.3);
451 |                  border-top: 4px solid #2E8B57;
452 |                  border-radius: 50%;
453 |                  animation: spin 1s linear infinite;
454 |              }
455 | 
456 | 
457 |     @keyframes spin {
458 |                  0% { transform: rotate(0deg); }
459 |                  100% { transform: rotate(360deg); }
460 |              }
461 | 
462 |       .chart-container {
463 |            width: 100%;
464 |            max-width: 800px;
465 |            margin: 20px auto;
466 |        }
467 | 
468 | 
469 | 
470 |   </style>
471 | </head>
472 | <body>
473 |    <div class="logo-header-container">
474 |        <img src="{{ url_for('static', filename='images/missiTrack.png') }}" alt="Logo" class="logo">
475 |        <div class="div1">
476 |            <h1 style="color:white; text-align:center;"> EmissiTrack</h1>
477 |            <p class="catchy-phrase">Advanced Search</p>
478 |        </div>
479 |    </div>
480 | 
481 |   <div class="dropdown">
482 |       <button class="dropbtn">My Pro Account</button>
483 |       <div class="dropdown-content">
484 |           <a href="{{url_for('register')}}">Create an account</a>
485 |           <a href="{{url_for('login')}}">Login</a>
486 |       </div>
487 |   </div>
488 |   <div class="hamburger-icon">&#9776;</div>
489 |      <ul class="navigation">
490 |       <li class="active">
491 |           <a href="{{url_for('test')}}">
492 |               <span class="icon"> <ion-icon name="home-outline"></ion-icon></span>
493 |           </a>
494 |       </li>
495 |       <li>
496 |           <a href="{{url_for('instructions')}}">
497 |               <span class="icon"> <ion-icon name="help-circle-outline"></ion-icon></span>
498 |           </a>
499 |       </li>
500 |       <li>
501 |           <a href="{{url_for('advanced_search')}}">
502 |               <span class="icon"> <ion-icon name="funnel-outline"></ion-icon></span> <!-- ✅ Corrected -->
503 |           </a>
504 |       </li>
505 |       <li>
506 |           <a href="{{url_for('register')}}">
507 |               <span class="icon"><ion-icon name="person-add-outline"></ion-icon></span> <!-- ✅ Corrected -->
508 |           </a>
509 |       </li>
510 |       <li class="active">
511 |           <a href=/firstpage>
512 |               <span class="icon"> <ion-icon name="grid-outline"></ion-icon></span> <!-- ✅ First Page Icon -->
513 |           </a>
514 |       </li>
515 |   </ul>
516 |      <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
517 |          <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
518 |          <script>
519 |              document.addEventListener('DOMContentLoaded', function () {
520 |                  const hamburger = document.querySelector('.hamburger-icon');
521 |                  const navigation = document.querySelector('.navigation');
522 |                  let isOpen = false;
523 | 
524 | 
525 | 
526 | 
527 | 
528 | 
529 | 
530 | 
531 |                  hamburger.addEventListener('click', function () {
532 |                      // Toggle menu visibility
533 |                      isOpen = !isOpen;
534 |                      if (isOpen) {
535 |                          navigation.classList.add('show');
536 |                      } else {
537 |                          navigation.classList.remove('show');
538 |                      }
539 |                  });
540 | 
541 | 
542 | 
543 | 
544 | 
545 | 
546 | 
547 | 
548 |                  // Keep your existing navigation item click event listener
549 |                  let list = document.querySelectorAll('.navigation li');
550 |                  function activeLink() {
551 |                      list.forEach((item) => item.classList.remove('active'));
552 |                      this.classList.add('active');
553 |                  }
554 |                  list.forEach((item) => item.addEventListener('click', activeLink));
555 |              });
556 | 
557 | 
558 | 
559 | 
560 | 
561 | 
562 | 
563 | 
564 |          </script>
565 | 
566 | 
567 |   <form action="/submit" method="post">
568 |       <div class="dropdown-container">
569 |           <div>
570 |               <label for="country">Choose a Country:</label>
571 |               <select name="country" id="country">
572 |                   <option value="all">All</option>
573 |                   {% for country in countries %}
574 |                   <option value="{{ country }}">{{ country }}</option>
575 |                   {% endfor %}
576 |               </select>
577 |           </div>
578 |           <div>
579 |               <label for="sector">Choose a Sector:</label>
580 |               <select name="sector" id="sector">
581 |                   <option value="all">All</option>
582 |                   {% for sector in sectors %}
583 |                   <option value="{{ sector }}">{{ sector }}</option>
584 |                   {% endfor %}
585 |               </select>
586 |           </div>
587 |           <div>
588 |               <label for="industry">Choose an Industry:</label>
589 |               <select name="industry" id="industry">
590 |                   <option value="all">All</option>
591 |                   {% for industry in industries %}
592 |                   <option value="{{ industry }}">{{ industry }}</option>
593 |                   {% endfor %}
594 |               </select>
595 |           </div>
596 |           {% if not companies %}
597 |           <div>
598 |               <input type="submit" value="Submit" class="submit-button">
599 |           </div>
600 |           {% endif %}
601 |       </div>
602 |       {% if companies %}
603 |       <div class="company-container">
604 |           <label for="company">Choose a Company:</label>
605 |           <select name="company" id="company">
606 |               {% for company in companies %}
607 |               <option value="{{ company }}">{{ company }}</option>
608 |               {% endfor %}
609 |           </select>
610 |           <div style="display: flex; justify-content: center; align-items: center; gap: 10px; margin-top: 10px;">
611 |              <button type="submit" id="submit" class="submit-button">Search</button>
612 |              <div id="loading-spinner" style="display: none;"></div>
613 |      </div>
614 |       </div>
615 |       {% endif %}
616 |       {% if selected_company %}
617 | 
618 |       <div class="report-container">
619 |           {% if report_url %}
620 |               <p>Latest ESG Report Link for {{selected_company}}: <a href="{{ report_url }}" target="_blank">{{ report_url }}</a></p>
621 | 
622 | 
623 |           {% else %}
624 |               <p>No report found.</p>
625 |           {% endif %}
626 |       </div>
627 | 
628 |       <ul class="nav nav-tabs mt-4" id="resultTabs" role="tablist">
629 |           <li class="nav-item" role="presentation">
630 |               <button class="nav-link active" id="table-tab" data-bs-toggle="tab" data-bs-target="#table-content" type="button" role="tab">Extracted Table <i class="fa-solid fa-table"></i></button>
631 |           </li>
632 |           <li class="nav-item" role="presentation">
633 |               <button class="nav-link" id="chart-tab" data-bs-toggle="tab" data-bs-target="#chart-content" type="button" role="tab">Data Visualization <i class="fa-solid fa-chart-column"></i></button>
634 |           </li>
635 |       </ul>
636 |       <!-- Tab Content -->
637 |       <div class="tab-content mt-3" id="resultTabsContent">
638 |           <!-- Table Section -->
639 |           <div class="tab-pane fade show active" id="table-content" role="tabpanel">
640 |               {% if selected_company and emissions_data %}
641 |               <div class="selected-company">
642 |                   <a href="{{ url_for('download_table', company_name=selected_company) }}" class="btn btn-success mt-3">Download Table</a>
643 |                   <div>
644 |                       {{ emissions_data | safe }}
645 |                   </div>
646 |               {% else %}
647 |                   <p>No table data available.</p>
648 |               {% endif %}
649 |           </div>
650 |           </div>
651 | 
652 |         <!-- Data Visualization Section -->
653 |          <div class="tab-pane fade" id="chart-content">
654 |         <div class="chart-container">
655 |             <h3>Emissions Data Visualization</h3>
656 |             <canvas id="emissionsChart"></canvas>
657 |         </div>
658 |            {% endif %}
659 |     </div>
660 |          <div class="page-bottom">
661 |       </div>
662 |      </div>
663 |   </form>
664 | 
665 | 
666 |      <!-- Bootstrap JS (Ensure Bootstrap's JavaScript is included) -->
667 |      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
668 |     <!-- React and ReactDOM via CDN -->
669 |     <script src="https://unpkg.com/react@17/umd/react.production.min.js"></script>
670 |     <script src="https://unpkg.com/react-dom@17/umd/react-dom.production.min.js"></script>
671 | 
672 |     <!-- Material-UI Core (includes CircularProgress) -->
673 |     <script crossorigin src="https://unpkg.com/@mui/material@latest/umd/material-ui.production.min.js"></script>
674 | 
675 |     <script>
676 |     document.addEventListener("DOMContentLoaded", function () {
677 |          const { CircularProgress } = window.MaterialUI || {};
678 |          const spinnerContainer = document.getElementById("loading-spinner");
679 |          const submitButton = document.getElementById("submit");
680 |          const form = document.querySelector("form");
681 | 
682 |          let spinnerInitialized = false;
683 |          function initializeSpinner() {
684 |              if (!spinnerInitialized && CircularProgress) {
685 |                  const spinner = React.createElement(CircularProgress, { color: "success", size: 24 });
686 |                  ReactDOM.render(spinner, spinnerContainer);
687 |                  spinnerInitialized = true;
688 |              }
689 |          }
690 |          function showSpinner() {
691 |              submitButton.disabled = true;
692 |              submitButton.innerText = "Searching...";
693 |              initializeSpinner();
694 |              spinnerContainer.style.display = "inline-block"; // Show only when "Searching..."
695 |          }
696 | 
697 |          function hideSpinner() {
698 |              submitButton.disabled = false;
699 |              submitButton.innerText = "Search";
700 |              spinnerContainer.style.display = "none";
701 |          }
702 |          form.addEventListener("submit", function () {
703 |              showSpinner();
704 |          });
705 | 
706 |          //Reset spinner if user navigates away or cancels search
707 |          submitButton.addEventListener("click", function () {
708 |              if (submitButton.innerText === "Searching...") {
709 |                  hideSpinner();
710 |              }
711 |          });
712 |         });
713 |     </script>
714 |     <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
715 | <script>
716 | document.addEventListener("DOMContentLoaded", function () {
717 |     function extractDataFromTable() {
718 |         const table = document.querySelector(".selected-company table");
719 |         if (!table) {
720 |             console.error(" No table found in .selected-company!");
721 |             return;
722 |         }
723 | 
724 |         const rows = table.querySelectorAll("tr");
725 |         if (rows.length < 2) {
726 |             console.error(" Table has no data rows.");
727 |             return;
728 |         }
729 | 
730 |         // Extract Headers & Year Columns
731 |         const headers = Array.from(rows[0].querySelectorAll("th")).map(th => th.innerText.trim());
732 |         let yearHeaders = headers.filter(h => /^\d{4}$/.test(h));
733 |         let yearIndexes = headers.map((h, i) => (yearHeaders.includes(h) ? i : -1)).filter(i => i !== -1);
734 | 
735 |         if (yearHeaders.length === 0) {
736 |             console.error(" No valid year columns found.");
737 |             return;
738 |         }
739 | 
740 |         console.log(" Extracted Year Headers:", yearHeaders);
741 | 
742 |         let emissionsData = {};
743 |         let dataFound = false;
744 | 
745 |         rows.forEach((row, rowIndex) => {
746 |             if (rowIndex === 0) return;
747 |             const cells = row.querySelectorAll("td");
748 | 
749 |             let metricName = cells[1]?.innerText.trim() || `Metric ${rowIndex}`; // Extract actual metric name from column 2
750 |             let values = yearIndexes.map(colIndex => {
751 |                 let value = parseFloat(cells[colIndex]?.innerText.replace(/,/g, "").trim()) || 0;
752 |                 if (value !== 0) dataFound = true;
753 |                 return value;
754 |             });
755 | 
756 |             emissionsData[metricName] = values;
757 |         });
758 | 
759 |         if (dataFound) {
760 |             console.log(" Emissions Data:", emissionsData);
761 |             setTimeout(() => renderHistogram(yearHeaders, emissionsData), 500);
762 |         } else {
763 |             console.warn(" No valid emissions data found.");
764 |         }
765 |     }
766 | 
767 |     function renderHistogram(labels, emissionsData) {
768 |         const canvas = document.getElementById("emissionsChart");
769 |         if (!canvas) {
770 |             console.error(" No canvas element found!");
771 |             return;
772 |         }
773 | 
774 |         const ctx = canvas.getContext("2d");
775 | 
776 |         if (window.myChart) {
777 |             window.myChart.destroy();
778 |         }
779 | 
780 |         const datasets = Object.keys(emissionsData).map((metric, index) => ({
781 |             label: metric, // Use metric names from column 2 as legend labels
782 |             data: emissionsData[metric],
783 |             backgroundColor: getRandomColor(index),
784 |             borderWidth: 1
785 |         }));
786 | 
787 |         window.myChart = new Chart(ctx, {
788 |             type: "bar",
789 |             data: { labels: labels, datasets: datasets },
790 |             options: {
791 |                 responsive: true,
792 |                 plugins: {
793 |                     legend: { position: "top" },
794 |                     title: { display: true, text: "Emissions Over the Years" }
795 |                 },
796 |                 scales: {
797 |                     x: { title: { display: true, text: "Year" } },
798 |                     y: { title: { display: true, text: "Emissions" }, beginAtZero: true }
799 |                 }
800 |             }
801 |         });
802 |     }
803 | 
804 |     function getRandomColor(index) {
805 |         const colors = ["rgba(255, 99, 132, 0.7)", "rgba(54, 162, 235, 0.7)", "rgba(255, 206, 86, 0.7)"];
806 |         return colors[index % colors.length];
807 |     }
808 | 
809 |     extractDataFromTable();
810 | });
811 | 
812 | </script>
813 | </body>
814 | </html>
815 | 
```

src/templates/firstpage.html
```
1 | 
2 | 
3 | 
4 | 
5 | <!DOCTYPE html>
6 | <html lang="en">
7 | <head>
8 | <meta charset="UTF-8">
9 | <meta name="viewport" content="width=device-width, initial-scale=1.0">
10 | <title>EmissiTrack</title>
11 | <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
12 |  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
13 | <style>
14 |    html, body {
15 |       width: 100vw;  /* Ensures full width of the viewport */
16 |       overflow-x: hidden; /* Prevents horizontal scroll issues */
17 |       margin: 0;
18 |       padding: 0;
19 |       font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
20 |       background-color: #1C1C1C;
21 |       color: #333333;
22 |     }
23 | 
24 | 
25 |     .footer {
26 |        display: flex; flex-direction: column;
27 |        justify-content: space-around;
28 |        align-items: center;
29 |        background-color: #1C1C1C;
30 |        color: #F5F5F5;
31 |        padding: 20px;
32 |        flex-wrap: wrap;
33 |        text-align: center;
34 |     }
35 | 
36 | 
37 |     .footer-section {
38 |        flex: 1;
39 |        min-width: 200px;
40 |        margin: 10px;
41 |     }
42 | 
43 | 
44 | 
45 |     .footer-section ul {
46 |        list-style: none;
47 |        padding: 0;
48 |        display: flex;
49 |        gap:15px;
50 |        justify-content: center;
51 |     }
52 | 
53 | 
54 |     .footer-section ul li {
55 |        margin: 5px 0;
56 |     }
57 | 
58 | 
59 |     .footer-section ul li a {
60 |        color: #F5F5F5;
61 |        text-decoration: none;
62 |     }
63 | 
64 | 
65 |     .footer-section ul li a:hover {
66 |        text-decoration: underline;
67 |     }
68 | 
69 | 
70 |     .social-icons a {
71 |        font-size: 24px;
72 |        color: white;
73 |        margin: 0 10px;
74 |        text-decoration: none;
75 |     }
76 | 
77 | 
78 |     .social-icons a:hover {
79 |        color: #606060;
80 |     }
81 | 
82 | 
83 |     #description {
84 |          font-weight:bold;
85 |     }
86 | 
87 | 
88 |      #learnMoreSection p {
89 |          margin-bottom: 50px; /* Adjust this value as needed */
90 |      }
91 | 
92 | 
93 |      #learnMoreBtn {
94 |          position:relative;
95 |          left: 50%; /* Adjust this value to move it more to the right */
96 |          top:200px;
97 |          width: auto; /* Adjust width automatically based on content */
98 |          font-size: 20px; /* Increase font size */
99 |          padding: 16px 32px;
100 |          font-size: 20px; /* Increase font size */
101 |          text-align: center; /* Center the text */
102 |          display: inline-flex; /* Ensure proper button behavior */
103 |          width: auto; /* Adjust width automatically based on content */
104 |          height: 50px; /* Adjust height automatically */
105 |          white-space: nowrap;
106 |          color:white;
107 |          font-weight: bold;
108 |          align-items: center; /* Centers vertically */
109 |          justify-content: center; /* Centers horizontally */
110 |          transform: translateX(-50%);
111 |          left: 51%;
112 |          background-color:#063800;
113 | 
114 |      }
115 | 
116 | 
117 |      #learnMoreSection {
118 |          color:white;
119 |      }
120 | 
121 | 
122 |    .btn {/* Keeps the button fixed in one position */
123 |        bottom: 120px;
124 |        padding: 16px 32px;
125 |        font-size: 16px;
126 |        color:   #2D2D2D ;
127 |        background-color:white  ;
128 |        border: none;
129 |        border-radius: 8px;
130 |        text-decoration: none;
131 |        cursor: pointer;
132 |        justify-content: center;
133 |        transition: background-color 0.3s ease;
134 |        display: inline-flex; /* Enables flexbox */
135 |   align-items: center; /* Centers text vertically */
136 |   justify-content: center; /* Centers text horizontally */
137 | 
138 | 
139 |    }
140 | 
141 |    .btn:hover {
142 |        background-color: #3B6633;
143 |    }
144 | 
145 | 
146 | 
147 | 
148 |    h3{
149 |           color:  white ;
150 |           font-size: 24px;
151 |           font-weight: bold;
152 |           margin-top: 0px;
153 |    }
154 | 
155 | 
156 | 
157 | 
158 |    @keyframes moveText {
159 |        0% {
160 |            transform: translateX(0);
161 |        }
162 |        100% {
163 |            transform: translateX(-100%);
164 |        }
165 |    }
166 | 
167 | 
168 |   .content-container {
169 |   display: flex;
170 |   justify-content: center; /* Centers elements horizontally */
171 |   align-items: center; /* Aligns elements vertically */
172 |   gap: 200px; /* Space between the two elements */
173 |   max-width: 1100px; /* Prevents excessive stretching */
174 |   margin: 250px auto 50px;  /* Centers everything on the page */
175 |   flex-wrap: wrap; /* Ensures responsiveness */
176 |   position: relative;
177 | }
178 | 
179 | 
180 | 
181 | /* Ensure Both Containers Have the Same Size */
182 | #imageContainer, .information_container {
183 |   width: 450px; /* Same width for both */
184 |   height: 440px; /* Same height for both */
185 |   display: flex;
186 |   align-items: center;
187 |   justify-content: center;
188 |   border-radius: 10px; /* Ensures uniform rounded corners */
189 |   box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3); /* Matches the box-shadow */
190 | }
191 | 
192 |    .information_container{
193 |     background-color: #063800;
194 |     box-shadow: 0px 16px 32px rgba(0, 0, 0, 0.5);
195 |     text-align: center;
196 |     color: white;
197 |     align-items: center;
198 |     border-radius: 10px;
199 |     padding: 20px;
200 |     display: block;
201 |        white-space: pre-line;
202 |        font-size: 23px;
203 |        font-weight: bold;
204 |    }
205 | 
206 | 
207 |    #container {
208 |        width: 100%;
209 |        text-align: right; /* Aligns text to the right */
210 |        position: absolute;
211 |        top: 150px;
212 |    }
213 | 
214 | 
215 |    #imageContainer {
216 |        text-align: center;
217 |    }
218 | 
219 | 
220 |    #dynamicImage {
221 |        width: 450px; /* Adjust size as needed */
222 |        height: 440px;
223 |        border-radius: 10px;
224 | 
225 | 
226 | 
227 | 
228 |    }
229 | 
230 | 
231 |    #dynamicText {
232 |     z-index: 15;
233 |        font-size: 24px;
234 |         font-family: ;
235 |        display: inline-block;
236 |        padding: 10px;
237 |        color: #063800;
238 |        position: relative;
239 |        white-space: nowrap; /* Prevent text from wrapping */
240 |        animation: moveText 45s linear infinite alternate;
241 |    }
242 | 
243 | 
244 |    #dynamicTextContainer {
245 |         z-index: 10;
246 |        display: inline-block;
247 |        background-color: white; /* White background box */
248 |        padding: 10px 20px; /* Adds padding inside the box */
249 |        border-radius: 8px; /* Rounds the corners */
250 |        position: relative;
251 |        width:100%;
252 |        height:60px;
253 |        top:0px;
254 | 
255 |    }
256 | 
257 |    .div1 {
258 |     z-index: 10; /* Ensures it appears above other elements */
259 |     position: relative; /* Required for z-index to work */
260 |        height: 160px;
261 |        width: 100%; /* Ensure it takes full width */
262 |        margin: 0;
263 |        background-color: #063800;
264 |        display: flex;
265 |        align-items: center; /* Centers vertically */
266 |        justify-content: center; /* Centers horizontally */
267 |        box-shadow: 0px 4px 15px rgba(20, 80, 20, 0.6);
268 |    }
269 |    .catchy-phrase {
270 |    color: white;
271 |    font-size: 20px;
272 |    margin-top: 5px; /* Adjust spacing between header and phrase */
273 | }
274 | 
275 | 
276 |     .hamburger-icon {
277 |         font-size: 30px;
278 |         color: white;
279 |         cursor: pointer;
280 |         position: absolute;
281 |         top: 20px;
282 |         left: 20px;
283 |     }
284 | 
285 |     .sidebar1 {
286 |         display: flex;
287 |         flex-direction: column;
288 |         align-items: center;
289 |         justify-content: center;
290 |         border: 1px solid #ccc;
291 |         border-radius: 8px;
292 |         margin-left: 50px;
293 |         float: left;
294 |         width: 250px;
295 |         height: 150px;
296 |         padding: 20px;
297 |         background-color: white;
298 |         color: white;
299 | 
300 |     }
301 |     .navigation {
302 |         position: fixed; /* Sticks to the side */
303 |         left: 0;
304 |         top: 0;
305 |         width: 100px;
306 |         height: 100vh; /* 100% of the viewport height */
307 |         background:  #063800;
308 |         box-shadow: 25px 25px 75px rgba(0,0,0,0.25), 10px 10px 70px rgba(0,0,0,0.25),
309 |                     inset 5px 5px 10px rgba(0,0,0,0.5), inset 5px 5px 20px rgba(255,255,255,0.2),
310 |                     inset -5px -5px 15px rgba(0,0,0,0.75);
311 |         display: flex;
312 |         justify-content: center;
313 |         align-items: center;
314 |         flex-direction: column;
315 |         gap: 10px;
316 |         transform: translateX(-100%);
317 |         transition: transform 0.3s ease;
318 | }
319 | 
320 |      .navigation.show {
321 |         transform: translateX(0);
322 |     }
323 | 
324 |     .navigation li {
325 |         position:relative;
326 |         list-style:none;
327 |         width:80px;
328 |         height: 80px;
329 |         display:flex;
330 |         justify-content:center;
331 |         margin: 0 5px;
332 | 
333 |     }
334 | 
335 |     .navigation li::before {
336 |         content: '';
337 |         position: absolute;
338 |         top:calc(50% - 2.5px);
339 |         left: 20px;
340 |         width:5px;
341 |         height: 5px;
342 |         border-radius:50%;
343 |         transition:0.5s;
344 | 
345 |     }
346 | 
347 |     .navigation li.active::before {
348 |         background:white;
349 |         box-shadow:0 0 5px white,
350 |         0 0 10px white,
351 |         0 0 20px white,
352 |         0 0 30px white,
353 |         0 0 40px white;
354 |     }
355 | 
356 |     .navigation li a {
357 |         display:flex;
358 |         justify-content:center;
359 |         align-items:center;
360 |         flex-direction:column;
361 |         text-decoration:none;
362 |     }
363 | 
364 |     .navigation li a .icon {
365 |         color: white;
366 |         transition: 0.5s;
367 |         transition-delay: 0.2s;
368 |         font-size: 1.5em; /* Adjust this value to your preference */
369 |     }
370 | 
371 |     .navigation li.active a .icon::before{
372 |         transform:scale(1);
373 | 
374 |     }
375 | 
376 |     .navigation li a .text{
377 |         position: absolute;
378 |         left:130px;
379 |         font-size:1.25em;
380 |         color:white;
381 |         visibility:hidden;
382 |         transition:0.5s;
383 | 
384 | 
385 |     }
386 | 
387 | 
388 |     .navigation li a .text::before {
389 |         content: '';
390 |         position: absolute;
391 |         top: 50%
392 |         left: -4px;
393 |         transform:translateY(-50%) rotate(45deg);
394 |         width:10px;
395 |         height:10px;
396 |     }
397 | 
398 |     .navigation li:hover a .text {
399 |         visibility: visible;
400 |     }
401 |     .logo {
402 |      z-index: 20;
403 |      max-height: 100px;
404 |      width: auto;
405 |      top: 30px;
406 |      left: 200px;
407 |      margin-right: 10px;
408 |     }
409 | 
410 |    *{
411 |          margin: 0;
412 |          padding: 0;
413 |          box-sizing: border-box;
414 |          font-family: sans-serif;
415 |      }
416 | 
417 | 
418 |      .main{
419 |          display: flex;
420 |          flex-direction: column;
421 |          align-items: center;
422 |          justify-content: center;
423 |          width: 100%;
424 |          margin-top: 90px;
425 |      }
426 | 
427 |      .full-boxer{
428 |          display: flex;
429 |          flex-wrap: wrap;
430 |          justify-content: center;
431 |          align-items: center;
432 |          width: 100%;
433 |      }
434 | 
435 | 
436 |      .box-top{
437 |          display: flex;
438 |          justify-content: space-between;
439 |          align-items: center;
440 |          margin-bottom: 20px;
441 |      }
442 | 
443 |      .comment-box:hover{
444 |          margin-top: 12px;
445 |      }
446 | 
447 |       .comments-container {
448 |      background-color: #414340;
449 |      padding: 30px;
450 |      border-radius: 10px;
451 |      box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
452 |      margin: 10px auto;
453 |      width: 80%;
454 |  }
455 |  .full-boxer {
456 |      display: flex;
457 |      flex-wrap: wrap;
458 |      justify-content: space-around;
459 |  }
460 |  .comment-box {
461 |      background: white;
462 |      padding: 20px;
463 |      margin: 15px;
464 |      border-radius: 8px;
465 |      cursor: pointer;
466 |      box-shadow: 3px 3px 25px rgba(0,0,0,0.3);
467 |      width: 22%;
468 | 
469 |  }
470 | 
471 | 
472 |      .Profile{
473 |          display: flex;
474 |          align-items: center;
475 |      }
476 | 
477 | 
478 |      .profile-image{
479 |          width: 70px;
480 |          height: 70px;
481 |          box-shadow: 2px 2px 30px rgba(0,0,0,0.3);
482 |          overflow: hidden;
483 |          border-radius: 50%;
484 |          margin-right: 10px;
485 |      }
486 | 
487 | 
488 |      .profile-image img{
489 |          width: 100%;
490 |          height: 100%;
491 |          object-fit: cover;
492 |          object-position: center;
493 |      }
494 | 
495 |      .Name{
496 |          display: flex;
497 |          flex-direction: column;
498 |          margin-left: 10px;
499 |      }
500 | 
501 | 
502 |      .Name strong{
503 |          color: black;
504 |          font-size: 18px;
505 |      }
506 | 
507 |      .Name span{
508 |          color: gray;
509 |          margin-top: 2px;
510 |      }
511 | 
512 |      .comment p{
513 |          color: black;
514 |      }
515 |      .padding-for-info {
516 |   max-width: 1100px;
517 |   padding: 0 40px;
518 |   text-align: center;
519 |   margin: 0 auto;
520 | 
521 | }
522 | 
523 |     .centered-link {
524 |     text-align: center;
525 |     margin-top: 20px;
526 | }
527 | 
528 | .centered-link a {
529 |     font-size: 18px;
530 |     color: white; /* Change to any preferred color */
531 |     text-decoration: none;
532 | 
533 | }
534 | 
535 | .centered-link a:hover {
536 |     color:white; /* Color on hover */
537 |     text-decoration: underline;
538 | }
539 | 
540 | </style>
541 | </head>
542 | <body>
543 | <div class="div1">
544 |    <img src="{{ url_for('static', filename='images/missiTrack.png') }}" alt="Logo" class="logo">
545 |     <h1 style="color:white; text-align:center;"> EmissiTrack</h1>
546 |    </div>
547 |  <div class="catchy-phrase">
548 |      <h2>Your Carbon Insights, Simplified</h2></div>
549 |  <a href="#learnMoreSection" class="btn" id="learnMoreBtn">Learn More  <i class="fa-solid fa-arrow-down"></i></a>
550 | <script>
551 |  document.getElementById("learnMoreBtn").addEventListener("click", function(event) {
552 |      event.preventDefault(); // Prevent default anchor behavior
553 |      document.getElementById("learnMoreSection").scrollIntoView({
554 |          behavior: "smooth"
555 |      });
556 |  });
557 | </script>
558 | <div class="centered-link">
559 |     <a href="emissions_map"> View the top 40 companies along with their ESG ratings.</a>
560 | </div>
561 | 
562 | 
563 | <div class="content-container">
564 |   <div id="imageContainer">
565 |       <img id="dynamicImage" src="{{ url_for('static', filename='images/image1.png') }}" alt="image1">
566 |   </div>
567 | 
568 | <div class="information_container">
569 | <h6 id="description">
570 |    EmissiTrack helps you effortlessly retrieve and analyze Scope 1 and Scope 2 carbon emissions data for listed companies using ISINs or company names. With real-time data sourcing from CSR reports, interactive filtering, and easy downloads, EmissiTrack empowers businesses and investors to make informed sustainability decisions.
571 | </h6>
572 | <br>
573 | <a href="/test" class="btn">Start Using for Free</a>
574 | </div>
575 | 
576 | 
577 | 
578 | 
579 | 
580 | 
581 | 
582 | 
583 | </div>
584 | <script>
585 |    document.addEventListener("DOMContentLoaded", function () {
586 |        const h6Element = document.getElementById("description");
587 |        const words = h6Element.innerText.split(" ");
588 |        let formattedText = "";
589 |        for (let i = 0; i < words.length; i++) {
590 |            formattedText += words[i] + " ";
591 |            if ((i + 1) % 6 === 0) {
592 |                formattedText += "<br>"; // Insert line break after every 6 words
593 |            }
594 |        }
595 |        h6Element.innerHTML = formattedText.trim();
596 |    });
597 | </script>
598 | <div id="container">
599 |    <div id="dynamicTextContainer">
600 |        <p id="dynamicText">Dynamically Filter Companies</p>
601 |    </div>
602 | </div>
603 | <script>
604 |    document.addEventListener("DOMContentLoaded", function () {
605 |        const wordsArray = [
606 |            "Retrieve Scope 1 and Scope 2 emissions data",
607 |            "Retrieve CSR Reports",
608 |            "Sustainability Reporting",
609 |            "ESG analysis"
610 |        ];
611 |        const dynamicText = document.getElementById("dynamicText");
612 |        let textContent = "";
613 |        // Create a long scrolling text by repeating words with spacing
614 |        for (let i = 0; i < wordsArray.length; i++) {
615 |            textContent += wordsArray[i] + " - ";
616 |        }
617 |        // Duplicate the text to create a seamless scrolling effect
618 |        dynamicText.innerHTML = textContent + textContent;
619 |    });
620 |    // Image Slideshow Logic
621 |    const images = ["image1.png", "image2.png", "image3.png"];
622 |    let imageIndex = 0;
623 |    const imgElement = document.getElementById("dynamicImage");
624 |    window.onload = function() {
625 |          document.getElementById("dynamicImage").src = "{{ url_for('static', filename='images/image1.png') }}";
626 |      };
627 |    function changeImage() {
628 |        imgElement.src = "{{ url_for('static', filename='images/') }}" + images[imageIndex];
629 |        imageIndex = (imageIndex + 1) % images.length;
630 |    }
631 |    setInterval(changeImage, 3000); // Change image every 3 seconds
632 | </script>
633 |  <section class="main">
634 |      <h4 style="color:white; margin-top:50px; font-weight:bold;">Learn more from our users</h4>
635 |      <div class="comments-container">
636 |      <div class="full-boxer">
637 |          <div class="comment-box">
638 |              <div class="box-top">
639 |                  <div class="Profile">
640 |                      <div class="profile-image">
641 |                          <img src="{{ url_for('static', filename='images/1.png') }}" alt="1">
642 |                      </div>
643 |                      <div class="Name">
644 |                          <strong>Ranidi Lochana</strong>
645 |                          <span>@Ranidi Lochana</span>
646 |                      </div>
647 |                  </div>
648 |              </div>
649 |              <div class="comment">
650 |                  <p>⭐️⭐️⭐️⭐️⭐️</p>
651 |                  <p>This tool is an excellent resource for academic research on corporate carbon footprints. The ability to retrieve and categorize emissions data dynamically, without spending hours on manual searches, is a huge time-saver. The accuracy and cleaning of the data are impressive, and the ability to export structured datasets makes it easy to conduct further analysis. Nice experience and efficient results, would recommend!</p>
652 |              </div>
653 |          </div>
654 |          <div class="comment-box">
655 |              <div class="box-top">
656 |                  <div class="Profile">
657 |                      <div class="profile-image">
658 |                          <img src="{{ url_for('static', filename='images/2.png') }}" alt="2">
659 |                      </div>
660 |                      <div class="Name">
661 |                          <strong>Senuda Dilwan</strong>
662 |                          <span>@senuda dilwan</span>
663 |                      </div>
664 |                  </div>
665 |              </div>
666 |              <div class="comment">
667 |                  <p>⭐️⭐️⭐️⭐️⭐️</p>
668 |                  <p>As someone responsible for reporting and benchmarking sustainability efforts, I find this tool incredibly valuable. It provides a centralized source of emissions data, reducing the hassle of manually tracking down reports from multiple sources. The user-friendly interface and downloadable CSV format are particularly helpful for integrating data into internal reports. This is the future of corporate carbon tracking!</p>
669 |              </div>
670 |          </div>
671 | 
672 |          <div class="comment-box">
673 |              <div class="box-top">
674 |                  <div class="Profile">
675 |                      <div class="profile-image">
676 |                          <img src="{{ url_for('static', filename='images/3.png') }}" alt="3">
677 |                      </div>
678 |                      <div class="Name">
679 |                          <strong>Rumali fernando</strong>
680 |                          <span>@Rumali fernando</span>
681 |                      </div>
682 |                  </div>
683 |              </div>
684 |              <div class="comment">
685 |                  <p>⭐️⭐️⭐️⭐️⭐️</p>
686 |                  <p>This platform is a game-changer for ESG research! Finding Scope 1 and Scope 2 emissions data used to be a tedious, manual process, requiring hours of combing through CSR reports. This tool simplifies everything—just input an ISIN or company name, and the latest emissions data is instantly retrieved, cleaned, and categorized. The visualization features are a great bonus, making trend analysis much easier. Highly recommend!</p>
687 | 
688 |              </div>
689 |          </div>
690 | 
691 |          <div class="comment-box">
692 |              <div class="box-top">
693 |                  <div class="Profile">
694 |                      <div class="profile-image">
695 |                          <img src="{{ url_for('static', filename='images/4.png') }}" alt="4">
696 |                      </div>
697 |                      <div class="Name">
698 |                          <strong>Midinu Thiranjana</strong>
699 |                          <span>@Midinu Thiranjana</span>
700 |                      </div>
701 |                  </div>
702 |              </div>
703 |              <div class="comment">
704 |                  <p>⭐️⭐️⭐️⭐️⭐</p>
705 |                  <p>A very useful tool for investment decision-making. Reliable emissions data is critical for evaluating companies from an ESG perspective, and this platform makes it easy to access. The filtering and download options allow for quick integration with our internal models. The chatbot offered by the pro account is very useful and enables me to find data more efficiently. </p>
706 | 
707 |              </div>
708 |          </div>
709 |      </div>
710 |      </div>
711 |  </section>
712 |  <section id="learnMoreSection">
713 |   <div class="padding-for-info">
714 |      <h2 style="text-align:center; margin-top:50px; font-weight:bold;">What is EmissiTrack?</h2>
715 |      <p style="text-align:center;">A Smart, Scalable, and Dynamic Solution for Tracking Corporate Carbon Footprints.</p>
716 | 
717 | <p style="text-align:center;">The Carbon Emissions Tracker is a web-based platform designed to dynamically retrieve, categorize, and visualize corporate carbon emissions data for listed companies within the MSCI All World Index. This tool empowers users to access the latest Scope 1 (direct emissions) and Scope 2 (indirect emissions from purchased electricity) data from publicly available sources such as Corporate Social Responsibility (CSR) reports, government databases, and other sustainability disclosures.</p>
718 | 
719 | <p style="text-align:center;">In addition to emissions data, the platform features a real-time news feed with top headlines for each company, keeping users updated on sustainability-related developments. Users can also filter companies by sector, country, industry, and other key parameters to refine their searches and insights.</p>
720 |      <p style="text-align:center;">Emissions data can be visualized in interactive bar charts or structured in a detailed table format. </p>
721 |      <p style="text-align:center;">A premium membership unlocks access to an AI-powered chatbot that assists users with data retrieval, insights, and sustainability analysis.
722 | The chatbot can answer queries, provide company-specific emissions insights, suggest comparisons, and summarize trends.</p>
723 |      </div>
724 | 
725 |  </section>
726 |  <footer class="footer">
727 | 
728 | 
729 |    <div class="footer-section">
730 |        <ul>
731 |            <li><a href="#">About Us</a></li>
732 |            <li><a href="#">Contact</a></li>
733 |            <li><a href="#">Terms of Use</a></li>
734 |            <li><a href="#">Privacy Policy</a></li>
735 |        </ul>
736 |    </div>
737 | 
738 | 
739 |    <div class="footer-section">
740 |        <div class="social-icons">
741 |            <a href="#"><i class="fab fa-facebook"></i></a>
742 |            <a href="https://www.linkedin.com/in/budha/"><i class="fab fa-linkedin"></i></a>
743 |            <a href=""><i class="fas fa-envelope"></i></a>
744 |        </div>
745 |    </div>
746 | </footer>
747 | 
748 | 
749 | <section>
750 |    <p style="text-align:center;color:white">&copy; 2024 EmissiTrack</p>
751 | </section>
752 | </body>
753 | </html>
754 | 
755 | 
756 | 
757 | 
758 | 
759 | 
760 | 
761 | 
762 | 
763 | 
764 | 
765 | 
```

src/templates/index.html
```
1 | <!DOCTYPE html>
2 | <html lang="en">
3 | <head>
4 |     <meta charset="UTF-8">
5 |     <title>My ESG App</title>
6 |     <!-- Add Font Awesome for icons -->
7 |     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
8 |     <!-- Marked.js for client-side Markdown->HTML conversion -->
9 |     <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
10 |     <!-- Chart.js for the line chart -->
11 |     <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
12 |     <!-- Optional: chartjs-plugin-annotation -->
13 |     <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-annotation@2"></script>
14 | 
15 |     <!-- Updated, more polished CSS -->
16 |     <style>
17 |       :root {
18 |         --primary-green: #1a4f1a;
19 |         --secondary-green: #2f8f2f;
20 |         --accent-green: #e8f5e9;
21 |         --text-dark: #2c3e50;
22 |       }
23 | 
24 | 
25 |       body {
26 |        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
27 |        background: linear-gradient(to bottom right, #f8fcf8, #e8f5e9);
28 |        margin: 0;
29 |        color: #2c3e50;
30 |      }
31 |      .content {
32 |       padding: 30px;
33 |     }
34 | 
35 | 
36 | 
37 | 
38 |     .logo-header-container {
39 |           z-index: 10;
40 |           position: relative;
41 |           height: 160px;
42 |           width: 100%;
43 |           background-color: #063800;
44 |           display: flex;
45 |           align-items: center; /* Align items vertically */
46 |           justify-content: center; /* Center items horizontally */
47 |           gap: 20px; /* Add spacing between logo and text */
48 |           box-shadow: 0px 4px 15px rgba(20, 80, 20, 0.6);
49 |           text-align: center;
50 |         }
51 | 
52 | 
53 |     .logo {
54 |           max-height: 100px;
55 |           width: auto;
56 |         }
57 | 
58 | 
59 |     .div1 {
60 |           display: flex;
61 |           flex-direction: column; /* Stack heading and phrase */
62 |           align-items: center;
63 |           justify-content: center;
64 |         }
65 | 
66 |     .catchy-phrase {
67 |           color: white;
68 |           font-size: 20px;
69 |           margin-top: 5px; /* Adjust spacing between header and phrase */
70 |         }
71 | 
72 |     .hamburger-icon {
73 |               font-size: 30px;
74 |               color: white;
75 |               cursor: pointer;
76 |               position: absolute;
77 |               top: 20px;
78 |               left: 20px;
79 |               z-index: 100;
80 |           }
81 | 
82 | 
83 |     .report-container {
84 |               color: #1C1C1C;
85 |               display: flex;
86 |               padding: 10px;
87 |               gap: 30px;
88 |               align-items: center;
89 |               justify-content: center;
90 |               margin-bottom: 30px;
91 |           }
92 | 
93 |     .sidebar1 {
94 |               display: flex;
95 |               flex-direction: column;
96 |               align-items: center;
97 |               justify-content: center;
98 |               border: 1px solid #ccc;
99 |               border-radius: 8px;
100 |               margin-left: 50px;
101 |               float: left;
102 |               width: 250px;
103 |               height: 150px;
104 |               padding: 20px;
105 |               background-color: white;
106 |               color: white;
107 |               z-index: 1000;
108 | 
109 |           }
110 | 
111 | 
112 |     .navigation {
113 |       position: fixed; /* Sticks to the side */
114 |       left: 0;
115 |       top: 0;
116 |       width: 100px;
117 |       height: 100vh; /* 100% of the viewport height */
118 |       background:  #063800;
119 |       box-shadow: 25px 25px 75px rgba(0,0,0,0.25), 10px 10px 70px rgba(0,0,0,0.25),
120 |                   inset 5px 5px 10px rgba(0,0,0,0.5), inset 5px 5px 20px rgba(255,255,255,0.2),
121 |                   inset -5px -5px 15px rgba(0,0,0,0.75);
122 |       display: flex;
123 |       justify-content: center;
124 |       align-items: center;
125 |       flex-direction: column;
126 |       gap: 10px;
127 |       transform: translateX(-100%);
128 |       transition: transform 0.3s ease;
129 |     }
130 | 
131 | 
132 |    /* Class to toggle menu visibility */
133 |    .navigation.show {
134 |               transform: translateX(0);
135 |    }
136 | 
137 | 
138 | 
139 |    .navigation li {
140 |               position:relative;
141 |               list-style:none;
142 |               width:80px;
143 |               height: 80px;
144 |               display:flex;
145 |               justify-content:center;
146 |               margin: 0 5px;
147 |           }
148 | 
149 | 
150 |    .navigation li::before {
151 |               content: '';
152 |               position: absolute;
153 |               top:calc(50% - 2.5px);
154 |               left: 20px;
155 |               width:5px;
156 |               height: 5px;
157 |               border-radius:50%;
158 |               transition:0.5s;
159 | 
160 |           }
161 | 
162 | 
163 |    .navigation li.active::before {
164 |               background:white;
165 |               box-shadow:0 0 5px white,
166 |               0 0 10px white,
167 |               0 0 20px white,
168 |               0 0 30px white,
169 |               0 0 40px white;
170 |           }
171 | 
172 | 
173 | 
174 | 
175 |    .navigation li a {
176 |               display:flex;
177 |               justify-content:center;
178 |               align-items:center;
179 |               flex-direction:column;
180 |               text-decoration:none;
181 |           }
182 | 
183 | 
184 | 
185 | 
186 |    .navigation li a .icon {
187 |               color: white;
188 |               transition: 0.5s;
189 |               transition-delay: 0.2s;
190 |               font-size: 1.5em;
191 |           }
192 | 
193 | 
194 | 
195 | 
196 |    .navigation li.active a .icon::before{
197 |               transform:scale(1);
198 | 
199 |           }
200 | 
201 | 
202 | 
203 | 
204 |    .navigation li a .text{
205 |               position: absolute;
206 |               left:130px;
207 |               font-size:1.25em;
208 |               color:white;
209 |               visibility:hidden;
210 |               transition:0.5s;
211 |           }
212 | 
213 | 
214 | 
215 | 
216 |    .navigation li a .text::before {
217 |               content: '';
218 |               position: absolute;
219 |               top: 50%;
220 |               left: -4px;
221 |               transform:translateY(-50%) rotate(45deg);
222 |               width:10px;
223 |               height:10px;
224 |           }
225 | 
226 | 
227 | 
228 | 
229 |    .navigation li:hover a .text {
230 |               visibility: visible;
231 |           }
232 | 
233 | 
234 |    .logout {
235 |             z-index: 15;
236 |             position: absolute;
237 |             top: 20px;
238 |             right: 20px;
239 |             background-color: white;
240 |             color:  #063800;
241 |             border: none;
242 |             padding: 20px 35px;
243 |             border-radius: 4px;
244 |             font-size: 16px;
245 |             cursor: pointer;
246 |           }
247 | 
248 |    .logout:hover {
249 |              background-color: #145a32;
250 |             color: white;
251 |     }
252 | 
253 | 
254 |     h1 {
255 |         color: var(--primary-green);
256 |         margin-top: 0;
257 |         font-weight: 600;
258 |         margin-bottom: 25px;
259 |         font-size: 2.2em;
260 |         letter-spacing: -0.5px;
261 |       }
262 | 
263 | 
264 |     h2 {
265 |         color: var(--primary-green);
266 |         font-weight: 600;
267 |         font-size: 1.6em;
268 |         margin-bottom: 20px;
269 |         padding-bottom: 10px;
270 |         border-bottom: 2px solid #e0f0e0;
271 |       }
272 | 
273 | 
274 |     .column {
275 |         float: left;
276 |         width: 45%;
277 |         margin: 1%;
278 |         background: white;
279 |         border-radius: 12px;
280 |         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05), 0 1px 3px rgba(0, 0, 0, 0.1);
281 |         padding: 25px;
282 |         box-sizing: border-box;
283 |         min-height: 400px;
284 |         transition: transform 0.3s ease, box-shadow 0.3s ease;
285 |       }
286 | 
287 | 
288 |     .column:hover {
289 |         transform: translateY(-5px);
290 |         box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
291 |       }
292 | 
293 | 
294 | 
295 |     #raw-markdown {
296 |         display: none;
297 |       }
298 | 
299 | 
300 |       #rendered-tables table {
301 |         border-collapse: collapse;
302 |         width: 100%;
303 |         margin: 20px 0;
304 |         border-radius: 8px;
305 |         overflow: hidden;
306 |         box-shadow: 0 1px 3px rgba(0,0,0,0.05);
307 |       }
308 | 
309 | 
310 |       #rendered-tables th,
311 |       #rendered-tables td {
312 |         border: 1px solid #e0f0e0;
313 |         padding: 12px;
314 |         text-align: left;
315 |       }
316 | 
317 | 
318 |       #rendered-tables th {
319 |         background-color: var(--secondary-green);
320 |         color: white;
321 |         font-weight: 600;
322 |         text-transform: uppercase;
323 |         font-size: 0.9em;
324 |         letter-spacing: 0.5px;
325 |       }
326 | 
327 | 
328 |       /* Chart box wrapper */
329 |       .chart-box {
330 |         border: 1px solid #d4edd4;
331 |         background: linear-gradient(to bottom, #f9fff9, #ffffff);
332 |         border-radius: 12px;
333 |         padding: 0;
334 |         margin-bottom: 25px;
335 |         overflow: hidden;
336 |         box-shadow: 0 3px 6px rgba(0,0,0,0.05);
337 |       }
338 | 
339 | 
340 |       .chart-box h3 {
341 |         background: var(--primary-green);
342 |         color: white;
343 |         margin: 0;
344 |         padding: 15px;
345 |         font-size: 1.1em;
346 |         text-transform: uppercase;
347 |         letter-spacing: 0.5px;
348 |       }
349 | 
350 | 
351 |       /* RAG status styling */
352 |       #rag-status {
353 |         background: var(--accent-green);
354 |         padding: 10px 15px;
355 |         border-radius: 6px;
356 |         color: var(--primary-green);
357 |         font-weight: 600;
358 |         display: flex;
359 |         align-items: center;
360 |         gap: 10px;
361 |       }
362 | 
363 | 
364 |       #rag-status::before {
365 |         content: '';
366 |         width: 12px;
367 |         height: 12px;
368 |         border-radius: 50%;
369 |         background: var(--secondary-green);
370 |         display: inline-block;
371 |       }
372 | 
373 | 
374 |       /* Form styling */
375 |       form {
376 |         background: #fff;
377 |         padding: 20px;
378 |         border-radius: 8px;
379 |         box-shadow: 0 2px 10px rgba(0,0,0,0.05);
380 |         margin-bottom: 30px;
381 |       }
382 |       .search-container {
383 |        display: flex;
384 |        align-items: center;
385 |        justify-content: center;
386 |        gap: 10px;
387 |       }
388 | 
389 | 
390 |       .search-container label {
391 |        font-size: 1.2em;
392 |        color: #1C1C1C;;
393 |       }
394 |        #company_input {
395 |         width: 95%;
396 |         padding: 12px;
397 |         border: 2px solid #d4edd4;
398 |         border-radius: 6px;
399 |         margin-bottom: 15px;
400 |         transition: border-color 0.3s ease;
401 |         font-size: 1.2em;
402 |       }
403 | 
404 | 
405 |       #submit-btn {
406 |         background: linear-gradient(to right, var(--secondary-green), var(--primary-green));
407 |         padding: 12px 25px;
408 |         font-weight: 600;
409 |         text-transform: uppercase;
410 |         letter-spacing: 0.5px;
411 |         color: #fff;
412 |         border: none;
413 |         border-radius: 4px;
414 |         cursor: pointer;
415 |         transition: transform 0.2s ease;
416 |         font-size: 1.2em;
417 |       }
418 | 
419 | 
420 |       #submit-btn:hover {
421 |         transform: scale(1.02);
422 |       }
423 | 
424 | 
425 |       /* Chat form styling */
426 |       #question-form {
427 |         display: flex;
428 |         gap: 10px;
429 |         margin-top: 15px;
430 |       }
431 | 
432 | 
433 |       #question-input {
434 |         flex: 1;
435 |         padding: 12px;
436 |         border: 2px solid #d4edd4;
437 |         border-radius: 8px;
438 |         font-size: 1em;
439 |         transition: all 0.3s ease;
440 |       }
441 | 
442 | 
443 |       #question-input:focus {
444 |         outline: none;
445 |         border-color: #70c270;
446 |       }
447 | 
448 | 
449 |       #question-form button {
450 |         background: var(--secondary-green);
451 |         color: #fff;
452 |         border: none;
453 |         border-radius: 4px;
454 |         padding: 12px 20px;
455 |         font-weight: 600;
456 |         cursor: pointer;
457 |         transition: background 0.3s ease;
458 |       }
459 | 
460 | 
461 |       #question-form button:hover {
462 |         background-color: var(--primary-green);
463 |       }
464 | 
465 | 
466 |       /* Chat Q&A bubbles */
467 |       #chat-output {
468 |         margin-top: 15px;
469 |       }
470 | 
471 | 
472 |       #chat-output div {
473 |         background-color: #e9ffe9;
474 |         border: 1px solid #c7edc7;
475 |         margin-bottom: 10px;
476 |         padding: 10px;
477 |         border-radius: 4px;
478 |         white-space: normal;
479 |       }
480 | 
481 | 
482 |       #chat-output table {
483 |         border-collapse: collapse;
484 |         width: 100%;
485 |         margin: 10px 0;
486 |       }
487 | 
488 | 
489 |       #chat-output th,
490 |       #chat-output td {
491 |         border: 1px solid #d4edd4;
492 |         padding: 8px;
493 |         text-align: left;
494 |       }
495 | 
496 | 
497 |       #chat-output th {
498 |         background-color: #f1f9f1;
499 |       }
500 | 
501 | 
502 |       /* Loading spinner */
503 |       #loading-spinner {
504 |         display: none;
505 |         text-align: center;
506 |         margin: 30px 0;
507 |       }
508 | 
509 | 
510 |       .spinner {
511 |         width: 40px;
512 |         height: 40px;
513 |         margin: 0 auto;
514 |         border: 4px solid #f3f3f3;
515 |         border-top: 4px solid var(--secondary-green);
516 |         border-radius: 50%;
517 |         animation: spin 1s linear infinite;
518 |       }
519 | 
520 | 
521 |       @keyframes spin {
522 |         0% { transform: rotate(0deg); }
523 |         100% { transform: rotate(360deg); }
524 |       }
525 | 
526 | 
527 |       .clear { clear: both; }
528 |     </style>
529 | </head>
530 | <body>
531 | 
532 | 
533 |  <div class="logo-header-container">
534 |    <img src="{{ url_for('static', filename='images/missiTrack.png') }}" alt="Logo" class="logo">
535 |    <div class="div1">
536 |        <h1 style="color:white; text-align:center;"> EmissiTrack</h1>
537 |        <p class="catchy-phrase">Advanced Search</p>
538 |    </div>
539 | </div>
540 | 
541 | 
542 | <div class="hamburger-icon">&#9776;</div>
543 |        <ul class="navigation">
544 |            <li class="active">
545 |                <a href="{{url_for('firstpage')}}">
546 |                    <span class="icon"> <ion-icon name="home-outline"></ion-icon></span>
547 |                    <span class="text">EmissiTrack</span>
548 |                </a>
549 |            </li>
550 |            <li>
551 |                <a href="{{url_for('advanced_search')}}">
552 |                    <span class="icon"> <ion-icon name="information-circle-outline"></ion-icon></span>
553 |                    <span class="text">Advanced Search</span>
554 |                </a>
555 |            </li>
556 |            <li>
557 |                <a href="{{url_for('home')}}">
558 |                    <span class="icon"> <ion-icon name="finger-print-outline"></ion-icon></span>
559 |                    <span class="text">Premium Page</span>
560 |                </a>
561 |            </li>
562 |            <li>
563 |                <a href="{{url_for('login')}}">
564 |                    <span class="icon"><ion-icon name="settings-outline"></ion-icon></span>
565 |                    <span class="text">Register/Login</span>
566 |                </a>
567 |            </li>
568 |            <li>
569 |                <a href="{{url_for('firstpage')}}">
570 |                    <span class="icon"><ion-icon name="log-out-outline"></ion-icon></span>
571 |                    <span class="text">Logout</span>
572 |                </a>
573 |            </li>
574 |        </ul>
575 |        <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
576 |            <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
577 |            <script>
578 |                document.addEventListener('DOMContentLoaded', function () {
579 |                    const hamburger = document.querySelector('.hamburger-icon');
580 |                    const navigation = document.querySelector('.navigation');
581 |                    let isOpen = false;
582 |                    hamburger.addEventListener('click', function () {
583 |                        // Toggle menu visibility
584 |                        isOpen = !isOpen;
585 |                        if (isOpen) {
586 |                            navigation.classList.add('show');
587 |                        } else {
588 |                            navigation.classList.remove('show');
589 |                        }
590 |                    });
591 |                    // Keep your existing navigation item click event listener
592 |                    let list = document.querySelectorAll('.navigation li');
593 |                    function activeLink() {
594 |                        list.forEach((item) => item.classList.remove('active'));
595 |                        this.classList.add('active');
596 |                    }
597 |                    list.forEach((item) => item.addEventListener('click', activeLink));
598 |                });
599 |            </script>
600 |  <div class="content">
601 |  <!-- Add search form at the top -->
602 |  <form method="POST" style="margin-bottom: 20px;">
603 |    <div class="search-container">
604 |    <label for="company_input">Enter Company, ISIN, or Ticker:</label>
605 |    <input type="text" id="company_input" name="company_name" required>
606 | 
607 | 
608 |    <label style="margin-left: 10px;"></label>
609 |    <label>
610 |      <input type="radio" name="idType" value="name" checked> Name
611 |    </label>
612 |    <label>
613 |      <input type="radio" name="idType" value="ticker"> Ticker
614 |    </label>
615 |    <label>
616 |      <input type="radio" name="idType" value="isin"> ISIN
617 |    </label>
618 |    <br><br>
619 |    <button type="submit" id="submit-btn">Search</button>
620 |  </div>
621 |  </form>
622 | 
623 | 
624 |  <!-- Updated loading spinner (initially hidden by CSS) -->
625 |  <div id="loading-spinner">
626 |    <div class="spinner"></div>
627 |    <p>Analyzing ESG Data...</p>
628 |  </div>
629 | 
630 | 
631 |  <!-- Wrap existing content in conditional -->
632 |  {% if company_name %}
633 |    <h1>
634 |      <i class="fas fa-leaf"></i>
635 |      ESG Insights: {{ company_name }}
636 |    </h1>
637 |  {% else %}
638 |    <h1>
639 |      <i class="fas fa-search"></i>
640 |      Discover ESG Analytics
641 |    </h1>
642 |  {% endif %}
643 | 
644 | 
645 |  {% if company_name %}
646 | 
647 | 
648 | 
649 | 
650 |  <div class="report-container">
651 |    {% if report_url %}
652 |        <p>Latest ESG Report Link for {{company_name}}: <a href="{{ report_url }}" target="_blank">{{ report_url }}</a></p>
653 | 
654 | 
655 | 
656 | 
657 |    {% else %}
658 |        <p>No report found.</p>
659 |    {% endif %}
660 | </div>
661 | 
662 | 
663 |    <!-- Left column: LLM data (tables) -->
664 |    <div class="column">
665 |      <h2>GHG Emissions Tables (tCO2e) 🌱</h2>
666 | 
667 | 
668 |      <!-- Hidden raw markdown from the LLM -->
669 |      <div id="raw-markdown">{{ llm_markdown }}</div>
670 | 
671 | 
672 |      <!-- We'll display the rendered HTML tables here -->
673 |      <div id="rendered-tables"></div>
674 |    </div>
675 | 
676 | 
677 |    <!-- Right column: Chart + RAG chatbot -->
678 |    <div class="column">
679 |      <!-- Chart box above the chatbot -->
680 |      <div class="chart-box">
681 |        <h3>Emissions Over Time</h3>
682 |        <canvas id="keyTableChart" width="300" height="200"></canvas>
683 |      </div>
684 | 
685 | 
686 |      <h2>Chatbot 🌍</h2>
687 |      <div id="rag-status">Initializing RAG...</div>
688 | 
689 | 
690 |      <form id="question-form">
691 |        <input type="text" id="question-input" name="question" placeholder="Type your question..." />
692 |        <button type="submit">Ask</button>
693 |      </form>
694 | 
695 | 
696 |      <!-- Add this STOP button (it doesn't belong to the question-form) -->
697 |      <button type="button" id="stop-rag-btn" style="margin-left: 10px; background-color: #f44336; color: white; border: none; border-radius: 4px; padding: 7px 12px;">
698 |        Stop RAG
699 |      </button>
700 | 
701 | 
702 |      <div id="chat-output"></div>
703 |    </div>
704 | 
705 | 
706 |    <div class="clear"></div>
707 |  {% endif %}
708 | 
709 | 
710 |  <script>
711 |    // Immediately call /rag_init in the background
712 |    fetch("{{ url_for('rag_init') }}", { method: "POST" })
713 |      .then(resp => resp.json())
714 |      .then(data => {
715 |        console.log("RAG init response:", data);
716 |        // Show the user that something is happening
717 |        const ragStatusEl = document.getElementById("rag-status");
718 |        ragStatusEl.innerText = data.status; // e.g. "RAG initialization started"
719 | 
720 | 
721 |        // Now poll /rag_status every 5 seconds instead of 2
722 |        const checkInterval = setInterval(() => {
723 |          fetch("{{ url_for('rag_status') }}")
724 |            .then(r => r.json())
725 |            .then(rd => {
726 |              if (rd.initialized) {
727 |                ragStatusEl.innerText = "RAG is ready!";
728 |                clearInterval(checkInterval); // stop polling
729 |              } else {
730 |                ragStatusEl.innerText = "RAG is still initializing...";
731 |              }
732 |            })
733 |            .catch(err => {
734 |              console.error("Error checking RAG status:", err);
735 |              // If there's an error talking to /rag_status, you can handle it here
736 |            });
737 |        }, 5000); // Changed from 2000 to 5000 milliseconds
738 |      })
739 |      .catch(err => {
740 |        console.error("RAG init error:", err);
741 |        document.getElementById("rag-status").innerText = "Error initializing RAG";
742 |      });
743 | 
744 | 
745 |    window.addEventListener('DOMContentLoaded', () => {
746 |      let rawMarkdown = document.getElementById('raw-markdown')?.textContent || "";
747 | 
748 | 
749 |      // 1) Remove code fences
750 |      rawMarkdown = rawMarkdown.replaceAll("```markdown", "").replaceAll("```", "");
751 | 
752 | 
753 |      // 2) Parse the Key Table for the chart (long format)
754 |      const keyTableData = parseKeyTableFromMarkdown(rawMarkdown);
755 |      renderKeyTableChart(keyTableData);
756 | 
757 | 
758 |      // 3) Parse and pivot each of the five tables
759 |      const pivotedKey = pivotTableData(keyTableData, 'category', 'year', 'emissions');
760 | 
761 |      const scope1Data = parseBreakdownFromMarkdown(rawMarkdown, "Scope 1 Breakdown");
762 |      const pivotedScope1 = pivotTableData(scope1Data, 'subcategory', 'year', 'emissions');
763 | 
764 | 
765 |      const scope2MarketData = parseBreakdownFromMarkdown(rawMarkdown, "Scope 2 Market-based Breakdown");
766 |      const pivotedScope2M = pivotTableData(scope2MarketData, 'subcategory', 'year', 'emissions');
767 | 
768 | 
769 |      const scope2LocationData = parseBreakdownFromMarkdown(rawMarkdown, "Scope 2 Location-based Breakdown");
770 |      const pivotedScope2L = pivotTableData(scope2LocationData, 'subcategory', 'year', 'emissions');
771 | 
772 | 
773 |      const scope3Data = parseBreakdownFromMarkdown(rawMarkdown, "Scope 3 Breakdown");
774 |      const pivotedScope3 = pivotTableData(scope3Data, 'subcategory', 'year', 'emissions');
775 | 
776 | 
777 |      // 4) Build HTML tables
778 |      let html = "";
779 |      html += "<h3>Summary</h3>";
780 |      html += buildHtmlTable(pivotedKey, "Category");
781 | 
782 | 
783 |      html += "<h3>Scope 1 Breakdown</h3>";
784 |      html += buildHtmlTable(pivotedScope1, "Scope 1 Source / Subcategory");
785 | 
786 | 
787 |      html += "<h3>Scope 2 Market-based Breakdown</h3>";
788 |      html += buildHtmlTable(pivotedScope2M, "Region or Business Unit");
789 | 
790 | 
791 |      html += "<h3>Scope 2 Location-based Breakdown</h3>";
792 |      html += buildHtmlTable(pivotedScope2L, "Region or Business Unit");
793 | 
794 | 
795 |      html += "<h3>Scope 3 Breakdown</h3>";
796 |      html += buildHtmlTable(pivotedScope3, "Scope 3 Category");
797 | 
798 | 
799 |      document.getElementById('rendered-tables').innerHTML = html;
800 | 
801 | 
802 |      // Add chart annotations
803 |      Chart.register(ChartjsPluginAnnotation);
804 | 
805 | 
806 |      // Add smooth scroll to tables
807 |      document.querySelectorAll('#rendered-tables table').forEach(table => {
808 |        table.addEventListener('mouseover', () => {
809 |          table.style.transform = 'scale(1.02)';
810 |          table.style.transition = 'transform 0.3s ease';
811 |        });
812 |        table.addEventListener('mouseout', () => {
813 |          table.style.transform = 'scale(1)';
814 |        });
815 |      });
816 | 
817 | 
818 |      // Real-time chart resizing via ResizeObserver
819 |      const chartCanvas = document.getElementById('keyTableChart');
820 |      if (chartCanvas) {
821 |        const resizeObserver = new ResizeObserver(entries => {
822 |          entries.forEach(entry => {
823 |            const chart = Chart.getChart(chartCanvas);
824 |            if (chart) {
825 |              chart.resize();
826 |            }
827 |          });
828 |        });
829 |        resizeObserver.observe(chartCanvas.parentElement);
830 |      }
831 |    });
832 | 
833 | 
834 |    function pivotTableData(longData, rowField, colField, valField) {
835 |      const rowLabels = [...new Set(longData.map(d => d[rowField]))];
836 |      const colLabels = [...new Set(longData.map(d => d[colField]))].sort();
837 | 
838 | 
839 |      const lookup = {};
840 |      longData.forEach(item => {
841 |        const r = item[rowField];
842 |        const c = item[colField];
843 |        lookup[`${r}-${c}`] = item[valField];
844 |      });
845 | 
846 | 
847 |      const pivoted = rowLabels.map(rLabel => {
848 |        let rowObj = { rowLabel: rLabel };
849 |        colLabels.forEach(cLabel => {
850 |          rowObj[cLabel] = lookup[`${rLabel}-${cLabel}`] ?? null;
851 |        });
852 |        return rowObj;
853 |      });
854 | 
855 | 
856 |      return { rowLabels, colLabels, pivoted };
857 |    }
858 | 
859 | 
860 |    function buildHtmlTable(pivotResult, rowName = "Category") {
861 |      const { pivoted, colLabels } = pivotResult;
862 |      let html = '<table><thead><tr><th>' + rowName + '</th>';
863 |      colLabels.forEach(yr => {
864 |        html += `<th>${yr}</th>`;
865 |      });
866 |      html += '</tr></thead><tbody>';
867 | 
868 | 
869 |      pivoted.forEach(row => {
870 |        html += `<tr><td>${row.rowLabel}</td>`;
871 |        colLabels.forEach(yr => {
872 |          let val = row[yr] !== null ? row[yr] : '';
873 |          html += `<td>${val}</td>`;
874 |        });
875 |        html += '</tr>';
876 |      });
877 |      html += '</tbody></table>';
878 |      return html;
879 |    }
880 | 
881 | 
882 |    function parseBreakdownFromMarkdown(md, headingName) {
883 |      let lines = md.split('\n');
884 |      let foundHeading = false;
885 |      let result = [];
886 | 
887 | 
888 |      for (let i = 0; i < lines.length; i++) {
889 |        let line = lines[i].trim();
890 | 
891 | 
892 |        // Case-insensitive check for the heading name
893 |        if (line.toLowerCase().includes(headingName.toLowerCase())) {
894 |          foundHeading = true;
895 |          continue;
896 |        }
897 | 
898 | 
899 |        if (foundHeading) {
900 |          // If we see a new heading (# up to ######), we stop
901 |          if (line.match(/^#{1,6}\s/)) {
902 |            break;
903 |          }
904 | 
905 | 
906 |          if (line.startsWith("|") && line.endsWith("|")) {
907 |            if (line.includes("|---")) continue;
908 | 
909 | 
910 |            let cols = line.split("|").map(c => c.trim()).filter(Boolean);
911 |            if (cols.length < 3) continue;
912 |            let lower = cols.join(" ").toLowerCase();
913 |            if (lower.includes("year") && lower.includes("emissions")) {
914 |              continue;
915 |            }
916 | 
917 | 
918 |            let subcategory = cols[0];
919 |            let yearStr = cols[1].toUpperCase();
920 |            let match = yearStr.match(/\d{4}|\d{2}/);
921 |            let year = null;
922 |            if (match) {
923 |              let num = parseInt(match[0]);
924 |              if (num < 50) year = 2000 + num;
925 |              else if (num < 100) year = 1900 + num;
926 |              else year = num;
927 |            }
928 | 
929 | 
930 |            let eStr = cols[2].replace(/[^\d.-]/g,'');
931 |            let emissions = parseFloat(eStr);
932 |            if (isNaN(emissions)) emissions = 0;
933 | 
934 | 
935 |            result.push({ subcategory, year, emissions });
936 |          }
937 |        }
938 |      }
939 |      return result;
940 |    }
941 | 
942 | 
943 |    // Modified question form handler
944 |    document.getElementById("question-form")?.addEventListener("submit", function(e) {
945 |      e.preventDefault();
946 |      const questionInput = document.getElementById("question-input");
947 |      const question = questionInput.value.trim();
948 |      if (!question) return;
949 | 
950 | 
951 |      // Show immediate feedback
952 |      const outputDiv = document.getElementById("chat-output");
953 |      const waitingMsg = document.createElement("div");
954 |      waitingMsg.innerHTML = "<em>Processing your question, please wait...</em>";
955 |      outputDiv.appendChild(waitingMsg);
956 | 
957 | 
958 |      // Disable the ASK button so user knows it's "in progress"
959 |      const askButton = this.querySelector("button[type='submit']");
960 |      askButton.disabled = true;
961 | 
962 | 
963 |      const formData = new FormData();
964 |      formData.append("question", question);
965 | 
966 | 
967 |      fetch("{{ url_for('ask_question') }}", {
968 |        method: "POST",
969 |        body: formData
970 |      })
971 |        .then(resp => resp.json())
972 |        .then(data => {
973 |          // Remove the "waiting" message
974 |          outputDiv.removeChild(waitingMsg);
975 |          // Re-enable the ASK button
976 |          askButton.disabled = false;
977 | 
978 | 
979 |          let newQA = document.createElement("div");
980 |          // Clean out triple backticks
981 |          let cleanAnswer = data.answer.replaceAll("```markdown", "").replaceAll("```", "");
982 |          // Convert markdown to HTML
983 |          let htmlAnswer = marked.parse(cleanAnswer);
984 | 
985 | 
986 |          newQA.innerHTML = `
987 |            <b>Q:</b> ${question}<br>
988 |            <b>A:</b> ${htmlAnswer}
989 |          `;
990 |          outputDiv.appendChild(newQA);
991 |        })
992 |        .catch(err => {
993 |          console.error("Ask error:", err);
994 |          // Remove "waiting" message
995 |          outputDiv.removeChild(waitingMsg);
996 |          // Re-enable the button
997 |          askButton.disabled = false;
998 | 
999 | 
1000 |          const newQA = document.createElement("div");
1001 |          newQA.innerHTML = `
1002 |            <b>Q:</b> ${question}<br>
1003 |            <b>A:</b> Sorry, there was an error. Please try again.
1004 |          `;
1005 |          outputDiv.appendChild(newQA);
1006 |        });
1007 |    });
1008 | 
1009 | 
1010 |    function parseKeyTableFromMarkdown(md) {
1011 |      let lines = md.split('\n');
1012 |      let inKeyTable = false;
1013 |      let entries = [];
1014 | 
1015 | 
1016 |      for (let i = 0; i < lines.length; i++) {
1017 |        let line = lines[i].trim();
1018 | 
1019 | 
1020 |        // 1) Detect "Key Table" (case-insensitive)
1021 |        if (!inKeyTable && line.toLowerCase().includes("key table")) {
1022 |          inKeyTable = true;
1023 |          continue;
1024 |        }
1025 |        // 2) If we've found Key Table and see a new heading (# up to ######), we stop
1026 |        if (inKeyTable && line.match(/^#{1,6}\s/)) {
1027 |          break;
1028 |        }
1029 | 
1030 | 
1031 |        // 3) If inKeyTable, gather table rows
1032 |        if (inKeyTable && line.startsWith("|") && line.endsWith("|")) {
1033 |          // skip lines like "|---"
1034 |          if (line.includes("|---")) continue;
1035 | 
1036 | 
1037 |          // split columns
1038 |          let cols = line.split("|").map(c => c.trim()).filter(Boolean);
1039 |          if (cols.length < 3) continue; // not enough columns
1040 | 
1041 | 
1042 |          // skip header row
1043 |          let lower = cols.join(" ").toLowerCase();
1044 |          if (lower.includes("category") && lower.includes("year")) {
1045 |            continue;
1046 |          }
1047 | 
1048 | 
1049 |          // parse category
1050 |          let category = cols[0];
1051 | 
1052 | 
1053 |          // parse year
1054 |          let yearStr = cols[1].toUpperCase();
1055 |          let match = yearStr.match(/\d{4}|\d{2}/);
1056 |          let year = null;
1057 |          if (match) {
1058 |            let num = parseInt(match[0]);
1059 |            // Example logic for 2-digit years
1060 |            if (num < 50) year = 2000 + num;
1061 |            else if (num < 100) year = 1900 + num;
1062 |            else year = num;
1063 |          }
1064 |          if (!year) {
1065 |            continue;
1066 |          }
1067 | 
1068 | 
1069 |          // parse emissions
1070 |          let emissStr = cols[2];
1071 |          let cleaned = emissStr.replace(/[^\d.-]/g, '');
1072 |          let emissions = parseFloat(cleaned);
1073 |          if (isNaN(emissions)) emissions = 0;
1074 | 
1075 | 
1076 |          entries.push({ category, year, emissions });
1077 |        }
1078 |      }
1079 |      return entries;
1080 |    }
1081 | 
1082 | 
1083 |    function renderKeyTableChart(data) {
1084 |      if (!data || data.length === 0) {
1085 |        console.log("No Key Table data found to chart.");
1086 |        return;
1087 |      }
1088 | 
1089 | 
1090 |      let categories = {
1091 |        "Scope 1": [],
1092 |        "Scope 2 (Market-based)": [],
1093 |        "Scope 2 (Location-based)": []
1094 |      };
1095 | 
1096 | 
1097 |      data.forEach(entry => {
1098 |        if (categories.hasOwnProperty(entry.category) && entry.year && entry.emissions !== null) {
1099 |          categories[entry.category].push({ x: entry.year, y: entry.emissions });
1100 |        }
1101 |      });
1102 | 
1103 | 
1104 |      Object.keys(categories).forEach(cat => {
1105 |        categories[cat].sort((a,b) => a.x - b.x);
1106 |      });
1107 | 
1108 | 
1109 |      const chartDatasets = [];
1110 |      const colorMap = {
1111 |        "Scope 1": "#26c6da",
1112 |        "Scope 2 (Market-based)": "#ef5350",
1113 |        "Scope 2 (Location-based)": "#66bb6a"
1114 |      };
1115 | 
1116 | 
1117 |      for (let cat of Object.keys(categories)) {
1118 |        if (categories[cat].length > 0) {
1119 |          chartDatasets.push({
1120 |            label: cat,
1121 |            data: categories[cat],
1122 |            backgroundColor: colorMap[cat] || "#888",
1123 |            borderColor: colorMap[cat] || "#888",
1124 |            borderWidth: 1,
1125 |            borderRadius: 4
1126 |          });
1127 |        }
1128 |      }
1129 | 
1130 | 
1131 |      const ctx = document.getElementById('keyTableChart').getContext('2d');
1132 |      new Chart(ctx, {
1133 |        type: 'bar',
1134 |        data: { datasets: chartDatasets },
1135 |        options: {
1136 |          scales: {
1137 |            x: {
1138 |              type: 'linear',
1139 |              title: { display: true, text: 'Year' },
1140 |              ticks: {
1141 |                stepSize: 1,
1142 |                callback: function(value) {
1143 |                  return value;
1144 |                }
1145 |              }
1146 |            },
1147 |            y: {
1148 |              title: {
1149 |                display: true,
1150 |                text: 'Emissions (tCO2e)'
1151 |              }
1152 |            }
1153 |          },
1154 |          plugins: {
1155 |            title: {
1156 |              display: false
1157 |            }
1158 |          }
1159 |        }
1160 |      });
1161 |    }
1162 |    /* ================================================================ */
1163 | 
1164 | 
1165 |    document.addEventListener('DOMContentLoaded', function() {
1166 |      // STOP RAG button
1167 |      const stopButton = document.getElementById('stop-rag-btn');
1168 |      if (stopButton) {
1169 |        stopButton.addEventListener('click', function() {
1170 |          fetch("{{ url_for('reset_rag') }}", {
1171 |            method: "POST"
1172 |          })
1173 |          .then(resp => resp.json())
1174 |          .then(data => {
1175 |            console.log("Stop RAG response:", data);
1176 |            document.getElementById('rag-status').innerText = "RAG reset.";
1177 |          })
1178 |          .catch(err => console.error("Error stopping RAG:", err));
1179 |        });
1180 |      }
1181 |    });
1182 |  </script>
1183 |   </div>
1184 | </body>
1185 | </html>
1186 | 
```

src/templates/instructions.html
```
1 | <!DOCTYPE html>
2 | <html lang="en">
3 | <head>
4 |   <meta charset="UTF-8">
5 |   <meta http-equiv="X-UA-Compatible" content="IE=edge">
6 |   <meta name="viewport" content="width=device-width, initial-scale=1.0">
7 |   <title>Emissions Report</title>
8 |   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
9 |   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
10 |   <style>
11 |       body {
12 |            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
13 |            background-color: #F5F5F5;
14 |            color: #333333;
15 |            margin: 0;
16 |            padding: 0;
17 |        }
18 | 
19 | 
20 | 
21 | 
22 |       table, th, td {
23 |            border: 1px solid black;
24 |       }
25 | 
26 | 
27 | 
28 | 
29 |       .content {
30 |          margin-left: 130px; /* Pushes content right */
31 |          padding: 20px;
32 |       }
33 | 
34 | 
35 | 
36 | 
37 |       .div1 {
38 |        z-index: 10; /* Ensures it appears above other elements */
39 |        position: relative; /* Required for z-index to work */
40 |           height: 160px;
41 |           width: 100%; /* Ensure it takes full width */
42 |           margin: 0;
43 |           background-color: #063800;
44 |           display: flex;
45 |           align-items: center; /* Centers vertically */
46 |           justify-content: center; /* Centers horizontally */
47 |           box-shadow: 0px 4px 15px rgba(20, 80, 20, 0.6);
48 |       }
49 |       .catchy-phrase {
50 |        z-index: 10;
51 |        position: absolute;
52 |        top: 120px;
53 |        transform: translate(-50%, -50%);
54 |        left: 50%;
55 |        color: white;
56 |        font-size: 20px;
57 | }
58 | 
59 | 
60 | 
61 | 
62 |       .navigation {
63 |           position: absolute;
64 |           left:0;
65 |           width:100px;
66 |           height:100%;
67 |           background:  #063800;
68 |           box-shadow: 25px 25px 75px rgba(0,0,0,0.25), 10px 10px 70px rgba(0,0,0,0.25), inset 5px 5px 10px rgba(0,0,0,0.5), inset 5px 5px 20px rgba(255,255,255,0.2) , inset -5px -5px 15px rgba(0,0,0,0.75);
69 |           display:center;
70 |           justify-content:center;
71 |           align-items:center;
72 |           flex-direction:column;
73 |           gap:10px;
74 |           transform: translateX(-100%);
75 |           transition: transform 0.3s ease;
76 | 
77 | 
78 | 
79 | 
80 |       }
81 | 
82 | 
83 |       /* Class to toggle menu visibility */
84 |       .navigation.show {
85 |           transform: translateX(0);
86 |       }
87 | 
88 | 
89 | 
90 | 
91 |       .navigation li {
92 |           position:relative;
93 |           list-style:none;
94 |           width:80px;
95 |           height: 80px;
96 |           display:flex;
97 |           justify-content:center;
98 |           margin: 0 5px;
99 | 
100 |       }
101 | 
102 | 
103 | 
104 | 
105 |       .navigation li::before {
106 |           content: '';
107 |           position: absolute;
108 |           top:calc(50% - 2.5px);
109 |           left: 20px;
110 |           width:5px;
111 |           height: 5px;
112 |           border-radius:50%;
113 |           transition:0.5s;
114 |       }
115 | 
116 | 
117 | 
118 | 
119 |       .navigation li.active::before {
120 |           background:white;
121 |           box-shadow:0 0 5px white,
122 |           0 0 10px white,
123 |           0 0 20px white,
124 |           0 0 30px white,
125 |           0 0 40px white;
126 |       }
127 | 
128 | 
129 | 
130 | 
131 |       .navigation li a {
132 |           display:flex;
133 |           justify-content:center;
134 |           align-items:center;
135 |           flex-direction:column;
136 |           text-decoration:none;
137 |       }
138 | 
139 | 
140 | 
141 | 
142 |       .navigation li a .icon {
143 |           color: white;
144 |           transition: 0.5s;
145 |           transition-delay: 0.2s;
146 |           font-size: 1.5em;
147 |       }
148 | 
149 | 
150 |       .navigation li.active a .icon::before{
151 |           transform:scale(1);
152 |       }
153 | 
154 | 
155 |       .navigation li a .text{
156 |           position: absolute;
157 |           left:130px;
158 |           font-size:1.25em;
159 |           color:white;
160 |           visibility:hidden;
161 |           transition:0.5s;
162 | 
163 |       }
164 | 
165 | 
166 |       .navigation li:hover a .text {
167 |           visibility: visible;
168 |       }
169 | 
170 | 
171 |       .hamburger-icon {
172 |           font-size: 30px;
173 |          color: white;
174 |          cursor: pointer;
175 |          position: absolute;
176 |          top: 20px;
177 |          left: 20px;
178 |          z-index: 100;
179 |          align-items: center;
180 |       }
181 | 
182 | 
183 | 
184 | 
185 |       .sidebar1 {
186 |           display: flex;
187 |          flex-direction: column;
188 |          align-items: center;
189 |          justify-content: center;
190 |          border: 1px solid #ccc;
191 |          border-radius: 8px;
192 |          margin-left: 50px;
193 |          margin-top: 40px;
194 |          float: left;
195 |          width: 250px;
196 |          height: 150px;
197 |          padding: 20px;
198 |          background-color: white;
199 |          color: white;
200 |          z-index: 1000;
201 |       }
202 | 
203 | 
204 | 
205 | 
206 |       .dropbtn {
207 |         background-color: white;
208 |            color:  #063800;
209 |            padding: 16px;
210 |            font-size: 16px;
211 |            border: none;
212 |           cursor: pointer;
213 |       }
214 | 
215 | 
216 | 
217 | 
218 |       /* The container <div> - needed to position the dropdown content */
219 |        .dropdown {
220 |        z-index: 15;
221 |         position: absolute;
222 |          top: 20px; /* Distance from the top */
223 |          right: 20px;
224 |            display: inline-block;
225 |            border: 1px solid white;
226 |            background-color: white;
227 |            border-radius: 12px;
228 |            padding: 4px 7px;
229 |              font-size: 16px;
230 |              cursor: pointer;
231 |              align-items: center;
232 |       }
233 | 
234 | 
235 | 
236 | 
237 |       /* Dropdown Content (Hidden by Default) */
238 |       .dropdown-content {
239 |            display: none;
240 |            padding: 5px 15px;
241 |            position: absolute;
242 |            font-size: 16px;
243 |            background-color:white;
244 |            min-width: 100px;
245 |            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
246 |            z-index: 1;
247 |       }
248 | 
249 | 
250 | 
251 | 
252 |       /* Links inside the dropdown */
253 |       .dropdown-content a {
254 |         color: black;
255 |         padding: 12px 16px;
256 |         text-decoration: none;
257 |         display: block;
258 |       }
259 | 
260 | 
261 | 
262 | 
263 |       /* Change color of dropdown links on hover */
264 |       .dropdown-content a:hover {background-color: #2e8b563d;}
265 | 
266 | 
267 | 
268 | 
269 |       /* Show the dropdown menu on hover */
270 |       .dropdown:hover .dropdown-content {display: block;}
271 | 
272 | 
273 | 
274 | 
275 |       /* Change the background color of the dropdown button when the dropdown content is shown */
276 |       .dropdown:hover .dropbtn {background-color: rgba(255, 255, 255, 0.607);}
277 | 
278 | 
279 | 
280 | 
281 |       .progress-bar {
282 |           background-color: #045000!important;/* This is the green color you used for other elements */
283 |       }
284 | 
285 | 
286 | 
287 | 
288 |       .selected-company {
289 |            background-color: white;
290 |            padding: 20px;
291 |            margin: 20px auto;
292 |            align-items: center;
293 |            justify-content: center;
294 |            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
295 |            border: 2px solid black;
296 |            display: inline-block;
297 |            width: 90%; /* Adjust width for better layout */
298 |            max-width: 1400px;
299 |         }
300 | 
301 | 
302 |         /* Table Styling */
303 |         .selected-company table {
304 |            width: 100%;
305 |            border-collapse: collapse;
306 |         }
307 | 
308 | 
309 |         .selected-company th, .selected-company td {
310 |            border: 1px solid black;
311 |            padding: 8px;
312 |            text-align: center;
313 |         }
314 | 
315 | 
316 |         .selected-company th {
317 |            background-color: #063800;
318 |            color: white;
319 |         }
320 | 
321 | 
322 |         /* Style the Download Button */
323 |         .selected-company a.btn-success {
324 |            display: block;
325 |            margin: 10px auto;
326 |            text-align: center;
327 |            background-color: #063800;
328 |            color: white;
329 |            padding: 10px 15px;
330 |            font-size: 16px;
331 |            border-radius: 5px;
332 |            text-decoration: none;
333 |            transition: background-color 0.3s ease;
334 |         }
335 | 
336 | 
337 |         .selected-company a.btn-success:hover {
338 |            background-color: #1E6B47;
339 |         }
340 | 
341 | 
342 |     .esg-container {
343 |              background-color: white;
344 |              display: flex;
345 |              padding: 10px;
346 |              gap: 30px;
347 |              align-items: center;
348 |              justify-content: center;
349 |              margin-bottom: 30px;
350 |          }
351 | 
352 | 
353 | 
354 |       .list-group-item {
355 |          width:1400px;
356 |          box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
357 |          border: 2px solid black; padding: 5px; display: inline-block;
358 |          background-color: white;
359 |          padding: 20px;
360 |          margin-left:20px;
361 |          align-items: center;
362 |          justify-content: center;
363 |       }
364 | 
365 | 
366 | 
367 | 
368 |       .dropdown-container {
369 |          background-color: #F5F5F5;
370 |          display: flex;
371 |          padding: 10px;
372 |          gap: 30px;
373 |          align-items: center;
374 |          justify-content: center;
375 |          margin-bottom: 30px;
376 |      }
377 |      .dropdown-container label{
378 |        color: #1C1C1C;
379 |      }
380 | 
381 | 
382 | 
383 | 
384 |      .nav-tabs .nav-link {
385 |           background-color: #063800 !important;
386 |           color: white !important; /* Ensure text is readable */
387 |           border: none !important; /* Optional: remove default border */
388 |       }
389 | 
390 | 
391 | 
392 | 
393 | 
394 | 
395 |       .nav-tabs .nav-link.active {
396 |           background-color: #045000 !important; /* Slightly darker shade for active tab */
397 |           color: white !important;
398 |       }
399 | 
400 | 
401 | 
402 | 
403 |       .submit-button {
404 |          background-color: #063800;
405 |          color: #FFFFFF;
406 |          border: none;
407 |          padding: 10px 20px;
408 |          border-radius: 4px;
409 |          font-size: 16px;
410 |          cursor: pointer;
411 |      }
412 |      .submit-button:hover {
413 |          background-color: #1E6B47;
414 |      }
415 | 
416 | 
417 | 
418 |      .report-container{
419 |        background-color: #F5F5F5;
420 |        color: #1C1C1C;
421 |        display: flex;
422 |        padding: 10px;
423 |        gap: 30px;
424 |        align-items: center;
425 |        justify-content: center;
426 |        margin-bottom: 30px;
427 |      }
428 | 
429 | 
430 |       #loading-spinner {
431 |           display: none;
432 |           width: 24px;
433 |           height: 24px;
434 |           border: 4px solid rgba(46, 139, 87, 0.3);
435 |           border-top: 4px solid #2E8B57;
436 |           border-radius: 50%;
437 |           animation: spin 1s linear infinite;
438 |       }
439 | 
440 | 
441 | 
442 | 
443 |       @keyframes spin {
444 |           0% { transform: rotate(0deg); }
445 |           100% { transform: rotate(360deg); }
446 |       }
447 | 
448 | 
449 | 
450 | 
451 |       .news-image {
452 |           width: 100px;  /* Set width */
453 |           height: 80px;  /* Set height */
454 |           object-fit: cover;  /* Crop image to fit */
455 |           border-radius: 5px;
456 |           box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
457 |       }
458 |       .nav-tabs {
459 |        border-bottom: none !important;
460 |        margin-bottom: 0 !important;
461 |        padding-bottom: 0 !important;
462 |     }
463 | 
464 | 
465 | 
466 |     .tab-content {
467 |        color:#F5F5F5;
468 |        background-color: #1C1C1C !important; /* Match the surrounding area */
469 |        margin-top: -1px !important; /* Fixes any white gap */
470 |        border-radius: 0 0 8px 8px;
471 |        border: none !important;
472 |     }
473 | 
474 | 
475 |     /* Ensure each tab-pane also has the correct background */
476 |     .tab-pane {
477 |        background-color: #1C1C1C !important;
478 |        margin: 0 !important;
479 |        border: none !important;
480 |     }
481 | 
482 | 
483 |     /* If a card or container inside tab-content has a background, override it */
484 |     .tab-pane > div {
485 |        background-color: #1C1C1C !important;
486 |        border: none !important;
487 |        margin: 0 !important;
488 |        padding: 20px;
489 |     }
490 |     .page-bottom {
491 |        background-color: #1C1C1C !important;
492 |        padding: 50px 0; /* Adds spacing */
493 |        min-height: 1000px; /* Adjust as needed */
494 |     }
495 | 
496 | 
497 |     .logo {
498 |            z-index: 20;
499 |        max-height: 100px; /* Adjusts within the header */
500 |        width: auto; /* Maintains aspect ratio */
501 |        position: absolute;
502 |        top: 30px; /* Aligns with the hamburger icon */
503 |        left: 500px; /* Pushes it to the right of the hamburger icon */
504 |     }
505 |     .padding-for-info {
506 |        max-width: 1100px; /* Limits width for readability */
507 |        padding: 0 40px; /* Left & right padding */
508 |        text-align: center;
509 |        margin: 0 auto; /* Ensures centering */
510 |     }
511 | 
512 |   </style>
513 |   <script src="https://cdn.socket.io/4.5.3/socket.io.min.js"
514 |   integrity="sha384-WPFUvHkB1aHA5TDSZi6xtDgkF0wXJcIIxXhC6h8OT8EH3fC5PWro5pWJ1THjcfEi"
515 |   crossorigin="anonymous"></script>
516 | </head>
517 | <body>
518 |    <div class="div1">
519 |        <h1 style="color:white; text-align:center;"> EmissiTrack</h1>
520 |       </div>
521 |       <div class="catchy-phrase"> User Guide </div>
522 |   <img src="{{ url_for('static', filename='images/missiTrack.png') }}" alt="Logo" class="logo">
523 |       <div class="hamburger-icon">&#9776;</div>
524 |       <ul class="navigation">
525 |        <li class="active">
526 |            <a href="{{url_for('test')}}">
527 |                <span class="icon"> <ion-icon name="home-outline"></ion-icon></span>
528 |            </a>
529 |        </li>
530 |        <li>
531 |            <a href="#">
532 |                <span class="icon"> <ion-icon name="help-circle-outline"></ion-icon></span>
533 |            </a>
534 |        </li>
535 |        <li>
536 |            <a href="{{url_for('advanced_search')}}">
537 |                <span class="icon"> <ion-icon name="funnel-outline"></ion-icon></span> <!-- ✅ Corrected -->
538 |            </a>
539 |        </li>
540 |        <li>
541 |            <a href="{{url_for('register')}}">
542 |                <span class="icon"><ion-icon name="person-add-outline"></ion-icon></span> <!-- ✅ Corrected -->
543 |            </a>
544 |        </li>
545 |        <li class="active">
546 |            <a href=/firstpage>
547 |                <span class="icon"> <ion-icon name="grid-outline"></ion-icon></span> <!-- ✅ First Page Icon -->
548 |            </a>
549 |        </li>
550 |    </ul>
551 |       <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
552 |           <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
553 |           <script>
554 |               document.addEventListener('DOMContentLoaded', function () {
555 |                   const hamburger = document.querySelector('.hamburger-icon');
556 |                   const navigation = document.querySelector('.navigation');
557 |                   let isOpen = false;
558 |                   hamburger.addEventListener('click', function () {
559 |                       // Toggle menu visibility
560 |                       isOpen = !isOpen;
561 |                       if (isOpen) {
562 |                           navigation.classList.add('show');
563 |                       } else {
564 |                           navigation.classList.remove('show');
565 |                       }
566 |                   });
567 | 
568 |                   // Keep your existing navigation item click event listener
569 |                   let list = document.querySelectorAll('.navigation li');
570 |                   function activeLink() {
571 |                       list.forEach((item) => item.classList.remove('active'));
572 |                       this.classList.add('active');
573 |                   }
574 |                   list.forEach((item) => item.addEventListener('click', activeLink));
575 |               });
576 |           </script>
577 | <br>
578 | <h1 style="text-align:center;">How does EmissiTrack work? </h1>
579 | <div class="padding-for-info">
580 | <h2 style="text-align:center; margin-top:50px; font-weight:bold;">What is EmissiTrack?</h2>
581 |       <p style="text-align:center;">A Smart, Scalable, and Dynamic Solution for Tracking Corporate Carbon Footprints.</p>
582 | 
583 | 
584 | 
585 | 
586 |       <p style="text-align:center;">The Carbon Emissions Tracker is a web-based platform designed to dynamically retrieve, categorize, and visualize corporate carbon emissions data for listed companies within the MSCI All World Index. This tool empowers users to access the latest Scope 1 (direct emissions) and Scope 2 (indirect emissions from purchased electricity) data from publicly available sources such as Corporate Social Responsibility (CSR) reports, government databases, and other sustainability disclosures.</p>
587 | 
588 | 
589 | 
590 | 
591 |       <p style="text-align:center;">In addition to emissions data, the platform features a real-time news feed with top headlines for each company, keeping users updated on sustainability-related developments. Users can also filter companies by sector, country, industry, and other key parameters to refine their searches and insights.</p>
592 |           <p style="text-align:center;">Emissions data can be visualized either in interactive bar charts or structured in a detailed table format. </p>
593 | 
594 | 
595 | 
596 | 
597 |           <h2 style="text-align:center; margin-top:50px; font-weight:bold;">What is EmissiTrack Pro?</h2>
598 | 
599 |          <p> EmissiTrack Pro is a web-based platform that helps you quickly and accurately view a company’s greenhouse gas (GHG) emissions.<p></p> Under the hood, it uses Docling to extract raw GHG emission tables (Scope 1, Scope 2, etc.) from a company’s ESG PDFs. Once you search by name, ticker, or ISIN, EmissiTrack Pro retrieves the relevant PDF reports, processes the relevant tables with Docling, and uses an LLM for accurate data extraction and unit conversions. It then displays the extracted figures in a clear, interactive layout on the premium page, where a bar chart lets you visualise year-over-year changes at a glance. </p>
600 |          <p> Meanwhile, the system also creates a separate Chatbot using the full sustainability report parsed in chunks by PyMuPDF4LLM, powered by a vector-embedding and retrieval flow that references the same underlying text and tables for in-depth Q&A. The Chatbot runs in parallel by indexing the parsed data into vector storage and retrieving details on demand. If you wish to halt loading—perhaps to search for a different company—you can click “Stop RAG” to interrupt the Chatbot’s background retrieval process before starting fresh.<p></p> This dual approach—Docling for accurate table extraction and an LLM-based retriever for chat—ensures maximum accuracy in capturing raw numbers while still providing a dynamic conversational interface for deeper insight into sustainability reports.</p>
601 | 
602 | 
603 | </div>
604 |       <!-- Bootstrap JS (Ensure Bootstrap's JavaScript is included) -->
605 |       <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
606 | 
607 | </body>
608 | </html>
609 | 
610 | 
611 | 
```

src/templates/instructionspremium.html
```
1 | <!DOCTYPE html>
2 | <html lang="en">
3 | <head>
4 |   <meta charset="UTF-8">
5 |   <meta http-equiv="X-UA-Compatible" content="IE=edge">
6 |   <meta name="viewport" content="width=device-width, initial-scale=1.0">
7 |   <title>Emissions Report</title>
8 |   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
9 |   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
10 |   <style>
11 |       body {
12 |            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
13 |            background-color: #F5F5F5;
14 |            color: #333333;
15 |            margin: 0;
16 |            padding: 0;
17 |        }
18 | 
19 | 
20 |       table, th, td {
21 |            border: 1px solid black;
22 |       }
23 | 
24 | 
25 | 
26 | 
27 |       .content {
28 |          margin-left: 130px; /* Pushes content right */
29 |          padding: 20px;
30 | 
31 |       }
32 | 
33 | 
34 |       .div1 {
35 |        z-index: 10; /* Ensures it appears above other elements */
36 |        position: relative; /* Required for z-index to work */
37 |           height: 160px;
38 |           width: 100%; /* Ensure it takes full width */
39 |           margin: 0;
40 |           background-color: #063800;
41 |           display: flex;
42 |           align-items: center; /* Centers vertically */
43 |           justify-content: center; /* Centers horizontally */
44 |           box-shadow: 0px 4px 15px rgba(20, 80, 20, 0.6);
45 |       }
46 |       .catchy-phrase {
47 |        z-index: 10;
48 |        position: absolute;
49 |        top: 120px;
50 |        transform: translate(-50%, -50%);
51 |        left: 50%;
52 |        color: white;
53 |        font-size: 20px;
54 | }
55 | 
56 | 
57 | 
58 | 
59 |       .navigation {
60 |           position: absolute;
61 |           left:0;
62 |           width:100px;
63 |           height:100%;
64 |           background:  #063800;
65 |           box-shadow: 25px 25px 75px rgba(0,0,0,0.25), 10px 10px 70px rgba(0,0,0,0.25), inset 5px 5px 10px rgba(0,0,0,0.5), inset 5px 5px 20px rgba(255,255,255,0.2) , inset -5px -5px 15px rgba(0,0,0,0.75);
66 |           display:center;
67 |           justify-content:center;
68 |           align-items:center;
69 |           flex-direction:column;
70 |           gap:10px;
71 |           transform: translateX(-100%);
72 |           transition: transform 0.3s ease;
73 | 
74 | 
75 | 
76 | 
77 |       }
78 | 
79 | 
80 |       .navigation.show {
81 |           transform: translateX(0);
82 |       }
83 | 
84 | 
85 | 
86 | 
87 |       .navigation li {
88 |           position:relative;
89 |           list-style:none;
90 |           width:80px;
91 |           height: 80px;
92 |           display:flex;
93 |           justify-content:center;
94 |           margin: 0 5px;
95 | 
96 |       }
97 | 
98 |       .navigation li::before {
99 |           content: '';
100 |           position: absolute;
101 |           top:calc(50% - 2.5px);
102 |           left: 20px;
103 |           width:5px;
104 |           height: 5px;
105 |           border-radius:50%;
106 |           transition:0.5s;
107 | 
108 |       }
109 | 
110 | 
111 | 
112 | 
113 |       .navigation li.active::before {
114 |           background:white;
115 |           box-shadow:0 0 5px white,
116 |           0 0 10px white,
117 |           0 0 20px white,
118 |           0 0 30px white,
119 |           0 0 40px white;
120 |       }
121 | 
122 | 
123 |       .navigation li a {
124 |           display:flex;
125 |           justify-content:center;
126 |           align-items:center;
127 |           flex-direction:column;
128 |           text-decoration:none;
129 |       }
130 | 
131 | 
132 | 
133 | 
134 |       .navigation li a .icon {
135 |           color: white;
136 |           transition: 0.5s;
137 |           transition-delay: 0.2s;
138 |           font-size: 1.5em;
139 |       }
140 | 
141 | 
142 |       .navigation li.active a .icon::before{
143 |           transform:scale(1);
144 | 
145 |       }
146 | 
147 | 
148 | 
149 | 
150 |       .navigation li a .text{
151 |           position: absolute;
152 |           left:130px;
153 |           font-size:1.25em;
154 |           color:white;
155 |           visibility:hidden;
156 |           transition:0.5s;
157 | 
158 |       }
159 | 
160 | 
161 |       .navigation li:hover a .text {
162 |           visibility: visible;
163 |       }
164 | 
165 | 
166 |       .hamburger-icon {
167 |           font-size: 30px;
168 |          color: white;
169 |          cursor: pointer;
170 |          position: absolute;
171 |          top: 20px;
172 |          left: 20px;
173 |          z-index: 100;
174 |          align-items: center;
175 |       }
176 | 
177 | 
178 | 
179 | 
180 |       .sidebar1 {
181 |           display: flex;
182 |          flex-direction: column;
183 |          align-items: center;
184 |          justify-content: center;
185 |          border: 1px solid #ccc;
186 |          border-radius: 8px;
187 |          margin-left: 50px;
188 |          margin-top: 40px;
189 |          float: left;
190 |          width: 250px;
191 |          height: 150px;
192 |          padding: 20px;
193 |          background-color: white;
194 |          color: white;
195 |          z-index: 1000;
196 |       }
197 | 
198 | 
199 | 
200 | 
201 |       .dropbtn {
202 |         background-color: white;
203 |            color:  #063800;
204 |            padding: 16px;
205 |            font-size: 16px;
206 |            border: none;
207 |           cursor: pointer;
208 |       }
209 | 
210 | 
211 |        .dropdown {
212 |        z-index: 15;
213 |         position: absolute;
214 |          top: 20px; /* Distance from the top */
215 |          right: 20px;
216 |            display: inline-block;
217 |            border: 1px solid white;
218 |            background-color: white;
219 |            border-radius: 12px;
220 |            padding: 4px 7px;
221 |              font-size: 16px;
222 |              cursor: pointer;
223 |              align-items: center;
224 |       }
225 | 
226 | 
227 | 
228 | 
229 |       .dropdown-content {
230 |            display: none;
231 |            padding: 5px 15px;
232 |            position: absolute;
233 |            font-size: 16px;
234 |            background-color:white;
235 |            min-width: 100px;
236 |            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
237 |            z-index: 1;
238 |       }
239 | 
240 |       .dropdown-content a {
241 |         color: black;
242 |         padding: 12px 16px;
243 |         text-decoration: none;
244 |         display: block;
245 |       }
246 | 
247 | 
248 |       /* Change color of dropdown links on hover */
249 |       .dropdown-content a:hover {background-color: #2e8b563d;}
250 | 
251 | 
252 |       /* Show the dropdown menu on hover */
253 |       .dropdown:hover .dropdown-content {display: block;}
254 | 
255 |       /* Change the background color of the dropdown button when the dropdown content is shown */
256 |       .dropdown:hover .dropbtn {background-color: rgba(255, 255, 255, 0.607);}
257 | 
258 | 
259 | 
260 | 
261 |       .progress-bar {
262 |           background-color: #045000!important;/* This is the green color you used for other elements */
263 |       }
264 | 
265 | 
266 |       .selected-company {
267 |            background-color: white;
268 |            padding: 20px;
269 |            margin: 20px auto;
270 |            align-items: center;
271 |            justify-content: center;
272 |            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
273 |            border: 2px solid black;
274 |            display: inline-block;
275 |            width: 90%; /* Adjust width for better layout */
276 |            max-width: 1400px;
277 |         }
278 | 
279 | 
280 |     /* Table Styling */
281 |     .selected-company table {
282 |        width: 100%;
283 |        border-collapse: collapse;
284 |     }
285 | 
286 | 
287 |     .selected-company th, .selected-company td {
288 |        border: 1px solid black;
289 |        padding: 8px;
290 |        text-align: center;
291 |     }
292 | 
293 | 
294 |     .selected-company th {
295 |        background-color: #063800;
296 |        color: white;
297 |     }
298 | 
299 | 
300 |     /* Style the Download Button */
301 |     .selected-company a.btn-success {
302 |        display: block;
303 |        margin: 10px auto;
304 |        text-align: center;
305 |        background-color: #063800;
306 |        color: white;
307 |        padding: 10px 15px;
308 |        font-size: 16px;
309 |        border-radius: 5px;
310 |        text-decoration: none;
311 |        transition: background-color 0.3s ease;
312 |     }
313 | 
314 | 
315 |     .selected-company a.btn-success:hover {
316 |        background-color: #1E6B47;
317 |     }
318 | 
319 | 
320 |     .esg-container {
321 |              background-color: white;
322 |              display: flex;
323 |              padding: 10px;
324 |              gap: 30px;
325 |              align-items: center;
326 |              justify-content: center;
327 |              margin-bottom: 30px;
328 |          }
329 | 
330 | 
331 |       .list-group-item {
332 |          width:1400px;
333 |          box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
334 |          border: 2px solid black; padding: 5px; display: inline-block;
335 |          background-color: white;
336 |          padding: 20px;
337 |          margin-left:20px;
338 |          align-items: center;
339 |          justify-content: center;
340 |       }
341 | 
342 | 
343 | 
344 | 
345 |       .dropdown-container {
346 |          background-color: #F5F5F5;
347 |          display: flex;
348 |          padding: 10px;
349 |          gap: 30px;
350 |          align-items: center;
351 |          justify-content: center;
352 |          margin-bottom: 30px;
353 |      }
354 |      .dropdown-container label{
355 |        color: #1C1C1C;
356 |      }
357 | 
358 | 
359 | 
360 | 
361 |      .nav-tabs .nav-link {
362 |           background-color: #063800 !important;
363 |           color: white !important; /* Ensure text is readable */
364 |           border: none !important; /* Optional: remove default border */
365 |       }
366 | 
367 | 
368 | 
369 | 
370 | 
371 | 
372 |       .nav-tabs .nav-link.active {
373 |           background-color: #045000 !important; /* Slightly darker shade for active tab */
374 |           color: white !important;
375 |       }
376 | 
377 | 
378 | 
379 | 
380 |       .submit-button {
381 |          background-color: #063800;
382 |          color: #FFFFFF;
383 |          border: none;
384 |          padding: 10px 20px;
385 |          border-radius: 4px;
386 |          font-size: 16px;
387 |          cursor: pointer;
388 |      }
389 |      .submit-button:hover {
390 |          background-color: #1E6B47;
391 |      }
392 | 
393 | 
394 | 
395 | 
396 |      .report-container{
397 |        background-color: #F5F5F5;
398 |        color: #1C1C1C;
399 |        display: flex;
400 |        padding: 10px;
401 |        gap: 30px;
402 |        align-items: center;
403 |        justify-content: center;
404 |        margin-bottom: 30px;
405 |      }
406 | 
407 | 
408 | 
409 | 
410 |       #loading-spinner {
411 |           display: none;
412 |           width: 24px;
413 |           height: 24px;
414 |           border: 4px solid rgba(46, 139, 87, 0.3);
415 |           border-top: 4px solid #2E8B57;
416 |           border-radius: 50%;
417 |           animation: spin 1s linear infinite;
418 |       }
419 | 
420 | 
421 | 
422 | 
423 |       @keyframes spin {
424 |           0% { transform: rotate(0deg); }
425 |           100% { transform: rotate(360deg); }
426 |       }
427 | 
428 | 
429 | 
430 | 
431 |       .news-image {
432 |           width: 100px;  /* Set width */
433 |           height: 80px;  /* Set height */
434 |           object-fit: cover;  /* Crop image to fit */
435 |           border-radius: 5px;
436 |           box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
437 |       }
438 |       .nav-tabs {
439 |            border-bottom: none !important;
440 |            margin-bottom: 0 !important;
441 |            padding-bottom: 0 !important;
442 |         }
443 | 
444 | 
445 |         /* Ensure tab content blends perfectly with the background */
446 |         .tab-content {
447 |            color:#F5F5F5;
448 |            background-color: #1C1C1C !important; /* Match the surrounding area */
449 |            margin-top: -1px !important; /* Fixes any white gap */
450 |            border-radius: 0 0 8px 8px;
451 |            border: none !important;
452 |         }
453 | 
454 | 
455 |         /* Ensure each tab-pane also has the correct background */
456 |         .tab-pane {
457 |            background-color: #1C1C1C !important;
458 |            margin: 0 !important;
459 |            border: none !important;
460 |         }
461 | 
462 | 
463 |         /* If a card or container inside tab-content has a background, override it */
464 |         .tab-pane > div {
465 |            background-color: #1C1C1C !important;
466 |            border: none !important;
467 |            margin: 0 !important;
468 |            padding: 20px;
469 |         }
470 |         .page-bottom {
471 |            background-color: #1C1C1C !important;
472 |            padding: 50px 0; /* Adds spacing */
473 |            min-height: 1000px; /* Adjust as needed */
474 |         }
475 | 
476 | 
477 |         .logo {
478 |                z-index: 20;
479 |            max-height: 100px; /* Adjusts within the header */
480 |            width: auto; /* Maintains aspect ratio */
481 |            position: absolute;
482 |            top: 30px; /* Aligns with the hamburger icon */
483 |            left: 500px; /* Pushes it to the right of the hamburger icon */
484 |         }
485 |         .padding-for-info {
486 |            max-width: 1100px; /* Limits width for readability */
487 |            padding: 0 40px; /* Left & right padding */
488 |            text-align: center;
489 |            margin: 0 auto; /* Ensures centering */
490 |         }
491 |   </style>
492 |   <script src="https://cdn.socket.io/4.5.3/socket.io.min.js"
493 |   integrity="sha384-WPFUvHkB1aHA5TDSZi6xtDgkF0wXJcIIxXhC6h8OT8EH3fC5PWro5pWJ1THjcfEi"
494 |   crossorigin="anonymous"></script>
495 | 
496 | 
497 | 
498 | 
499 | </head>
500 | <body>
501 |    <div class="div1">
502 |        <h1 style="color:white; text-align:center;"> EmissiTrack</h1>
503 |       </div>
504 |       <div class="catchy-phrase"> Instructions </div>
505 |   <img src="{{ url_for('static', filename='images/missiTrack.png') }}" alt="Logo" class="logo">
506 |       <div class="hamburger-icon">&#9776;</div>
507 |       <ul class="navigation">
508 |        <li class="active">
509 |            <a href="{{url_for('test')}}">
510 |                <span class="icon"> <ion-icon name="home-outline"></ion-icon></span>
511 |            </a>
512 |        </li>
513 |        <li>
514 |            <a href="#">
515 |                <span class="icon"> <ion-icon name="help-circle-outline"></ion-icon></span>
516 |            </a>
517 |        </li>
518 |        <li>
519 |            <a href="{{url_for('advanced_search')}}">
520 |                <span class="icon"> <ion-icon name="funnel-outline"></ion-icon></span> <!-- ✅ Corrected -->
521 |            </a>
522 |        </li>
523 |        <li>
524 |            <a href="{{url_for('register')}}">
525 |                <span class="icon"><ion-icon name="person-add-outline"></ion-icon></span> <!-- ✅ Corrected -->
526 |            </a>
527 |        </li>
528 |        <li class="active">
529 |            <a href=/firstpage>
530 |                <span class="icon"> <ion-icon name="grid-outline"></ion-icon></span> <!-- ✅ First Page Icon -->
531 |            </a>
532 |        </li>
533 |    </ul>
534 |       <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
535 |           <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
536 |           <script>
537 |               document.addEventListener('DOMContentLoaded', function () {
538 |                   const hamburger = document.querySelector('.hamburger-icon');
539 |                   const navigation = document.querySelector('.navigation');
540 |                   let isOpen = false;
541 | 
542 |                   hamburger.addEventListener('click', function () {
543 |                       // Toggle menu visibility
544 |                       isOpen = !isOpen;
545 |                       if (isOpen) {
546 |                           navigation.classList.add('show');
547 |                       } else {
548 |                           navigation.classList.remove('show');
549 |                       }
550 |                   });
551 | 
552 |                   // Keep your existing navigation item click event listener
553 |                   let list = document.querySelectorAll('.navigation li');
554 |                   function activeLink() {
555 |                       list.forEach((item) => item.classList.remove('active'));
556 |                       this.classList.add('active');
557 |                   }
558 |                   list.forEach((item) => item.addEventListener('click', activeLink));
559 |               });
560 | 
561 |           </script>
562 | 
563 | <div class="padding-for-info">
564 | 
565 | 
566 |    <h2 style="text-align:center; margin-top:50px; font-weight:bold;">How to use EmissiTrack Pro?</h2>
567 |    <p style="text-align:center;"> <strong> Step 1: Searching for a Company </strong></p>
568 |    <p style="text-align:center;">In the text box at the top, type the name (e.g., “Amazon”), the ticker symbol (e.g., “AMZN”), or the ISIN (unique identifier) of the company you want to research.</p>
569 | 
570 | 
571 | 
572 | 
573 |    <p style="text-align:center;"><strong>  Step 2: Viewing GHG Emissions Tables </strong></p>
574 | <p style="text-align:center;">After searching, you’ll see GHG Emissions Tables on the left.
575 | • This includes “Key Table,” which lists the company’s Scope 1, Scope 2 (market-based), and Scope 2 (location-based) emissions by year.
576 | • There may also be additional breakdown tables (Scope 1 detail, Scope 2 detail, etc.).
577 | </p>
578 |    <p style="text-align:center;"> Tip: If you see “null,” that means no data was reported for that category/year.</p>
579 | 
580 | 
581 | 
582 | 
583 | <p style="text-align:center;"> <strong> Step 3: Checking the Emissions Chart </strong></p>
584 |    <p style="text-align:center;">No data for the Key Table was found, or the system couldn’t parse the year numbers.
585 | • If this happens, try searching a different way (e.g., exact company name or ticker).
586 | </p>
587 |    <p style="text-align:center;"> <strong> Step 4: RAG Chatbot </strong></p>
588 |    <p style="text-align:center;">It automatically initializes (you’ll see “RAG initialization started”).
589 | • Once it’s ready, you can type questions like “How do these emissions compare to last year?” or “What are the biggest drivers for Scope 3?”
590 | • Click Ask to see an AI-generated response based on the PDF data that was retrieved.</p>
591 | <p style="text-align:center;"> Stop RAG button:  If the background data build is taking too long or you want to cancel it, click Stop RAG.</p>
592 | 
593 | 
594 | 
595 | 
596 | </div>
597 |           <!-- Bootstrap JS (Ensure Bootstrap's JavaScript is included) -->
598 |       <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
599 | 
600 | 
601 |    </body>
602 |    </html>
603 | 
604 | 
```

src/templates/login.html
```
1 | <!DOCTYPE html>
2 | <html lang="en">
3 | <head>
4 |    <meta charset="UTF-8">
5 |    <title>login1</title>
6 |    <style>
7 |        body {
8 |            font-family: 'Inter', sans-serif;
9 |            background-color: #F5F5F5;
10 |            display: flex;
11 |            justify-content: center;
12 |            align-items: center;
13 |            height: 100vh;
14 |            margin: 0;
15 |        }
16 |        .logo {
17 |    z-index: 20;
18 |    max-height: 175px; /* Adjusts within the header */
19 |    width: auto; /* Maintains aspect ratio */
20 |    position: absolute;
21 |    top: 150px; /* Aligns with the hamburger icon */
22 |    left: 627px; /* Pushes it to the right of the hamburger icon */
23 | }
24 |        .container {
25 |            display: flex;
26 |        }
27 | 
28 | 
29 |        .box {
30 |            background-color: #063800;
31 |            width: 50%;
32 |            height: 700px;
33 |            box-shadow: 0px 16px 32px rgba(0, 0, 0, 0.5);
34 |            border-radius: 10px;
35 |            padding: 30px;
36 |        }
37 | 
38 | 
39 |        .content {
40 |            text-align: center;
41 |            padding-top: 160px;
42 |        }
43 | 
44 | 
45 |        .welcome-text {
46 |            text-align: center;
47 |            color: white;
48 |            font-size: 36px;
49 |        }
50 | 
51 | 
52 |        form {
53 |            text-align: center;
54 |        }
55 | 
56 | 
57 |        ul {
58 |            list-style-type: none;
59 |            margin: 0;
60 |            padding: 0;
61 |        }
62 | 
63 | 
64 |        .login-btn {
65 |            background-color: #FFFFFF;
66 |            color: #063800;
67 |            border: none;
68 |            padding: 10px 20px;
69 |            border-radius: 4px;
70 |            font-size: 16px;
71 |            cursor: pointer;
72 |        }
73 | 
74 | 
75 |        .login-btn:hover {
76 |            background-color: #ffffff9a;
77 |        }
78 | 
79 | 
80 |        .input-field {
81 |    border: 1px solid #ccc;
82 |    border-radius: 6px;
83 |    padding: 12px;
84 |    font-size: 16px;
85 |    width: 95%;
86 |    transition: all 0.3s ease-in-out;
87 | }
88 | .input-field:focus {
89 |    border-color: #063800;
90 |    box-shadow: 0 0 8px rgba(6, 56, 0, 0.3);
91 |    outline: none;
92 | }
93 | 
94 | 
95 | 
96 | 
97 |        .input-field::placeholder {
98 |    font-size: 18px;  /* For placeholder text */
99 | }
100 |        .forgot-password {
101 |            font-size: 14px;
102 |            color: #063800;
103 |            text-decoration: none;
104 |        }
105 | 
106 | 
107 |        .forgot-password:hover {
108 |            text-decoration: underline;
109 |        }
110 | 
111 | 
112 |        footer {
113 |            text-align: center;
114 |            margin-top: 20px;
115 |            font-size: 14px;
116 |        }
117 | 
118 | 
119 |        footer a {
120 |            color: #F5F5F5;
121 |            text-decoration: none;
122 |        }
123 | 
124 | 
125 |        footer a:hover {
126 |            text-decoration: underline;
127 |        }
128 |    </style>
129 | </head>
130 | <body>
131 | 
132 | 
133 |    <div class="box">
134 |        <h1 class="welcome-text">Welcome Back to EmissiTrack Pro!</h1>
135 |        <img src="{{ url_for('static', filename='images/missiTrack2.png') }}" alt="Logo" class="logo">
136 |        <div class="content">
137 |            <h2 style="color:white;">Sign in to access your Account</h2>
138 |            <form method="POST" action="/login">
139 |                <br>
140 |                <input type="email" id="email" name="email" required class="input-field" placeholder="Enter your email">
141 |                <br>
142 |                <br>
143 |                <input type="password" id="password" name="password" required class="input-field" placeholder="Enter your password">
144 |                <br>
145 |                <br>
146 |                <button type="submit" class="login-btn">Login</button>
147 |            </form>
148 |            <br>
149 |            <a href="#" class="forgot-password">Forgot Password?</a>
150 |            <br>
151 |            <br>
152 |            <footer>
153 |            <a href="{{url_for('register')}}" style="color:white;">Don't have an account? Sign up</a>
154 |        </footer>
155 |            <br>
156 |            <br>
157 |            <footer>
158 |                <p style="color: #F5F5F5;">Look at our <a href="#">Privacy Policy</a> for more information.</p>
159 |            </footer>
160 |        </div>
161 |    </div>
162 | 
163 | 
164 | 
165 | 
166 | </body>
167 | </html>
```

src/templates/maps.html
```
1 | <!DOCTYPE html>
2 | <html lang="en">
3 | <head>
4 |  <meta charset="UTF-8">
5 |     <style>
6 |         body {
7 |           font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
8 |           background-color: #1C1C1C;
9 |           color: #1C1C1C;
10 |           margin: 0;
11 |           padding: 0;
12 |       }
13 | 
14 |           .logo-header-container {
15 |    z-index: 10;
16 |    position: relative;
17 |    height: 160px;
18 |    width: 100%;
19 |    background-color: #063800;
20 |    display: flex;
21 |    align-items: center; /* Align items vertically */
22 |    justify-content: center; /* Center items horizontally */
23 |    gap: 20px; /* Add spacing between logo and text */
24 |    text-align: center;
25 | }
26 | 
27 | 
28 | .logo {
29 |    max-height: 100px;
30 |    width: auto;
31 | }
32 | 
33 | 
34 | .div1 {
35 |    display: flex;
36 |    flex-direction: column; /* Stack heading and phrase */
37 |    align-items: center;
38 |    justify-content: center;
39 | }
40 | 
41 | 
42 | .catchy-phrase {
43 |    color: white;
44 |    font-size: 20px;
45 |    margin-top: 5px; /* Adjust spacing between header and phrase */
46 | }
47 |         .padding-for-info {
48 |    max-width: 1100px; /* Limits width for readability */
49 |    padding: 40px; /* Left & right padding */
50 |    text-align: center;
51 |    margin: 0 auto; /* Ensures centering */
52 | }
53 | 
54 | 
55 | 
56 | 
57 | 
58 |      .navigation li:hover a .text {
59 |          visibility: visible;
60 |      }
61 | 
62 | 
63 |      .hamburger-icon {
64 |          font-size: 30px;
65 |         color: white;
66 |         cursor: pointer;
67 |         position: absolute;
68 |         top: 20px;
69 |         left: 20px;
70 |         z-index: 100;
71 |         align-items: center;
72 |      }
73 | 
74 | 
75 |      .sidebar1 {
76 |          display: flex;
77 |         flex-direction: column;
78 |         align-items: center;
79 |         justify-content: center;
80 |         border: 1px solid #ccc;
81 |         border-radius: 8px;
82 |         margin-left: 50px;
83 |         margin-top: 40px;
84 |         float: left;
85 |         width: 250px;
86 |         height: 150px;
87 |         padding: 20px;
88 |         background-color: white;
89 |         color: white;
90 |         z-index: 1000;
91 |      }
92 | 
93 | 
94 |      .navigation {
95 |          position: absolute;
96 |          left:0;
97 |          width:100px;
98 |          height:100%;
99 |          background:  #063800!important;
100 |          box-shadow: 25px 25px 75px rgba(0,0,0,0.25), 10px 10px 70px rgba(0,0,0,0.25), inset 5px 5px 10px rgba(0,0,0,0.5), inset 5px 5px 20px rgba(255,255,255,0.2) , inset -5px -5px 15px rgba(0,0,0,0.75);
101 |          display:center;
102 |          justify-content:center;
103 |          align-items:center;
104 |          flex-direction:column;
105 |          gap:10px;
106 |          transform: translateX(-100%);
107 |          transition: transform 0.3s ease;
108 | 
109 |      }
110 | 
111 |      .navigation.show {
112 |          transform: translateX(0);
113 |      }
114 | 
115 |      .navigation li {
116 |          position:relative;
117 |          list-style:none;
118 |          width:80px;
119 |          height: 80px;
120 |          display:flex;
121 |          justify-content:center;
122 |          margin: 0 5px;
123 | 
124 |      }
125 | 
126 | 
127 |      .navigation li::before {
128 |          content: '';
129 |          position: absolute;
130 |          top:calc(50% - 2.5px);
131 |          left: 20px;
132 |          width:5px;
133 |          height: 5px;
134 |          border-radius:50%;
135 |          transition:0.5s;
136 | 
137 |      }
138 | 
139 | 
140 |      .navigation li.active::before {
141 |          background:white;
142 |          box-shadow:0 0 5px white,
143 |          0 0 10px white,
144 |          0 0 20px white,
145 |          0 0 30px white,
146 |          0 0 40px white;
147 |      }
148 | 
149 |      .navigation li a {
150 |          display:flex;
151 |          justify-content:center;
152 |          align-items:center;
153 |          flex-direction:column;
154 |          text-decoration:none;
155 |      }
156 | 
157 | 
158 |      .navigation li a .icon {
159 |          color: white;
160 |          transition: 0.5s;
161 |          transition-delay: 0.2s;
162 |          font-size: 1.5em; /* Adjust this value to your preference */
163 |      }
164 | 
165 |      .navigation li.active a .icon::before{
166 |          transform:scale(1);
167 | 
168 | 
169 |      }
170 |      .navigation li a .text{
171 |          position: absolute;
172 |          left:130px;
173 |          font-size:1.25em;
174 |          color:white;
175 |          visibility:hidden;
176 |          transition:0.5s;
177 | 
178 |      }
179 | 
180 |     </style>
181 |     <title>Emissions Map</title>
182 | </head>
183 | <body>
184 |        <div class="logo-header-container">
185 |        <img src="{{ url_for('static', filename='images/missiTrack.png') }}" alt="Logo" class="logo">
186 |        <div class="div1">
187 |            <h1 style="color:white; text-align:center;"> EmissiTrack</h1>
188 |            <p class="catchy-phrase">Company Emissions Map</p>
189 |        </div>
190 |        </div>
191 |        <div class="hamburger-icon">&#9776;</div>
192 |      <ul class="navigation">
193 |       <li class="active">
194 |           <a href="{{url_for('test')}}">
195 |               <span class="icon"> <ion-icon name="home-outline"></ion-icon></span>
196 |           </a>
197 |       </li>
198 |       <li>
199 |           <a href="{{url_for('instructions')}}">
200 |               <span class="icon"> <ion-icon name="help-circle-outline"></ion-icon></span>
201 |           </a>
202 |       </li>
203 |       <li>
204 |           <a href="{{url_for('advanced_search')}}">
205 |               <span class="icon"> <ion-icon name="funnel-outline"></ion-icon></span> <!-- ✅ Corrected -->
206 |           </a>
207 |       </li>
208 |       <li>
209 |           <a href="{{url_for('register')}}">
210 |               <span class="icon"><ion-icon name="person-add-outline"></ion-icon></span> <!-- ✅ Corrected -->
211 |           </a>
212 |       </li>
213 |       <li class="active">
214 |           <a href=/firstpage>
215 |               <span class="icon"> <ion-icon name="grid-outline"></ion-icon></span> <!-- ✅ First Page Icon -->
216 |           </a>
217 |       </li>
218 |   </ul>
219 |      <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
220 |          <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
221 |          <script>
222 |              document.addEventListener('DOMContentLoaded', function () {
223 |                  const hamburger = document.querySelector('.hamburger-icon');
224 |                  const navigation = document.querySelector('.navigation');
225 |                  let isOpen = false;
226 |                  hamburger.addEventListener('click', function () {
227 |                      // Toggle menu visibility
228 |                      isOpen = !isOpen;
229 |                      if (isOpen) {
230 |                          navigation.classList.add('show');
231 |                      } else {
232 |                          navigation.classList.remove('show');
233 |                      }
234 |                  });
235 |                  // Keep your existing navigation item click event listener
236 |                  let list = document.querySelectorAll('.navigation li');
237 |                  function activeLink() {
238 |                      list.forEach((item) => item.classList.remove('active'));
239 |                      this.classList.add('active');
240 |                  }
241 |                  list.forEach((item) => item.addEventListener('click', activeLink));
242 |              });
243 |          </script>
244 |    </div>
245 |        <div class="padding-for-info">
246 |            <h3 style="color:white;">Top 40 Companies and their ESG Ratings</h3>
247 |     <iframe src="{{ url_for('serve_emissions_map') }}" width="90%" height="700px"></iframe>
248 |            </div>
249 | </body>
250 | </html>
```

src/templates/register.html
```
1 | <!DOCTYPE html>
2 | <html lang="en">
3 | <head>
4 |    <meta charset="UTF-8">
5 |    <title>Financial Markets</title>
6 |    <style>
7 |        body {
8 |            font-family: 'Inter', sans-serif;
9 |            background-color: #F5F5F5;
10 |            display: flex;
11 |            justify-content: center;
12 |            align-items: center;
13 |            height: 100vh;
14 |            margin: 0;
15 |        }
16 |        .instructions{
17 |            background-color: #F5F5F5;
18 |            color:#063800;
19 |            width: 47%;
20 |            height: 700px;
21 |        }
22 |        .container {
23 |            display: flex;
24 |        }
25 |        .logo-container {
26 |    display: flex;
27 |    justify-content: center;
28 |    margin-top: -70px;
29 | }
30 | .logo {
31 |    max-height: 160px;
32 |    width: auto;
33 | }
34 | 
35 | 
36 |        .box {
37 |            background-color: #063800;
38 |            width: 30%;
39 |            height: 700px;
40 |            box-shadow: 0px 16px 32px rgba(0, 0, 0, 0.5);
41 |            border-radius: 10px;
42 |            padding: 30px;
43 |        }
44 | 
45 | 
46 |        .content {
47 |            text-align: center;
48 |            padding-top:130px;
49 |            padding-left:20px;
50 |            padding-right:20px;
51 |            align-items: center;
52 |        }
53 | 
54 | 
55 | 
56 | 
57 | 
58 | 
59 |        form {
60 |            text-align: center;
61 |        }
62 | 
63 | 
64 |        .essay1 {
65 |            font-size: 14px;
66 |            padding-right: 120px
67 |        }
68 | 
69 | 
70 |        .box2 {
71 |            width: 400px;
72 |            padding: 1px;
73 |            border: 4px solid #ccc;
74 |            border-radius: 4px;
75 |            background-color: #fff;
76 |            color: #333;
77 |            font-size: 16px;
78 |            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
79 |        }
80 | 
81 | 
82 | 
83 | 
84 |        .input-field {
85 |    border: 1px solid #ccc;
86 |    border-radius: 6px;
87 |    padding: 12px;
88 |    font-size: 16px;
89 |    width: 95%;
90 |    transition: all 0.3s ease-in-out;
91 | }
92 | .input-field:focus {
93 |    border-color: #063800;
94 |    box-shadow: 0 0 8px rgba(6, 56, 0, 0.3);
95 |    outline: none;
96 | }
97 |        .input-field::placeholder {
98 |    font-size: 18px;  /* For placeholder text */
99 | }
100 |        .register-btn {
101 |            background-color: #FFFFFF;
102 |            color: #215839;
103 |            border: none;
104 |            padding: 10px 20px;
105 |            border-radius: 4px;
106 |            font-size: 16px;
107 |            cursor: pointer;
108 |        }
109 |        .register-btn:hover {
110 |            background-color: #ffffffa1;
111 |        }
112 |        footer {
113 |            text-align: center;
114 |            margin-top: 20px;
115 |            font-size: 14px;
116 |        }
117 | 
118 | 
119 |        footer a {
120 |            color: #F5F5F5;
121 |            text-decoration: none;
122 |        }
123 | 
124 | 
125 |        footer a:hover {
126 |            text-decoration: underline;
127 |        }
128 | 
129 |    </style>
130 | </head>
131 | <body>
132 |    <div class="instructions">
133 |        <h1 > Welcome to EmissiTrack Pro</h1>
134 |        <h2 >User Instructions:</h2>
135 |         <p > <b>1.</b> In the text field at the top, type the company name, ticker, or ISIN. </p>
136 |        <br>
137 |            <p> <b>2.</b> Choose the matching “Search Type” radio button.</p>
138 |            <br>
139 |                <p>   <b>3.</b> Click “Go.”</p>
140 |                <br>
141 |                    <p>   <b>4.</b> View the left column for the extracted emissions tables.</p>
142 |                    <br>
143 |                        <p>   <b>5.</b> Check the right column for the emissions chart and the chatbot.</p>
144 |                        <br>
145 |                            <p>   <b>6.</b> (Optional) Type a question for the chatbot and click “Ask.”</p>
146 |                            <br>
147 |                                <p>  <b>7.</b> (Optional) If you need to cancel the data retrieval process, click Stop RAG.</p>
148 |                                <br>
149 |                                    <h4>  That’s it! The page is meant to help you quickly find, visualize, and chat about greenhouse gas emissions data from the company’s sustainability reports.</h4>
150 |    </div>
151 | 
152 | 
153 |      <div class="box">
154 |          <div class="content">
155 |            <div class="logo-container">
156 |                <img src="{{ url_for('static', filename='images/missiTrack2.png') }}" alt="EmissiTrack Logo" class="logo">
157 |            </div>
158 | 
159 |              <h2 style="color:white;"> Register to access EmissiTrack Pro </h2>
160 |              <form method="POST" action="">
161 |                <br>
162 |                <input type="text" id="first_name" name="first_name" required class="input-field" placeholder="First Name"> <br>
163 |                <br>
164 |                <input type="text" id="last_name" name="last_name" required class="input-field" placeholder="Last Name"> <br>
165 |                <br>
166 |                <input type="email" id="email" name="email" required class="input-field" placeholder="Email Address"> <br>
167 |                <br>
168 |                <input type="password" id="password" name="Password" required class="input-field" placeholder="Password"> <br>
169 |                <br>
170 |                  <button type="submit" class="register-btn">Register</button>
171 |              </form>
172 |              <footer>
173 |              <p><a href="{{url_for('login')}}" style="color:white;">Already have an account, log in!</a></p>
174 |            </footer>
175 |              <footer>
176 |                <p style="color: #F5F5F5;">By continuing, you agree to our <a href="#">Terms of Service</a> and acknowledge that you've read our <a href="#">Privacy Policy</a>.</p>
177 |            </footer>
178 |          </div>
179 |      </div>
180 |  </div>
181 | </body>
182 | </html>
```

src/templates/test.html
```
1 | <!DOCTYPE html>
2 | <html lang="en">
3 | <head>
4 |  <meta charset="UTF-8">
5 |  <meta http-equiv="X-UA-Compatible" content="IE=edge">
6 |  <meta name="viewport" content="width=device-width, initial-scale=1.0">
7 |  <title>Emissions Report</title>
8 |  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
9 |  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
10 |    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
11 |  <style>
12 |      body {
13 |           font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
14 |           background-color: #F5F5F5;
15 |           color: #333333;
16 |           margin: 0;
17 |           padding: 0;
18 |       }
19 | 
20 | 
21 |      table, th, td {
22 |           border: 1px solid black;
23 |      }
24 | 
25 | 
26 |      .content {
27 |         margin-left: 130px; /* Pushes content right */
28 |         padding: 20px;
29 | 
30 |      }
31 | 
32 | 
33 |      .navigation {
34 |          position: absolute;
35 |          left:0;
36 |          width:100px;
37 |          height:100%;
38 |          background:  #063800;
39 |          box-shadow: 25px 25px 75px rgba(0,0,0,0.25), 10px 10px 70px rgba(0,0,0,0.25), inset 5px 5px 10px rgba(0,0,0,0.5), inset 5px 5px 20px rgba(255,255,255,0.2) , inset -5px -5px 15px rgba(0,0,0,0.75);
40 |          display:center;
41 |          justify-content:center;
42 |          align-items:center;
43 |          flex-direction:column;
44 |          gap:10px;
45 |          transform: translateX(-100%);
46 |          transition: transform 0.3s ease;
47 | 
48 | 
49 |      }
50 | 
51 | 
52 |      /* Class to toggle menu visibility */
53 |      .navigation.show {
54 |          transform: translateX(0);
55 |      }
56 | 
57 |      .navigation li {
58 |          position:relative;
59 |          list-style:none;
60 |          width:80px;
61 |          height: 80px;
62 |          display:flex;
63 |          justify-content:center;
64 |          margin: 0 5px;
65 | 
66 |      }
67 | 
68 |      .navigation li::before {
69 |          content: '';
70 |          position: absolute;
71 |          top:calc(50% - 2.5px);
72 |          left: 20px;
73 |          width:5px;
74 |          height: 5px;
75 |          border-radius:50%;
76 |          transition:0.5s;
77 |      }
78 | 
79 | 
80 |      .navigation li.active::before {
81 |          background:white;
82 |          box-shadow:0 0 5px white,
83 |          0 0 10px white,
84 |          0 0 20px white,
85 |          0 0 30px white,
86 |          0 0 40px white;
87 |      }
88 | 
89 | 
90 |      .navigation li a {
91 |          display:flex;
92 |          justify-content:center;
93 |          align-items:center;
94 |          flex-direction:column;
95 |          text-decoration:none;
96 |      }
97 | 
98 | 
99 |      .navigation li a .icon {
100 |          color: white;
101 |          transition: 0.5s;
102 |          transition-delay: 0.2s;
103 |          font-size: 1.5em;
104 |      }
105 | 
106 |      .navigation li.active a .icon::before{
107 |          transform:scale(1);
108 | 
109 |      }
110 | 
111 | 
112 |      .navigation li a .text{
113 |          position: absolute;
114 |          left:130px;
115 |          font-size:1.25em;
116 |          color:white;
117 |          visibility:hidden;
118 |          transition:0.5s;
119 | 
120 | 
121 |      }
122 | 
123 | 
124 |      .logo-header-container {
125 |    z-index: 10;
126 |    position: relative;
127 |    height: 160px;
128 |    width: 100%;
129 |    background-color: #063800;
130 |    display: flex;
131 |    align-items: center; /* Align items vertically */
132 |    justify-content: center; /* Center items horizontally */
133 |    gap: 20px; /* Add spacing between logo and text */
134 |    box-shadow: 0px 4px 15px rgba(20, 80, 20, 0.6);
135 |    text-align: center;
136 | }
137 | 
138 | 
139 | .logo {
140 |    max-height: 100px;
141 |    width: auto;
142 | }
143 | 
144 | 
145 | .div1 {
146 |    display: flex;
147 |    flex-direction: column; /* Stack heading and phrase */
148 |    align-items: center;
149 |    justify-content: center;
150 | }
151 | 
152 | 
153 | .catchy-phrase {
154 |    color: white;
155 |    font-size: 20px;
156 |    margin-top: 5px; /* Adjust spacing between header and phrase */
157 | }
158 | 
159 | 
160 |      .navigation li:hover a .text {
161 |          visibility: visible;
162 |      }
163 | 
164 | 
165 |      /* Hamburger Icon Styles */
166 |      .hamburger-icon {
167 |          font-size: 30px;
168 |         color: white;
169 |         cursor: pointer;
170 |         position: absolute;
171 |         top: 20px;
172 |         left: 20px;
173 |         z-index: 100;
174 |         align-items: center;
175 |      }
176 | 
177 | 
178 | 
179 | 
180 | 
181 | 
182 | 
183 | 
184 |      .sidebar1 {
185 |          display: flex;
186 |         flex-direction: column;
187 |         align-items: center;
188 |         justify-content: center;
189 |         border: 1px solid #ccc;
190 |         border-radius: 8px;
191 |         margin-left: 50px;
192 |         margin-top: 40px;
193 |         float: left;
194 |         width: 250px;
195 |         height: 150px;
196 |         padding: 20px;
197 |         background-color: white;
198 |         color: white;
199 |         z-index: 1000;
200 |      }
201 | 
202 | 
203 | 
204 | 
205 | 
206 | 
207 | 
208 | 
209 |      .dropbtn {
210 |        background-color: white;
211 |           color:  #063800;
212 |           padding: 16px;
213 |           font-size: 16px;
214 |           border: none;
215 |          cursor: pointer;
216 |      }
217 | 
218 | 
219 | 
220 | 
221 | 
222 | 
223 | 
224 | 
225 |      /* The container <div> - needed to position the dropdown content */
226 |       .dropdown {
227 |       z-index: 15;
228 |        position: absolute;
229 |         top: 20px; /* Distance from the top */
230 |         right: 20px;
231 |           display: inline-block;
232 |           border: 1px solid white;
233 |           background-color: white;
234 |           border-radius: 12px;
235 |           padding: 4px 7px;
236 |             font-size: 16px;
237 |             cursor: pointer;
238 |             align-items: center;
239 |      }
240 | 
241 | 
242 |      /* Dropdown Content (Hidden by Default) */
243 |      .dropdown-content {
244 |           display: none;
245 |           padding: 5px 15px;
246 |           position: absolute;
247 |           font-size: 16px;
248 |           background-color:white;
249 |           min-width: 100px;
250 |           box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
251 |           z-index: 1;
252 |      }
253 | 
254 | 
255 | 
256 | 
257 | 
258 | 
259 | 
260 | 
261 |      /* Links inside the dropdown */
262 |      .dropdown-content a {
263 |        color: black;
264 |        padding: 12px 16px;
265 |        text-decoration: none;
266 |        display: block;
267 |      }
268 | 
269 | 
270 |      /* Change color of dropdown links on hover */
271 |      .dropdown-content a:hover {background-color: #2e8b563d;}
272 | 
273 | 
274 |      /* Show the dropdown menu on hover */
275 |      .dropdown:hover .dropdown-content {display: block;}
276 | 
277 | 
278 |      /* Change the background color of the dropdown button when the dropdown content is shown */
279 |      .dropdown:hover .dropbtn {background-color: rgba(255, 255, 255, 0.607);}
280 | 
281 |      .progress-bar {
282 |          background-color: #045000!important;/* This is the green color you used for other elements */
283 |      }
284 | 
285 | 
286 |      .selected-company {
287 |       background-color: white;
288 |       padding: 20px;
289 |       margin: 20px auto;
290 |       align-items: center;
291 |       justify-content: center;
292 |       box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
293 |       border: 2px solid black;
294 |       display: inline-block;
295 |       width: 90%; /* Adjust width for better layout */
296 |       max-width: 1400px;
297 |     }
298 | 
299 | 
300 | 
301 | 
302 | /* Table Styling */
303 | .selected-company table {
304 |   width: 100%;
305 |   border-collapse: collapse;
306 | }
307 | 
308 | 
309 | 
310 | 
311 | .selected-company th, .selected-company td {
312 |   border: 1px solid black;
313 |   padding: 8px;
314 |   text-align: center;
315 | }
316 | 
317 | 
318 | 
319 | 
320 | .selected-company th {
321 |   background-color: #063800;
322 |   color: white;
323 | }
324 | 
325 | 
326 | 
327 | 
328 | /* Style the Download Button */
329 | .selected-company a.btn-success {
330 |   display: block;
331 |   margin: 10px auto;
332 |   text-align: center;
333 |   background-color: #063800;
334 |   color: white;
335 |   padding: 10px 15px;
336 |   font-size: 16px;
337 |   border-radius: 5px;
338 |   text-decoration: none;
339 |   transition: background-color 0.3s ease;
340 | }
341 | 
342 | 
343 | 
344 | 
345 | .selected-company a.btn-success:hover {
346 |   background-color: #1E6B47;
347 | }
348 | 
349 | 
350 | 
351 | 
352 | .esg-container {
353 |         background-color: white;
354 |         display: flex;
355 |         padding: 10px;
356 |         gap: 30px;
357 |         align-items: center;
358 |         justify-content: center;
359 |         margin-bottom: 30px;
360 |     }
361 | 
362 | 
363 |      .list-group-item {
364 |         width:1400px;
365 |         box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
366 |         border: 2px solid black; padding: 5px; display: inline-block;
367 |         background-color: white;
368 |         padding: 20px;
369 |         margin-left:20px;
370 |         align-items: center;
371 |         justify-content: center;
372 |      }
373 | 
374 | 
375 |      .dropdown-container {
376 |         background-color: #F5F5F5;
377 |         display: flex;
378 |         padding: 10px;
379 |         gap: 30px;
380 |         align-items: center;
381 |         justify-content: center;
382 |         margin-bottom: 30px;
383 |     }
384 |     .dropdown-container label{
385 |       color: #1C1C1C;
386 |     }
387 | 
388 | 
389 |     .nav-tabs .nav-link {
390 |          background-color: #063800 !important;
391 |          color: white !important; /* Ensure text is readable */
392 |          border: none !important; /* Optional: remove default border */
393 |      }
394 | 
395 |      .nav-tabs .nav-link.active {
396 |          background-color: #045000 !important; /* Slightly darker shade for active tab */
397 |          color: white !important;
398 |      }
399 | 
400 |      .submit-button {
401 |         background-color: #063800;
402 |         color: #FFFFFF;
403 |         border: none;
404 |         padding: 10px 20px;
405 |         border-radius: 4px;
406 |         font-size: 16px;
407 |         cursor: pointer;
408 |     }
409 |     .submit-button:hover {
410 |         background-color: #1E6B47;
411 |     }
412 | 
413 |     .report-container{
414 |       background-color: #F5F5F5;
415 |       color: #1C1C1C;
416 |       display: flex;
417 |       padding: 10px;
418 |       gap: 30px;
419 |       align-items: center;
420 |       justify-content: center;
421 |       margin-bottom: 30px;
422 |     }
423 | 
424 | 
425 |      #loading-spinner {
426 |          display: none;
427 |          width: 24px;
428 |          height: 24px;
429 |          border: 4px solid rgba(46, 139, 87, 0.3);
430 |          border-top: 4px solid #2E8B57;
431 |          border-radius: 50%;
432 |          animation: spin 1s linear infinite;
433 |      }
434 | 
435 | 
436 |      @keyframes spin {
437 |          0% { transform: rotate(0deg); }
438 |          100% { transform: rotate(360deg); }
439 |      }
440 | 
441 | 
442 |      .news-image {
443 |          width: 100px;  /* Set width */
444 |          height: 80px;  /* Set height */
445 |          object-fit: cover;  /* Crop image to fit */
446 |          border-radius: 5px;
447 |          box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
448 |      }
449 |      .nav-tabs {
450 |   border-bottom: none !important;
451 |   margin-bottom: 0 !important;
452 |   padding-bottom: 0 !important;
453 | }
454 | 
455 | 
456 | 
457 | 
458 | /* Ensure tab content blends perfectly with the background */
459 | .tab-content {
460 |   color:#F5F5F5;
461 |   background-color: #1C1C1C !important; /* Match the surrounding area */
462 |   margin-top: -1px !important; /* Fixes any white gap */
463 |   border-radius: 0 0 8px 8px;
464 |   border: none !important;
465 | }
466 | 
467 | 
468 | 
469 | 
470 | /* Ensure each tab-pane also has the correct background */
471 | .tab-pane {
472 |   background-color: #1C1C1C !important;
473 |   margin: 0 !important;
474 |   border: none !important;
475 | }
476 | 
477 | 
478 | 
479 | 
480 | /* If a card or container inside tab-content has a background, override it */
481 | .tab-pane > div {
482 |   background-color: #1C1C1C !important;
483 |   border: none !important;
484 |   margin: 0 !important;
485 |   padding: 20px;
486 | }
487 | .page-bottom {
488 |   background-color: #1C1C1C !important;
489 |   padding: 50px 0; /* Adds spacing */
490 |   min-height: 1000px; /* Adjust as needed */
491 | }
492 | 
493 |      .chart-container {
494 |            width: 100%;
495 |            max-width: 800px;
496 |            margin: 20px auto;
497 |        }
498 | 
499 | 
500 |  </style>
501 |  <script src="https://cdn.socket.io/4.5.3/socket.io.min.js"
502 |  integrity="sha384-WPFUvHkB1aHA5TDSZi6xtDgkF0wXJcIIxXhC6h8OT8EH3fC5PWro5pWJ1THjcfEi"
503 |  crossorigin="anonymous"></script>
504 | 
505 | </head>
506 | <body>
507 |    <div class="logo-header-container">
508 |        <img src="{{ url_for('static', filename='images/missiTrack.png') }}" alt="Logo" class="logo">
509 |        <div class="div1">
510 |            <h1 style="color:white; text-align:center;"> EmissiTrack</h1>
511 |            <p class="catchy-phrase">Home</p>
512 |        </div>
513 |    </div>
514 |  <div class="dropdown">
515 |          <button class="dropbtn">My Premium Profile</button>
516 |          <div class="dropdown-content">
517 |              <a href="{{url_for('register')}}">Create an account</a>
518 |              <a href="{{url_for('login')}}">Login</a>
519 |          </div>
520 |  </div>
521 | 
522 |      <div class="hamburger-icon">&#9776;</div>
523 |      <ul class="navigation">
524 |       <li class="active">
525 |           <a href="{{url_for('test')}}">
526 |               <span class="icon"> <ion-icon name="home-outline"></ion-icon></span>
527 |           </a>
528 |       </li>
529 |       <li>
530 |           <a href="{{url_for('instructions')}}">
531 |               <span class="icon"> <ion-icon name="help-circle-outline"></ion-icon></span>
532 |           </a>
533 |       </li>
534 |       <li>
535 |           <a href="{{url_for('advanced_search')}}">
536 |               <span class="icon"> <ion-icon name="funnel-outline"></ion-icon></span> <!-- ✅ Corrected -->
537 |           </a>
538 |       </li>
539 |       <li>
540 |           <a href="{{url_for('register')}}">
541 |               <span class="icon"><ion-icon name="person-add-outline"></ion-icon></span> <!-- ✅ Corrected -->
542 |           </a>
543 |       </li>
544 |       <li class="active">
545 |           <a href=/firstpage>
546 |               <span class="icon"> <ion-icon name="grid-outline"></ion-icon></span> <!-- ✅ First Page Icon -->
547 |           </a>
548 |       </li>
549 |   </ul>
550 |      <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
551 |          <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
552 |          <script>
553 |              document.addEventListener('DOMContentLoaded', function () {
554 |                  const hamburger = document.querySelector('.hamburger-icon');
555 |                  const navigation = document.querySelector('.navigation');
556 |                  let isOpen = false;
557 | 
558 |                  hamburger.addEventListener('click', function () {
559 |                      // Toggle menu visibility
560 |                      isOpen = !isOpen;
561 |                      if (isOpen) {
562 |                          navigation.classList.add('show');
563 |                      } else {
564 |                          navigation.classList.remove('show');
565 |                      }
566 |                  });
567 | 
568 |                  // Keep your existing navigation item click event listener
569 |                  let list = document.querySelectorAll('.navigation li');
570 |                  function activeLink() {
571 |                      list.forEach((item) => item.classList.remove('active'));
572 |                      this.classList.add('active');
573 |                  }
574 |                  list.forEach((item) => item.addEventListener('click', activeLink));
575 |              });
576 | 
577 |          </script>
578 | 
579 |  <!-- Form to enter company name -->
580 |  <form method="post" class="mb-4">
581 |      <div class="dropdown-container">
582 |      <label for="company_name" class="form-label">Enter Company Identifier:</label>
583 |      <input type="text" id="company_name" name="company_name" class="form-control" style="width:850px;" required>
584 | 
585 |      <div class="form-check mt-2">
586 |          <input class="form-check-input" type="radio" id="company" name="idType" value="name" checked>
587 |          <label class="form-check-label" for="company">Company</label>
588 |      </div>
589 |      <div class="form-check">
590 |          <input class="form-check-input" type="radio" id="ticker" name="idType" value="ticker">
591 |          <label class="form-check-label" for="ticker">Ticker</label>
592 |      </div>
593 |      <div class="form-check">
594 |          <input class="form-check-input" type="radio" id="isin" name="idType" value="isin">
595 |          <label class="form-check-label" for="isin">ISIN</label>
596 |      </div>
597 |      </div>
598 |      <!-- Submit Button and Spinner Container -->
599 |      <div style="display: flex; justify-content: center; align-items: center; gap: 10px; margin-top: 10px;">
600 |          <button type="submit" id="submit" class="submit-button">Search</button>
601 |          <div id="loading-spinner" style="display: none;"></div>
602 |      </div>
603 | 
604 |  </form>
605 |  <div id="resultContainer" style="display: none;"></div>
606 |  {% if company_name %}
607 |  <div class="report-container">
608 |      {% if report_url %}
609 |          <p>Latest ESG Report Link for {{company_name}}: <a href="{{ report_url }}" target="_blank">{{ report_url }}</a></p>
610 | 
611 | 
612 | 
613 | 
614 |      {% else %}
615 |          <p>No report found.</p>
616 |      {% endif %}
617 |  </div>
618 | 
619 | 
620 | 
621 | 
622 | 
623 | 
624 | 
625 | 
626 | 
627 | 
628 | 
629 | 
630 | 
631 | 
632 | 
633 | 
634 | 
635 | 
636 | 
637 | 
638 | 
639 | 
640 | 
641 | 
642 |      <!-- Tab Navigation -->
643 |      <ul class="nav nav-tabs mt-4" id="resultTabs" role="tablist">
644 |          <li class="nav-item" role="presentation">
645 |              <button class="nav-link active" id="table-tab" data-bs-toggle="tab" data-bs-target="#table-content" type="button" role="tab">Extracted Table <i class="fa-solid fa-table"></i></button>
646 |          </li>
647 |          <li class="nav-item" role="presentation">
648 |              <button class="nav-link" id="news-tab" data-bs-toggle="tab" data-bs-target="#news-content" type="button" role="tab">Latest News <i class="fa-solid fa-newspaper"></i></button>
649 |          </li>
650 |          <li class="nav-item" role="presentation">
651 |              <button class="nav-link" id="chart-tab" data-bs-toggle="tab" data-bs-target="#chart-content" type="button" role="tab">Data Visualization <i class="fa-solid fa-chart-column"></i></button>
652 |          </li>
653 |      </ul>
654 | 
655 |      <!-- Tab Content -->
656 |          <div class="tab-content mt-3" id="resultTabsContent">
657 |           <!-- Table Section -->
658 |           <div class="tab-pane fade show active" id="table-content" role="tabpanel">
659 |               {% if company_name and table_html %}
660 |               <div class="selected-company">
661 |                   <a href="{{ url_for('download_table', company_name=company_name) }}" class="btn btn-success mt-3">Download Table</a>
662 |                   <div>
663 |                       {{ table_html | safe }}
664 |                   </div>
665 |               {% else %}
666 |                   <p>No table data available.</p>
667 |               {% endif %}
668 |           </div>
669 |           </div>
670 | 
671 |          <!-- News Section -->
672 |          <div class="tab-pane fade" id="news-content" role="tabpanel">
673 |           <br>
674 |           <h3>Top Headlines for {{ company_name }}</h3>
675 |           {% if news_data %}
676 |               <div class="container-fluid"> <!-- Fluid container to match background -->
677 |                   <div class="row">
678 |                       {% for news in news_data %}
679 |                           <div class="col-md-6 mb-4"> <!-- Two columns per row -->
680 |                               <div class="card border-0 shadow-sm bg-transparent"> <!-- Transparent background -->
681 |                                   <div class="card-body d-flex align-items-center">
682 |                                       <img src="{{ news.image }}" alt="News Image" class="news-image me-3"
683 |                                            onerror="this.style.display='none';" style="width: 100px; height: auto;">
684 |                                       <div>
685 |                                           <strong style="color: white;">{{ news.title }}</strong> <!-- News Title -->
686 |                                           <br>
687 |                                           <small style="color: white;">Source: {{ news.publisher }}</small> <!-- Publisher Name -->
688 |                                           <br>
689 |                                           <a href="{{ news.link }}" target="_blank" class="btn btn-primary btn-sm mt-2">Read More</a> <!-- Read More Button -->
690 |                                       </div>
691 |                                   </div>
692 |                               </div>
693 |                           </div>
694 |                       {% endfor %}
695 |                   </div>
696 |               </div>
697 |           {% else %}
698 |               <p>No news available for this company.</p>
699 |           {% endif %}
700 |       </div>
701 | 
702 |           <!-- Histogram Visualization Section -->
703 |        <div class="tab-pane fade" id="chart-content">
704 |     <div class="chart-container">
705 |         <h3>Emissions Data Visualization</h3>
706 |         <canvas id="emissionsChart"></canvas>
707 |     </div>
708 |        {% endif %}
709 | </div>
710 | 
711 |          <div class="page-bottom">
712 |       </div>
713 | 
714 |      </div>
715 | 
716 |      <!-- Bootstrap JS (Ensure Bootstrap's JavaScript is included) -->
717 |      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
718 | 
719 |     <!-- React and ReactDOM via CDN -->
720 |     <script src="https://unpkg.com/react@17/umd/react.production.min.js"></script>
721 |     <script src="https://unpkg.com/react-dom@17/umd/react-dom.production.min.js"></script>
722 |     <!-- Material-UI Core (includes CircularProgress) -->
723 |     <script crossorigin src="https://unpkg.com/@mui/material@latest/umd/material-ui.production.min.js"></script>
724 | 
725 |     <script>
726 |     document.addEventListener("DOMContentLoaded", function () {
727 |      const { CircularProgress } = window.MaterialUI || {};
728 |      const spinnerContainer = document.getElementById("loading-spinner");
729 |      const submitButton = document.getElementById("submit");
730 |      const form = document.querySelector("form");
731 | 
732 |      let spinnerInitialized = false;
733 |      function initializeSpinner() {
734 |          if (!spinnerInitialized && CircularProgress) {
735 |              const spinner = React.createElement(CircularProgress, { color: "success", size: 24 });
736 |              ReactDOM.render(spinner, spinnerContainer);
737 |              spinnerInitialized = true;
738 |          }
739 |      }
740 | 
741 |      function showSpinner() {
742 |          submitButton.disabled = true;
743 |          submitButton.innerText = "Searching...";
744 |          initializeSpinner();
745 |          spinnerContainer.style.display = "inline-block"; // Show only when "Searching..."
746 |      }
747 | 
748 |      function hideSpinner() {
749 |          submitButton.disabled = false;
750 |          submitButton.innerText = "Search";
751 |          spinnerContainer.style.display = "none";
752 |      }
753 | 
754 |      form.addEventListener("submit", function () {
755 |          showSpinner();
756 |      });
757 | 
758 |      //  Reset spinner if user navigates away or cancels search
759 |      submitButton.addEventListener("click", function () {
760 |          if (submitButton.innerText === "Searching...") {
761 |              hideSpinner();
762 |          }
763 |      });
764 |     });
765 | 
766 |     </script>
767 |    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
768 | <script>
769 | document.addEventListener("DOMContentLoaded", function () {
770 |     function extractDataFromTable() {
771 |         const table = document.querySelector(".selected-company table");
772 |         if (!table) {
773 |             console.error(" No table found in .selected-company!");
774 |             return;
775 |         }
776 | 
777 |         const rows = table.querySelectorAll("tr");
778 |         if (rows.length < 2) {
779 |             console.error(" Table has no data rows.");
780 |             return;
781 |         }
782 | 
783 |         // Extract Headers & Year Columns
784 |         const headers = Array.from(rows[0].querySelectorAll("th")).map(th => th.innerText.trim());
785 |         let yearHeaders = headers.filter(h => /^\d{4}$/.test(h));
786 |         let yearIndexes = headers.map((h, i) => (yearHeaders.includes(h) ? i : -1)).filter(i => i !== -1);
787 | 
788 |         if (yearHeaders.length === 0) {
789 |             console.error(" No valid year columns found.");
790 |             return;
791 |         }
792 | 
793 |         console.log(" Extracted Year Headers:", yearHeaders);
794 | 
795 |         let emissionsData = {};
796 |         let dataFound = false;
797 | 
798 |         rows.forEach((row, rowIndex) => {
799 |             if (rowIndex === 0) return;
800 |             const cells = row.querySelectorAll("td");
801 | 
802 |             let metricName = cells[1]?.innerText.trim() || `Metric ${rowIndex}`; // Extract actual metric name from column 2
803 |             let values = yearIndexes.map(colIndex => {
804 |                 let value = parseFloat(cells[colIndex]?.innerText.replace(/,/g, "").trim()) || 0;
805 |                 if (value !== 0) dataFound = true;
806 |                 return value;
807 |             });
808 | 
809 |             emissionsData[metricName] = values;
810 |         });
811 | 
812 |         if (dataFound) {
813 |             console.log(" Emissions Data:", emissionsData);
814 |             setTimeout(() => renderHistogram(yearHeaders, emissionsData), 500);
815 |         } else {
816 |             console.warn("No valid emissions data found.");
817 |         }
818 |     }
819 | 
820 |     function renderHistogram(labels, emissionsData) {
821 |         const canvas = document.getElementById("emissionsChart");
822 |         if (!canvas) {
823 |             console.error(" No canvas element found!");
824 |             return;
825 |         }
826 | 
827 |         const ctx = canvas.getContext("2d");
828 | 
829 |         if (window.myChart) {
830 |             window.myChart.destroy();
831 |         }
832 | 
833 |         const datasets = Object.keys(emissionsData).map((metric, index) => ({
834 |             label: metric, // Use metric names from column 2 as legend labels
835 |             data: emissionsData[metric],
836 |             backgroundColor: getRandomColor(index),
837 |             borderWidth: 1
838 |         }));
839 | 
840 |         window.myChart = new Chart(ctx, {
841 |             type: "bar",
842 |             data: { labels: labels, datasets: datasets },
843 |             options: {
844 |                 responsive: true,
845 |                 plugins: {
846 |                     legend: { position: "top" },
847 |                     title: { display: true, text: "Emissions Over the Years" }
848 |                 },
849 |                 scales: {
850 |                     x: { title: { display: true, text: "Year" } },
851 |                     y: { title: { display: true, text: "Emissions" }, beginAtZero: true }
852 |                 }
853 |             }
854 |         });
855 |     }
856 | 
857 |     function getRandomColor(index) {
858 |         const colors = ["rgba(255, 99, 132, 0.7)", "rgba(54, 162, 235, 0.7)", "rgba(255, 206, 86, 0.7)"];
859 |         return colors[index % colors.length];
860 |     }
861 | 
862 |     extractDataFromTable();
863 | });
864 | </script>
865 | 
866 | 
867 | </body>
868 | </html>
869 | 
870 | 
871 | 
```

src/utils/__init__.py
```
```

src/utils/data.py
```
1 | import os
2 | import sys
3 | import urllib
4 | from io import BytesIO
5 | from typing import List
6 | 
7 | import pandas as pd
8 | import requests
9 | from dotenv import load_dotenv
10 | from loguru import logger
11 | 
12 | load_dotenv()
13 | 
14 | sys.path.append(os.getenv("ROOT_DIR"))
15 | 
16 | # URL to the CSV file (ACWI ETF holdings)
17 | MSCI_FUND_URL = "https://www.blackrock.com/ca/investors/en/products/239697/ishares-msci-world-index-etf/1515395013957.ajax?fileType=xls&fileName=iShares-MSCI-World-Index-ETF_fund&dataType=fund"
18 | 
19 | 
20 | def get_msci_index_df(write=False):
21 |     """
22 |     # TODO - add functionality for data refresh every 2 months
23 |     Function to fetch the MSCI ACWI ETF holdings data and return a filtered DataFrame.
24 | 
25 |     Args:
26 |         write (bool): Whether to write the CSV file to disk (default: False)
27 | 
28 |     Returns:
29 |         pd.DataFrame: DataFrame containing the MSCI ACWI ETF holdings data
30 |     """
31 |     headers = {
32 |         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
33 |     }
34 | 
35 |     # if file already downloaded read directly from disk
36 |     if os.path.exists(f'{os.getenv("ROOT_DIR")}/data/ACWI_holdings.csv'):
37 |         # Load the CSV file from disk
38 |         df = pd.read_csv(f'{os.getenv("ROOT_DIR")}/data/ACWI_holdings.csv', header=9)
39 |     else:
40 |         response = requests.get(MSCI_FUND_URL, headers=headers)
41 |         # Save the CSV file to disk (optional)
42 |         if write:
43 |             with open(f'{os.getenv("ROOT_DIR")}/data/ACWI_holdings.csv', "wb") as f:
44 |                 f.write(response.content)
45 |         # Load the content into a Pandas DataFrame (headers are on row 10 (0-indexed: row 9))
46 |         file_content = BytesIO(response.content)
47 |         df = pd.read_csv(file_content, header=9)
48 |     # Filter the rows where the 'Asset Class' column is equal to 'Equity'
49 |     df_filtered = df[df["Asset Class"] == "Equity"]
50 |     # Select the first two columns (Ticker and Name)
51 |     df_filtered = df_filtered[["Ticker", "Name"]]
52 |     return df_filtered
53 | 
54 | 
55 | def download_pdf_from_urls(urls: List[str], root_path: str):
56 |     """
57 |     Function to download a PDF file from a URL. Breaks on the first successful download.
58 | 
59 |     Args:
60 |         urls (List[str]): List of URLs to try to download in pdf format.
61 |     """
62 |     for url in urls:
63 |         try:
64 |             # isolate PDF filename from URL
65 |             pdf_file_name = (
66 |                 os.path.basename(url) + ".pdf"
67 |                 if not url.endswith(".pdf")
68 |                 else os.path.basename(url)
69 |             )
70 |             with urllib.request.urlopen(url, timeout=10):
71 |                 urllib.request.urlretrieve(url, os.path.join(root_path, pdf_file_name))
72 |             return os.path.join(root_path, pdf_file_name)
73 |         except Exception as e:
74 |             logger.error(f"Uh oh! Could not download {url}: {e}")
75 |             continue
```

src/utils/data_models.py
```
1 | """
2 | Stores enums and data models
3 | """
4 | 
5 | from enum import Enum
6 | 
7 | from pydantic import BaseModel, Field
8 | 
9 | 
10 | class SearchKeyWords(Enum):
11 |     ESG = "esg"
12 |     CSR = "csr"
13 |     SUSTAINABILITY = "sustainability"
14 |     EMISSION = "emission"
15 |     ENVIRONMENT = "environment"
16 |     SCOPE_1 = "scope 1"
17 |     SCOPE_2 = "scope 2"
18 |     SCOPE = "scope"
19 |     SUSTAINABLE = "sustainable"
20 |     IMPACT = "impact"
21 |     REPORT = "report"
22 |     FACT_SHEET = "fact sheet"
23 | 
24 | 
25 | class RegexPatterns(Enum):
26 |     SCOPE1 = r"\b(scope\s*1|scope\s*i|scope\s*one)\b"
27 |     SCOPE2 = r"\b(scope\s*2|scope\s*ii|scope\s*two)\b"
28 |     YEAR_1 = r"\b(?:FY|FISCAL\s*YEAR)?\s*(\d{2}|20\d{2}|[-–]\d{2})"
29 |     YEAR_2 = r"\b(\d{2}|20\d{2}|[-–]\d{2})"
30 |     UNITS_1 = r"\b(?:\d+(?:,\d{3})*(?:\.\d+)?|million|billion|thousand)"
31 |     UNITS_2 = r"\s*(?:tco2e|tco2-e|co2e|co₂e|co2-eq|co₂-eq|mtco2e|mtco₂e|ktco2e|ktco₂e|mt|kt|tons?|tonnes?|metric\s*tons?)"
32 | 
33 | 
34 | class TableParsers(Enum):
35 |     DOCLING = "docling"
36 |     TABULA = "tabula"
37 | 
38 | 
39 | class PDFParsers(Enum):
40 |     LLAMA_PARSE = "llama"
41 | 
42 | 
43 | class Company(BaseModel):
44 |     ticker: str = Field(..., title="Ticker Symbol")
45 |     name: str = Field(..., title="Company Name")
46 |     isin: str = Field(..., title="Company ISIN")
```

src/utils/llm_table_data_filtering.py
```
1 | import os
2 | 
3 | import pandas as pd
4 | from dotenv import load_dotenv
5 | 
6 | load_dotenv()
7 | 
8 | 
9 | try:
10 |     from openai import OpenAI
11 | except ImportError:
12 |     print("OpenAI client is not installed. Please install with: pip install openai")
13 |     OpenAI = None
14 | 
15 | 
16 | # Both keys are available. Uncomment the one you want to use below.
17 | OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
18 | DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
19 | 
20 | 
21 | def filter_tables(directory_path, parser):
22 |     """
23 |     Gather all CSVs in directory_path/parser.value, convert them to markdown,
24 |     send them to the LLM, store the LLM's markdown output, and return as a DataFrame.
25 |     """
26 | 
27 |     # 1) Collect all CSVs into one markdown string
28 |     combined_markdown = ""
29 |     parser_subfolder = os.path.join(directory_path, parser.value)
30 | 
31 |     # If the parser subfolder doesn't exist or is empty, handle gracefully
32 |     if not os.path.isdir(parser_subfolder):
33 |         print(f"No directory found for parser: {parser_subfolder}")
34 |         return pd.DataFrame()
35 | 
36 |     for filename in os.listdir(parser_subfolder):
37 |         if filename.endswith(".csv"):
38 |             file_path = os.path.join(parser_subfolder, filename)
39 |             try:
40 |                 df = pd.read_csv(file_path)
41 |                 # Convert df to markdown
42 |                 md = df.to_markdown(index=False, tablefmt="pipe")
43 |                 # Optionally label by file
44 |                 combined_markdown += f"\n\n#### File: {filename}\n\n"
45 |                 combined_markdown += md
46 |                 combined_markdown += "\n\n"
47 |             except Exception as e:
48 |                 print(f"Error reading CSV {file_path}: {e}")
49 | 
50 |     if not combined_markdown.strip():
51 |         print("No CSV data found to send to the LLM.")
52 |         return pd.DataFrame()
53 | 
54 |     # 2) Send markdown content to LLM
55 |     llm_output = _send_to_deepseek(combined_markdown)
56 |     if not llm_output:
57 |         print("No response from LLM or an error occurred.")
58 |         return pd.DataFrame()
59 | 
60 |     # 3) Save the LLM's markdown output directly as .md file
61 |     output_path = os.path.join(directory_path, "esg_data_llm.md")
62 |     with open(output_path, "w", encoding="utf-8") as f:
63 |         f.write(llm_output)
64 |     print(f"LLM output saved to: {output_path}")
65 | 
66 |     # 4) Return DataFrame for compatibility with existing code
67 |     return pd.DataFrame({"LLM_Output": [llm_output]})
68 | 
69 | 
70 | def _send_to_deepseek(markdown_content: str) -> str | None:
71 |     """Sends markdown content to the LLM (either OpenAI or DeepSeek) for processing."""
72 |     # ---------------------------------------------------------------------
73 |     # To use OpenAI, uncomment the following block:
74 |     if not OPENAI_API_KEY:
75 |         print("OpenAI API key missing.")
76 |         return None
77 |     client = OpenAI(api_key=OPENAI_API_KEY)
78 |     # model="gpt-4o" will be used below.
79 |     # ---------------------------------------------------------------------
80 | 
81 |     # ---------------------------------------------------------------------
82 |     # To use DeepSeek, comment out the above block and uncomment this one:
83 |     # if not DEEPSEEK_API_KEY:
84 |     #     print("DeepSeek API key missing.")
85 |     #     return None
86 |     # client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")
87 |     # ---------------------------------------------------------------------
88 | 
89 |     try:
90 |         response = client.chat.completions.create(
91 |             # -----------------------------------------------------------------
92 |             # To use OpenAI, uncomment the following line:
93 |             model="gpt-4o",
94 |             # To use DeepSeek, comment out the above line and uncomment this one:
95 |             # model="deepseek-chat",
96 |             # -----------------------------------------------------------------
97 |             messages=[
98 |                 {
99 |                     "role": "system",
100 |                     "content": "You are a sustainability data extraction specialist. Return ONLY valid markdown tables.",
101 |                 },
102 |                 {"role": "user", "content": _build_llm_prompt(markdown_content)},
103 |             ],
104 |             temperature=1,
105 |             max_tokens=4000,
106 |         )
107 |         return response.choices[0].message.content.strip()
108 |     except Exception as e:
109 |         print(f"API error: {str(e)}")
110 |         return None
111 | 
112 | 
113 | def _build_llm_prompt(markdown_data: str) -> str:
114 |     return f"""
115 | You are given sustainability report tables as markdown below:
116 | {markdown_data}
117 | 
118 | 
119 | 
120 | 
121 | Please perform the following steps:
122 | 
123 | 
124 | 
125 | 
126 | 1. Identify the table(s) with the most complete year-by-year data for
127 |  Scope 1, Scope 2 (market-based), and Scope 2 (location-based)
128 |  from the provided markdown.
129 |  - Use judgment to select tables with the most complete and likely
130 |    accurate data across all years.
131 |  - Prioritize completeness and consistency.
132 |  - For Scope 2, include both market-based and location-based data if
133 |    available, and explicitly note which is which.
134 |  - Convert all values to tCO2e and keep units consistent across years.
135 |  - Use null for years where data is missing or unavailable.
136 | 
137 | 
138 | 
139 | 
140 | 2. Create a **"Key Table"** in Markdown with columns for:
141 |  | Category | Year | Emissions (tCO2e) |
142 |  The rows should be:
143 |    - Scope 1
144 |    - Scope 2 (Market-based)
145 |    - Scope 2 (Location-based)
146 |  Include data for as many years as can be found (e.g., 2020, 2021, 2022, 2023).
147 |  Convert all values to tCO2e. Use null for years where data is missing.
148 | 
149 | 
150 | 
151 | 
152 | 3. Create four additional Markdown tables (breakdown tables) if
153 |  information is available; otherwise, return them with "No Data" or "N/A":
154 |  - **Scope 1 Breakdown**:
155 |    | Scope 1 Source / Subcategory | Year | Emissions (tCO2e) |
156 |  - **Scope 2 Market-based Breakdown**:
157 |    | Region or Business Unit | Year | Emissions (tCO2e) |
158 |  - **Scope 2 Location-based Breakdown**:
159 |    | Region or Business Unit | Year | Emissions (tCO2e) |
160 |  - **Scope 3 Breakdown**:
161 |    | Scope 3 Category | Year | Emissions (tCO2e) |
162 |    Always include a "Total Scope 3" row.
163 | 
164 | 
165 | 
166 | 
167 | 4. Return exactly **these five Markdown tables** in this order with titles:
168 |  A) Key Table
169 |  B) Scope 1 Breakdown
170 |  C) Scope 2 Market-based Breakdown
171 |  D) Scope 2 Location-based Breakdown
172 |  E) Scope 3 Breakdown (with Total)
173 | 
174 | 
175 | 
176 | 
177 | 5. Provide **no additional commentary**, just the five tables in Markdown format.
178 | """
```

src/utils/rag_utils.py
```
1 | import hashlib
2 | import json
3 | import logging
4 | import os
5 | import shutil  # added for cache removal
6 | from threading import Event
7 | 
8 | import pymupdf4llm
9 | from langchain.prompts import ChatPromptTemplate
10 | from langchain.retrievers.multi_vector import MultiVectorRetriever
11 | from langchain.schema import Document, StrOutputParser
12 | from langchain.storage import InMemoryStore
13 | from langchain.text_splitter import MarkdownTextSplitter
14 | from langchain_community.embeddings import HuggingFaceEmbeddings
15 | from langchain_community.vectorstores import FAISS
16 | from langchain_core.runnables import RunnableLambda, RunnablePassthrough
17 | from langchain_openai import ChatOpenAI
18 | 
19 | logger = logging.getLogger(__name__)
20 | 
21 | 
22 | # ===========================
23 | # Environment Variables
24 | # ===========================
25 | OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
26 | DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
27 | 
28 | 
29 | # ===========================
30 | # Global RAG variables
31 | # ===========================
32 | rag_chain = None
33 | rag_initialized = False
34 | pdf_path_global = None
35 | stop_rag_event = Event()
36 | 
37 | 
38 | def _pdf_md5(pdf_path: str) -> str:
39 |     """Compute an MD5 hash of the entire PDF file contents."""
40 |     md5 = hashlib.md5()
41 |     with open(pdf_path, "rb") as f:
42 |         md5.update(f.read())
43 |     return md5.hexdigest()
44 | 
45 | 
46 | def _rag_cache_dir(pdf_path: str) -> str:
47 |     """Get the base 'rag_cache' folder next to the PDF."""
48 |     return os.path.join(os.path.dirname(pdf_path), "rag_cache")
49 | 
50 | 
51 | def chunk_with_tables(pdf_path):
52 |     """Convert PDF to markdown with table preservation. Skips on error or stop event."""
53 |     if stop_rag_event.is_set():
54 |         logger.info(
55 |             "Stop RAG event triggered before chunking. Exiting chunk_with_tables early."
56 |         )
57 |         return []
58 | 
59 |     try:
60 |         md_text = pymupdf4llm.to_markdown(pdf_path, write_images=False)
61 |     except Exception as e:
62 |         logger.error(f"Cannot parse PDF text: {e}")
63 |         return []
64 | 
65 |     if stop_rag_event.is_set():
66 |         logger.info("Stop RAG event triggered after PDF->markdown. Exiting.")
67 |         return []
68 | 
69 |     splitter = MarkdownTextSplitter(chunk_size=5000, chunk_overlap=400)
70 |     chunks = splitter.split_text(md_text)
71 | 
72 |     if stop_rag_event.is_set():
73 |         logger.info("Stop RAG event triggered after splitting text. Exiting.")
74 |         return []
75 | 
76 |     return chunks
77 | 
78 | 
79 | def build_rag_system(pdf_path):
80 |     """
81 |     Build the RAG pipeline using the unfiltered PDF, checking for a cached
82 |     FAISS vector store + docstore so we can skip chunking/summarizing if already done.
83 |     """
84 |     if stop_rag_event.is_set():
85 |         logger.info("Stop RAG event triggered at start of build_rag_system.")
86 |         return None
87 | 
88 |     # 1) Attempt to load from disk cache
89 |     pdf_hash = _pdf_md5(pdf_path)
90 |     cache_folder = os.path.join(_rag_cache_dir(pdf_path), pdf_hash)
91 |     vectorstore_dir = os.path.join(cache_folder, "vectorstore")
92 |     docstore_json = os.path.join(cache_folder, "docstore.json")
93 | 
94 |     if os.path.isdir(vectorstore_dir) and os.path.isfile(docstore_json):
95 |         logger.info(
96 |             f"[RAG Cache] Found existing cache for hash={pdf_hash}. Attempting to load."
97 |         )
98 |         if stop_rag_event.is_set():
99 |             logger.info(
100 |                 "Stop event was set before loading cache. Exiting build_rag_system."
101 |             )
102 |             return None
103 |         try:
104 |             embedder = HuggingFaceEmbeddings(
105 |                 model_name="nomic-ai/nomic-embed-text-v1.5",
106 |                 model_kwargs={"device": "cpu", "trust_remote_code": True},
107 |             )
108 |             # Load the FAISS index with dangerous deserialization allowed.
109 |             vectorstore = FAISS.load_local(
110 |                 vectorstore_dir,
111 |                 embeddings=embedder,
112 |                 allow_dangerous_deserialization=True,
113 |             )
114 |             # Load docstore from JSON
115 |             with open(docstore_json, "r", encoding="utf-8") as f:
116 |                 stored_docs = json.load(f)  # list of [doc_id, doc_content]
117 |             docstore = InMemoryStore()
118 |             for doc_id, content in stored_docs:
119 |                 docstore.mset(
120 |                     [
121 |                         (
122 |                             doc_id,
123 |                             Document(page_content=content, metadata={"doc_id": doc_id}),
124 |                         )
125 |                     ]
126 |                 )
127 |             retriever = MultiVectorRetriever(
128 |                 vectorstore=vectorstore,
129 |                 docstore=docstore,
130 |                 id_key="doc_id",
131 |                 search_kwargs={"k": 3},
132 |             )
133 |             logger.info("[RAG Cache] Successfully loaded RAG cache!")
134 |             return retriever
135 | 
136 |         except Exception as e:
137 |             logger.warning(
138 |                 f"[RAG Cache] Failed to load from cache: {e}. Removing cache folder and proceeding with normal pipeline."
139 |             )
140 |             try:
141 |                 shutil.rmtree(cache_folder)
142 |             except Exception as re:
143 |                 logger.error(f"Failed to remove cache folder {cache_folder}: {re}")
144 | 
145 |     # 2) No valid cache found; proceed with chunking & summarizing.
146 |     chunks = chunk_with_tables(pdf_path)
147 |     if stop_rag_event.is_set() or not chunks:
148 |         logger.info(
149 |             "Stop RAG event triggered or no chunks found. Exiting build_rag_system."
150 |         )
151 |         return None
152 | 
153 |     summarize_prompt = ChatPromptTemplate.from_template(
154 |         """
155 | Create a concise summary of this text chunk from a sustainability report
156 | optimized for retrieval purposes.
157 | Focus on:
158 | - Key numerical data and metrics
159 | - Table and figure descriptions
160 | - Technical terms and definitions
161 | Original text: {chunk}
162 | Summary:"""
163 |     )
164 | 
165 |     # ===================================================================
166 |     # To switch to DeepSeek, comment out the OpenAI lines and uncomment
167 |     # the DeepSeek lines below:
168 |     #
169 |     summarizer = (
170 |         {"chunk": RunnablePassthrough()}
171 |         | summarize_prompt
172 |         | ChatOpenAI(
173 |             # --- OPENAI (default) ---
174 |             openai_api_key=OPENAI_API_KEY,
175 |             model="gpt-4o-mini",
176 |             # ------------------------
177 |             # --- DEEPSEEK (comment out the above lines, then uncomment below) ---
178 |             # openai_api_key=DEEPSEEK_API_KEY,
179 |             # base_url="https://api.deepseek.com",
180 |             # model="deepseek-chat",
181 |             # -------------------------------------------------------
182 |             temperature=0.2,
183 |         )
184 |         | StrOutputParser()
185 |     )
186 |     # ===================================================================
187 | 
188 |     if stop_rag_event.is_set():
189 |         logger.info("Stop RAG event triggered before summarizing. Exiting.")
190 |         return None
191 | 
192 |     summaries = summarizer.batch(chunks)
193 |     if stop_rag_event.is_set() or not summaries:
194 |         logger.info("Stop event was set after summarizing. Exiting.")
195 |         return None
196 | 
197 |     summary_docs = [
198 |         Document(page_content=s, metadata={"doc_id": str(i)})
199 |         for i, s in enumerate(summaries)
200 |     ]
201 |     original_docs = [
202 |         Document(page_content=c, metadata={"doc_id": str(i)})
203 |         for i, c in enumerate(chunks)
204 |     ]
205 | 
206 |     embedder = HuggingFaceEmbeddings(
207 |         model_name="nomic-ai/nomic-embed-text-v1.5",
208 |         model_kwargs={"device": "cpu", "trust_remote_code": True},
209 |     )
210 | 
211 |     if stop_rag_event.is_set():
212 |         logger.info("Stop RAG event triggered before embedding. Exiting.")
213 |         return None
214 | 
215 |     vectorstore = FAISS.from_documents(summary_docs, embedder)
216 |     docstore = InMemoryStore()
217 |     docstore.mset([(str(i), original_docs[i]) for i in range(len(original_docs))])
218 | 
219 |     # 3) Save new cache if not stopped
220 |     if not stop_rag_event.is_set():
221 |         try:
222 |             os.makedirs(cache_folder, exist_ok=True)
223 |             vectorstore.save_local(vectorstore_dir)
224 |             # Save docstore to JSON
225 |             doc_data = []
226 |             for i, c in enumerate(chunks):
227 |                 doc_data.append((str(i), c))
228 |             with open(docstore_json, "w", encoding="utf-8") as f:
229 |                 json.dump(doc_data, f, indent=2)
230 |             logger.info(f"[RAG Cache] Saved new RAG cache to {cache_folder}")
231 |         except Exception as e:
232 |             logger.error(f"[RAG Cache] Failed to save cache: {e}")
233 | 
234 |     retriever = MultiVectorRetriever(
235 |         vectorstore=vectorstore,
236 |         docstore=docstore,
237 |         id_key="doc_id",
238 |         search_kwargs={"k": 3},
239 |     )
240 | 
241 |     return retriever
242 | 
243 | 
244 | def build_final_system(pdf_path):
245 |     """
246 |     Wrap the retriever in a final prompt chain that answers user queries.
247 |     """
248 |     if stop_rag_event.is_set():
249 |         logging.info("Stop RAG event triggered at start of build_final_system.")
250 |         return None
251 | 
252 |     retriever = build_rag_system(pdf_path)
253 |     if stop_rag_event.is_set() or retriever is None:
254 |         logging.info(
255 |             "Stop RAG event triggered or retriever is None. Exiting build_final_system."
256 |         )
257 |         return None
258 | 
259 |     prompt = ChatPromptTemplate.from_template(
260 |         """
261 | Analyze this parsed text and poorly formatted markdown tables from a sustainability report:
262 | {context}
263 | 
264 | 
265 | Respond as a sustainability report assistant providing relevant information in detail.
266 | Create your own tables if applicable. If data is not available, say "Data not available".
267 | 
268 | 
269 | Question: {input}
270 | """
271 |     )
272 | 
273 |     if stop_rag_event.is_set():
274 |         logging.info(
275 |             "Stop RAG event triggered before returning final pipeline. Exiting build_final_system."
276 |         )
277 |         return None
278 | 
279 |     # ===================================================================
280 |     # To switch to DeepSeek, comment out the OpenAI lines and uncomment
281 |     # the DeepSeek lines below:
282 |     #
283 |     final_pipeline = (
284 |         {
285 |             "context": retriever
286 |             | RunnableLambda(lambda docs: "\n\n".join(d.page_content for d in docs)),
287 |             "input": RunnablePassthrough(),
288 |         }
289 |         | prompt
290 |         | ChatOpenAI(
291 |             # --- OPENAI ---
292 |             openai_api_key=OPENAI_API_KEY,
293 |             model="gpt-4o",
294 |             # ------------------------
295 |             # --- DEEPSEEK ---
296 |             # openai_api_key=DEEPSEEK_API_KEY,
297 |             # base_url="https://api.deepseek.com",
298 |             # model="deepseek-chat",
299 |             # -------------------------------------------------------
300 |             temperature=0.2,
301 |         )
302 |         | StrOutputParser()
303 |     )
304 | 
305 |     return final_pipeline
```

src/utils/standardize_table.py
```
1 | import os
2 | import re
3 | 
4 | import dotenv
5 | import numpy as np
6 | import pandas as pd
7 | 
8 | 
9 | def save_raw_data(df, output_path):
10 |     """
11 |     Save the raw data to a specified file path in CSV format.
12 |     """
13 |     df.to_csv(output_path, index=False)
14 |     print(f"Raw data saved at: {output_path}")
15 | 
16 | 
17 | def standardize_emissions_table(raw_data):
18 | 
19 |     renamed_columns = {}
20 |     for col in raw_data.columns:
21 |         clean_col = re.sub(r"[^a-zA-Z0-9 ]", " ", col).strip()
22 |         clean_col = " ".join(clean_col.split())  # Remove double spaces
23 |         match = re.search(r"(?:FY|fy|Year)?\D*(\d{4}|\d{2})", clean_col)
24 |         if match:
25 |             year = match.group(1)
26 |             if len(year) == 2:
27 |                 year = f"20{year}" if int(year) >= 10 else f"19{year}"
28 |             renamed_columns[col] = year
29 | 
30 |     raw_data = raw_data.rename(columns=renamed_columns)
31 |     financial_years = [
32 |         year for year in renamed_columns.values() if re.match(r"\b20\d{2}\b", year)
33 |     ]
34 | 
35 |     # Define regex patterns for Scope 1, Scope 2 Market, and Scope 2 Location
36 |     scope_1_pattern = r"scope\s*1"
37 |     scope_2_market_pattern = r"scope\s*2.*market"
38 |     scope_2_location_pattern = r"scope\s*2.*location"
39 |     scope_2_general_pattern = r"\bscope\s*2\b"
40 | 
41 |     # Identify the parameter column
42 |     parameter_col_index = None
43 |     for idx in range(len(raw_data.columns)):
44 |         if (
45 |             raw_data.iloc[:, idx]
46 |             .astype(str)
47 |             .str.contains(scope_1_pattern, case=False, regex=True)
48 |             .any()
49 |         ):
50 |             parameter_col_index = idx
51 |             break
52 | 
53 |     # Keep only relevant columns (years + parameter column)
54 |     if parameter_col_index is not None:
55 |         parameter_col_name = raw_data.columns[parameter_col_index]
56 |         columns_to_keep = (
57 |             [parameter_col_name]
58 |             + financial_years
59 |             + (["Units"] if "Units" in raw_data.columns else [])
60 |         )
61 | 
62 |     else:
63 |         columns_to_keep = financial_years
64 | 
65 |     filtered_data = raw_data[columns_to_keep]
66 |     filtered_data = filtered_data.rename(columns={filtered_data.columns[0]: "Metric"})
67 | 
68 |     # Save a copy of the filtered table
69 |     standardized_data = filtered_data.copy()
70 | 
71 |     # Keep rows matching Scope 1, Scope 2 Market, or Scope 2 Location
72 |     filtered_rows = standardized_data[
73 |         standardized_data.iloc[:, 0]
74 |         .astype(str)
75 |         .str.contains(
76 |             f"({scope_1_pattern}|{scope_2_market_pattern}|{scope_2_location_pattern})",
77 |             case=False,
78 |             regex=True,
79 |         )
80 |     ]
81 | 
82 |     # If no Scope 2 Market or Location rows exist, add rows matching Scope 2 General
83 |     if (
84 |         not filtered_rows.iloc[:, 0]
85 |         .astype(str)
86 |         .str.contains(scope_2_market_pattern, case=False, regex=True)
87 |         .any()
88 |         and not filtered_rows.iloc[:, 0]
89 |         .astype(str)
90 |         .str.contains(scope_2_location_pattern, case=False, regex=True)
91 |         .any()
92 |     ):
93 |         additional_rows = standardized_data[
94 |             standardized_data.iloc[:, 0]
95 |             .astype(str)
96 |             .str.contains(scope_2_general_pattern, case=False, regex=True)
97 |         ]
98 |         filtered_rows = pd.concat([filtered_rows, additional_rows], axis=0)
99 | 
100 |     # Function to clean the 'Metric' column by removing numbers except for 1 and 2 and commas
101 |     def clean_scope_metric(x):
102 |         # Convert to string
103 |         x = str(x)
104 | 
105 |         # Initialize a result list to accumulate the filtered characters
106 |         result = []
107 | 
108 |         # Flag to indicate when to stop removing characters
109 |         stop_removal = False
110 | 
111 |         # Start iterating from the end of the string
112 |         for char in reversed(x):
113 |             # If we encounter '1', '2', '(', ')', or any alphabet, stop removing
114 |             if char in ["1", "2", "(", ")"] or char.isalpha():
115 |                 stop_removal = True
116 | 
117 |             if stop_removal:
118 |                 result.append(char)
119 |             else:
120 |                 # Skip digits except 1 and 2, commas, and spaces
121 |                 if char.isdigit() and char not in ["1", "2"]:
122 |                     continue
123 |                 elif char == "," or char == " ":
124 |                     continue
125 |                 # Append allowed characters
126 |                 result.append(char)
127 | 
128 |         # Reverse the result list to get the original order and join it to form the final string
129 |         cleaned_x = "".join(reversed(result))
130 | 
131 |         return cleaned_x
132 | 
133 |     # Apply the cleaning function to the 'Metric' column in filtered_rows
134 |     filtered_rows["Metric"] = filtered_rows["Metric"].apply(clean_scope_metric)
135 | 
136 |     # Apply the cleaning function to the 'Metric' column in filtered_rows
137 |     filtered_rows["Metric"] = filtered_rows["Metric"].apply(clean_scope_metric)
138 | 
139 |     filtered_rows = filtered_rows.loc[:, ~filtered_rows.T.duplicated()]
140 |     filtered_rows.replace("", np.nan, inplace=True)
141 | 
142 |     # Drop rows where all values are NaN
143 |     filtered_rows = filtered_rows.dropna(how="any")
144 |     return filtered_rows
145 | 
146 | 
147 | def clean_header(headers):
148 |     """
149 |     Clean the header by removing any columns that match 'untitled' or 'Unnamed' (case-insensitive)
150 |     after the first valid one.
151 |     """
152 |     # Define the regex pattern to match 'untitled' or 'Unnamed' (case-insensitive)
153 |     invalid_pattern = re.compile(r"untitled|Unnamed", re.IGNORECASE)
154 | 
155 |     # Find the first valid header (non-"untitled" or "Unnamed" columns)
156 |     first_valid_header_index = next(
157 |         (i for i, header in enumerate(headers) if not invalid_pattern.search(header)),
158 |         None,
159 |     )
160 | 
161 |     if first_valid_header_index is not None:
162 |         # Remove all "untitled" or "Unnamed" columns after the first valid header
163 |         new_headers = headers[: first_valid_header_index + 1] + [
164 |             header
165 |             for header in headers[first_valid_header_index + 1 :]  # noqa: E203
166 |             if not invalid_pattern.search(header)
167 |         ]
168 |     else:
169 |         # If no valid header found, keep only the first and remove others
170 |         new_headers = headers[:1] + [
171 |             header for header in headers[1:] if not invalid_pattern.search(header)
172 |         ]
173 | 
174 |     return new_headers
175 | 
176 | 
177 | def clean_rows(df):
178 |     """
179 |     Clean rows by removing NaN values and shifting the data to the left.
180 |     """
181 |     cleaned_rows = []
182 |     for _, row in df.iterrows():
183 |         # Remove NaN values and shift the data to the left
184 |         cleaned_row = row.dropna().values.tolist()
185 |         cleaned_rows.append(cleaned_row)
186 |     return cleaned_rows
187 | 
188 | 
189 | def merge_rows_with_headers(cleaned_rows, headers):
190 |     """
191 |     Merge cleaned rows back into a DataFrame, filling with NA where necessary.
192 |     """
193 |     max_len = max(len(row) for row in cleaned_rows)
194 |     # Adjust each row to match the length of the header, filling missing values with NaN
195 |     adjusted_rows = [row + [np.nan] * (max_len - len(row)) for row in cleaned_rows]
196 | 
197 |     # Ensure all rows are aligned to the headers length
198 |     return pd.DataFrame(adjusted_rows, columns=headers)
199 | 
200 | 
201 | def process_dataframe(df):
202 |     """
203 |     Process the raw CSV file and clean up the data based on specified requirements.
204 |     """
205 | 
206 |     # Clean the header by removing "Untitled" columns after the first valid one
207 |     cleaned_headers = clean_header(df.columns.tolist())
208 | 
209 |     # Clean the rows by removing NaN values and shifting to the left
210 |     cleaned_rows = clean_rows(df)
211 | 
212 |     # Merge cleaned rows back into a DataFrame, aligning with the cleaned header
213 |     cleaned_df = merge_rows_with_headers(cleaned_rows, cleaned_headers)
214 | 
215 |     return cleaned_df
216 | 
217 | 
218 | def standardize_table(data):
219 |     try:
220 |         cleaned_data = process_dataframe(data)
221 |         print(cleaned_data.head())
222 |     except Exception as e:
223 |         print(f"Table clearing failed: {e}")
224 |         return None
225 | 
226 |     try:
227 |         standardized_table = standardize_emissions_table(
228 |             cleaned_data
229 |         )  # Pass the cleaned data
230 |         return standardized_table
231 | 
232 |     except Exception as e:
233 |         print(f"Standardization failed: {e}")
234 |         return cleaned_data
235 | 
236 | 
237 | if __name__ == "__main__":
238 |     dotenv.load_dotenv()
239 |     OUTPUT_DIR = os.getenv("ROOT_OUTPUT_PATH")
240 |     file_path = os.path.join(OUTPUT_DIR, "BANK_OF_AMERICA_CORP", "esg_data.csv")
241 |     df = pd.read_csv(file_path)
242 |     try:
243 |         df = standardize_table(df)
244 |         print(df.head())
245 |         output_path = os.path.join(OUTPUT_DIR, "std_esg_data.csv")
246 |         save_raw_data(df, output_path)
247 |     except Exception as e:
248 |         print(f"Table clearing failed: {e}")
```

src/utils/units.py
```
1 | import os
2 | import re
3 | 
4 | import dotenv
5 | import pandas as pd
6 | 
7 | from src.utils.data_models import TableParsers
8 | 
9 | 
10 | def extract_units(value):
11 |     match = re.search(
12 |         r"\b(t\s*o\s*n\s*s\s*o\s*f\s*C\s*O\s*2\s*e|m\s*e\s*t\s*r\s*i\s*c\s*t\s*o\s*n\s*s\s*o\s*f\s*C\s*O\s*2\s*e|C\s*O\s*2\s*e|t\s*C\s*O\s*2\s*e|M\s*T\s*C\s*O\s*2\s*e|k\s*g\s*C\s*O\s*2\s*e|k\s*t\s*C\s*O\s*2\s*e|g\s*C\s*O\s*2\s*e|h\s*u\s*n\s*d\s*r\s*e\s*d\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|t\s*h\s*o\s*u\s*s\s*a\s*n\s*d\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|m\s*i\s*l\s*l\s*i\s*o\s*n\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|b\s*i\s*l\s*l\s*i\s*o\s*n\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|m\s*e\s*t\s*r\s*i\s*c\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|m\s*e\s*t\s*r\s*i\s*c\s*t\s*o\s*n\s*s\s*C\s*O\s*2\s*e|t\s*o\s*n\s*s\s*C\s*O\s*2\s*e|t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|\srevenue\s)\b",
13 |         str(value),
14 |         re.IGNORECASE,
15 |     )
16 | 
17 |     return match.group(0) if match else None
18 | 
19 | 
20 | def get_units_raw_input(df: pd.DataFrame):
21 |     updated_df = df.copy()
22 | 
23 |     updated_df["Units"] = None
24 |     first_unit = None
25 |     for idx, row in df.iterrows():
26 |         extracted_units = extract_units(pd.DataFrame(row).to_string())
27 |         updated_df.iloc[idx]["Units"] = extracted_units
28 | 
29 |         if first_unit is None and extract_units is not None:
30 |             first_unit = extracted_units
31 | 
32 |     updated_df["Units"] = updated_df["Units"].apply(
33 |         lambda x: first_unit if x is None else x
34 |     )
35 | 
36 |     return updated_df
37 | 
38 | 
39 | def infer_emissions_unit(max, min):
40 |     """
41 |     Infer the unit of measurement based on the numerical value.
42 |     """
43 |     if max < 7:
44 |         return "Inferred: CO₂e per FTE"  # Emissions per Full-Time Employee
45 |     elif min > 2 and max < 100:
46 |         return "Inferred: MMT CO₂e"  # Million Metric Tons
47 |     elif min > 10 and max < 500:
48 |         return "Inferred: thousand MT CO₂e"  # Thousand Metric Tons
49 |     return "Inferred: MT CO₂e"  # Metric Tons
50 | 
51 | 
52 | def clean_numeric_values(row):
53 |     # Now apply the cleaning to all columns, including the first one (Metric)
54 |     numeric_values = pd.to_numeric(
55 |         row.astype(str).str.replace(
56 |             r"(?<=\d),(?=\d{3}\b)", "", regex=True
57 |         ),  # Remove commas only for thousands
58 |         errors="coerce",  # Ignore non-numeric values, treat them as NaN
59 |     ).dropna()
60 |     return numeric_values
61 | 
62 | 
63 | def infer_units_for_rows(filtered_rows):
64 |     """
65 |     Infer emissions unit for each row based on numerical values.
66 |     """
67 |     unit_inferences = []
68 |     for idx, row in filtered_rows.iterrows():
69 |         try:
70 |             # If the row already has a valid unit, keep it
71 |             if row["Units"] not in ["", None, "Unknown"]:
72 |                 unit_inferences.append(row["Units"])
73 |                 continue
74 |         except Exception:
75 |             unit_inferences.append(None)
76 | 
77 |         # Extract numerical values from the row (excluding the first column 'Metric')
78 |         numeric_values = clean_numeric_values(row)
79 | 
80 |         if numeric_values.empty:
81 |             unit_inferences.append(None)  # No valid numerical data
82 |         else:
83 |             # Infer unit based on the maximum value in the row
84 |             inferred_unit = infer_emissions_unit(
85 |                 numeric_values.max(), numeric_values.min()
86 |             )
87 |             unit_inferences.append(inferred_unit)
88 | 
89 |     try:
90 |         # Add the inferred units as a new column
91 |         filtered_rows["Units"] = unit_inferences
92 |     except ValueError:
93 |         filtered_rows["Units"] = unit_inferences[0]
94 |     return filtered_rows
95 | 
96 | 
97 | if __name__ == "__main__":
98 |     dotenv.load_dotenv()
99 |     OUTPUT_DIR = os.getenv("ROOT_OUTPUT_PATH")
100 |     df = pd.read_csv(
101 |         os.path.join(
102 |             OUTPUT_DIR,
103 |             "NVIDA",
104 |             TableParsers.DOCLING.value,
105 |             "FY2024-NVIDIA-Corporate-Sustainability-Report-table-2.csv",
106 |         )
107 |     )
108 |     get_units_raw_input(df)
```

tests/src/find/__init__.py
```
```

tests/src/find/test_company_profile.py
```
1 | from src.find.company_profile import CompanyProfile
2 | 
3 | 
4 | class TestIsValidISIN:
5 | 
6 |     def test_with_valid_isin(self):
7 |         ISIN = "GB00BNC5T391"
8 |         result = CompanyProfile.is_valid_isin(ISIN)
9 |         assert result is True
10 | 
11 |     def test_with_invalid_isin(self):
12 |         ISIN = "apple"
13 |         result = CompanyProfile.is_valid_isin(ISIN)
14 |         assert result is False
```

tests/src/find/test_esg_reports.py
```
1 | from datetime import datetime
2 | 
3 | from src.find.esg_reports import ESGReports, SearchResult
4 | 
5 | 
6 | class TestScoreSearch:
7 | 
8 |     def test_score_search_zero(self):
9 |         search = SearchResult(
10 |             company_name="apple",
11 |             url="amazon.com",
12 |             title="macbook pro",
13 |             description="product details",
14 |         )
15 |         score = search.score_search()
16 |         assert score == 0
17 | 
18 |     def test_score_search_nonzero(self):
19 |         current_year = str(datetime.now().year)
20 |         search = SearchResult(
21 |             company_name="Nvidia",
22 |             url="www.nvidia.com",
23 |             title=f"Nvidia ESG Report {current_year}",
24 |             description="latest esg figures",
25 |         )
26 |         score = search.score_search()
27 |         assert score == 5
28 | 
29 | 
30 | class TestSortResults:
31 | 
32 |     def test_sort_results(self):
33 |         current_year = str(datetime.now().year)
34 |         company_name = "Apple"
35 |         search_results = [
36 |             {"title": "Amazon Report", "link": "www.amazon.com", "snippet": "report"},
37 |             {
38 |                 "title": f"Apple Sustainability Report {current_year}",
39 |                 "link": "www.apple.com",
40 |                 "snippet": "ESG figures",
41 |             },
42 |             {
43 |                 "title": "2023 ESG report",
44 |                 "link": "www.apple-store.com",
45 |                 "snippet": "Sustainability report for Apple",
46 |             },
47 |         ]
48 |         sorted_results = ESGReports._sort_search_reults(
49 |             company_name=company_name, search_results=search_results
50 |         )
51 |         assert sorted_results[0] == search_results[1]
52 |         assert sorted_results[1] == search_results[2]
53 |         assert sorted_results[2] == search_results[0]
```

src/static/images/emissions_map.html
```
1 | <!DOCTYPE html>
2 | <html>
3 | <head>
4 |     
5 |     <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
6 |     
7 |         <script>
8 |             L_NO_TOUCH = false;
9 |             L_DISABLE_3D = false;
10 |         </script>
11 |     
12 |     <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
13 |     <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
14 |     <script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js"></script>
15 |     <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
16 |     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>
17 |     <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
18 |     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css"/>
19 |     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"/>
20 |     <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css"/>
21 |     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css"/>
22 |     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
23 |     <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css"/>
24 |     
25 |             <meta name="viewport" content="width=device-width,
26 |                 initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
27 |             <style>
28 |                 #map_28748e7bd156afca3a16a7fad43c62fe {
29 |                     position: relative;
30 |                     width: 100.0%;
31 |                     height: 100.0%;
32 |                     left: 0.0%;
33 |                     top: 0.0%;
34 |                 }
35 |                 .leaflet-container { font-size: 1rem; }
36 |             </style>
37 |         
38 | </head>
39 | <body>
40 |     
41 |     
42 |             <div class="folium-map" id="map_28748e7bd156afca3a16a7fad43c62fe" ></div>
43 |         
44 | </body>
45 | <script>
46 |     
47 |     
48 |             var map_28748e7bd156afca3a16a7fad43c62fe = L.map(
49 |                 "map_28748e7bd156afca3a16a7fad43c62fe",
50 |                 {
51 |                     center: [20.0, 0.0],
52 |                     crs: L.CRS.EPSG3857,
53 |                     ...{
54 |   "zoom": 2,
55 |   "zoomControl": true,
56 |   "preferCanvas": false,
57 | }
58 | 
59 |                 }
60 |             );
61 | 
62 |             
63 | 
64 |         
65 |     
66 |             var tile_layer_72cfa08a165107c1cb094a1caf0a8597 = L.tileLayer(
67 |                 "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
68 |                 {
69 |   "minZoom": 0,
70 |   "maxZoom": 19,
71 |   "maxNativeZoom": 19,
72 |   "noWrap": false,
73 |   "attribution": "\u0026copy; \u003ca href=\"https://www.openstreetmap.org/copyright\"\u003eOpenStreetMap\u003c/a\u003e contributors",
74 |   "subdomains": "abc",
75 |   "detectRetina": false,
76 |   "tms": false,
77 |   "opacity": 1,
78 | }
79 | 
80 |             );
81 |         
82 |     
83 |             tile_layer_72cfa08a165107c1cb094a1caf0a8597.addTo(map_28748e7bd156afca3a16a7fad43c62fe);
84 |         
85 |     
86 |             var circle_marker_64914ac016ac7073d9c3e13320b5acb0 = L.circleMarker(
87 |                 [48.06666666666667, -122.0],
88 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0168, "stroke": true, "weight": 3}
89 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
90 |         
91 |     
92 |         var popup_9e2a71f35897978c2dc3751cbfa40b80 = L.popup({
93 |   "maxWidth": "100%",
94 | });
95 | 
96 |         
97 |             
98 |                 var html_b66b19c481dc19271a05d38ec8269376 = $(`<div id="html_b66b19c481dc19271a05d38ec8269376" style="width: 100.0%; height: 100.0%;">Apple - 16.8 CO2</div>`)[0];
99 |                 popup_9e2a71f35897978c2dc3751cbfa40b80.setContent(html_b66b19c481dc19271a05d38ec8269376);
100 |             
101 |         
102 | 
103 |         circle_marker_64914ac016ac7073d9c3e13320b5acb0.bindPopup(popup_9e2a71f35897978c2dc3751cbfa40b80)
104 |         ;
105 | 
106 |         
107 |     
108 |     
109 |             var circle_marker_3eb0a02e0002afc2ee89d4be2aa7667c = L.circleMarker(
110 |                 [48.06666666666667, -121.78333333333333],
111 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0154, "stroke": true, "weight": 3}
112 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
113 |         
114 |     
115 |         var popup_4333922652221e4bd3c139694688ab52 = L.popup({
116 |   "maxWidth": "100%",
117 | });
118 | 
119 |         
120 |             
121 |                 var html_0c91f92c61122ec41c8dd1cd05cf3f8e = $(`<div id="html_0c91f92c61122ec41c8dd1cd05cf3f8e" style="width: 100.0%; height: 100.0%;">Microsoft - 15.4 CO2</div>`)[0];
122 |                 popup_4333922652221e4bd3c139694688ab52.setContent(html_0c91f92c61122ec41c8dd1cd05cf3f8e);
123 |             
124 |         
125 | 
126 |         circle_marker_3eb0a02e0002afc2ee89d4be2aa7667c.bindPopup(popup_4333922652221e4bd3c139694688ab52)
127 |         ;
128 | 
129 |         
130 |     
131 |     
132 |             var circle_marker_11a01ce12d2672567afd8ecbddf67842 = L.circleMarker(
133 |                 [37.7, -121.86666666666666],
134 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0249, "stroke": true, "weight": 3}
135 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
136 |         
137 |     
138 |         var popup_e808644f3710bb679dcf2258aa0f9caa = L.popup({
139 |   "maxWidth": "100%",
140 | });
141 | 
142 |         
143 |             
144 |                 var html_f7d626037641282734d19db38e41981f = $(`<div id="html_f7d626037641282734d19db38e41981f" style="width: 100.0%; height: 100.0%;">Alphabet - 24.9 CO2</div>`)[0];
145 |                 popup_e808644f3710bb679dcf2258aa0f9caa.setContent(html_f7d626037641282734d19db38e41981f);
146 |             
147 |         
148 | 
149 |         circle_marker_11a01ce12d2672567afd8ecbddf67842.bindPopup(popup_e808644f3710bb679dcf2258aa0f9caa)
150 |         ;
151 | 
152 |         
153 |     
154 |     
155 |             var circle_marker_a8b16ae5869115b545eab894d0f1ef80 = L.circleMarker(
156 |                 [18.466666666666665, 42.88333333333333],
157 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.047, "stroke": true, "weight": 3}
158 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
159 |         
160 |     
161 |         var popup_a66932cb678652700bf8b9e00cce5b74 = L.popup({
162 |   "maxWidth": "100%",
163 | });
164 | 
165 |         
166 |             
167 |                 var html_76928a2b3b998a5ace132383eaa2eb8f = $(`<div id="html_76928a2b3b998a5ace132383eaa2eb8f" style="width: 100.0%; height: 100.0%;">Saudi Aramco - 47.0 CO2</div>`)[0];
168 |                 popup_a66932cb678652700bf8b9e00cce5b74.setContent(html_76928a2b3b998a5ace132383eaa2eb8f);
169 |             
170 |         
171 | 
172 |         circle_marker_a8b16ae5869115b545eab894d0f1ef80.bindPopup(popup_a66932cb678652700bf8b9e00cce5b74)
173 |         ;
174 | 
175 |         
176 |     
177 |     
178 |             var circle_marker_5f13314c63e1c3c55fe7639730dd4401 = L.circleMarker(
179 |                 [37.61666666666667, -119.4],
180 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0122, "stroke": true, "weight": 3}
181 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
182 |         
183 |     
184 |         var popup_3f02147392a63fd6b1fc2636578f334a = L.popup({
185 |   "maxWidth": "100%",
186 | });
187 | 
188 |         
189 |             
190 |                 var html_10dc1c013bd59ea741803d09c53facb4 = $(`<div id="html_10dc1c013bd59ea741803d09c53facb4" style="width: 100.0%; height: 100.0%;">Nvidia - 12.2 CO2</div>`)[0];
191 |                 popup_3f02147392a63fd6b1fc2636578f334a.setContent(html_10dc1c013bd59ea741803d09c53facb4);
192 |             
193 |         
194 | 
195 |         circle_marker_5f13314c63e1c3c55fe7639730dd4401.bindPopup(popup_3f02147392a63fd6b1fc2636578f334a)
196 |         ;
197 | 
198 |         
199 |     
200 |     
201 |             var circle_marker_c69a962f7ba2a611ad4b1c942175f6c6 = L.circleMarker(
202 |                 [48.016666666666666, -121.43333333333334],
203 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0261, "stroke": true, "weight": 3}
204 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
205 |         
206 |     
207 |         var popup_012bb4db1cf4a42af708bacacf6c552c = L.popup({
208 |   "maxWidth": "100%",
209 | });
210 | 
211 |         
212 |             
213 |                 var html_48731b4e40c90083994029fae32faef1 = $(`<div id="html_48731b4e40c90083994029fae32faef1" style="width: 100.0%; height: 100.0%;">Amazon  - 26.1 CO2</div>`)[0];
214 |                 popup_012bb4db1cf4a42af708bacacf6c552c.setContent(html_48731b4e40c90083994029fae32faef1);
215 |             
216 |         
217 | 
218 |         circle_marker_c69a962f7ba2a611ad4b1c942175f6c6.bindPopup(popup_012bb4db1cf4a42af708bacacf6c552c)
219 |         ;
220 | 
221 |         
222 |     
223 |     
224 |             var circle_marker_6fc1147b06f4261819481ca4c740ab4a = L.circleMarker(
225 |                 [25.266666666666666, 120.0],
226 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0137, "stroke": true, "weight": 3}
227 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
228 |         
229 |     
230 |         var popup_8564a82e9b445b9aba8fd338bd4429bb = L.popup({
231 |   "maxWidth": "100%",
232 | });
233 | 
234 |         
235 |             
236 |                 var html_839d0d3c36a32e60c7c42fb868c38307 = $(`<div id="html_839d0d3c36a32e60c7c42fb868c38307" style="width: 100.0%; height: 100.0%;">Taiwan Semiconductor Company - 13.7 CO2</div>`)[0];
237 |                 popup_8564a82e9b445b9aba8fd338bd4429bb.setContent(html_839d0d3c36a32e60c7c42fb868c38307);
238 |             
239 |         
240 | 
241 |         circle_marker_6fc1147b06f4261819481ca4c740ab4a.bindPopup(popup_8564a82e9b445b9aba8fd338bd4429bb)
242 |         ;
243 | 
244 |         
245 |     
246 |     
247 |             var circle_marker_b4af2e1260d1add04da22a498b324ed4 = L.circleMarker(
248 |                 [30.033333333333335, 120.31666666666666],
249 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.01323, "stroke": true, "weight": 3}
250 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
251 |         
252 |     
253 |         var popup_93c61c0f24950aae6fc5910c924ca715 = L.popup({
254 |   "maxWidth": "100%",
255 | });
256 | 
257 |         
258 |             
259 |                 var html_638812fbb5bab5a9f9b4fa67134e4f87 = $(`<div id="html_638812fbb5bab5a9f9b4fa67134e4f87" style="width: 100.0%; height: 100.0%;">Alibaba - 13.23 CO2</div>`)[0];
260 |                 popup_93c61c0f24950aae6fc5910c924ca715.setContent(html_638812fbb5bab5a9f9b4fa67134e4f87);
261 |             
262 |         
263 | 
264 |         circle_marker_b4af2e1260d1add04da22a498b324ed4.bindPopup(popup_93c61c0f24950aae6fc5910c924ca715)
265 |         ;
266 | 
267 |         
268 |     
269 |     
270 |             var circle_marker_7cb59119f791d16cde2f7b58c773a0e1 = L.circleMarker(
271 |                 [51.85, 0.03333333333333333],
272 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0242, "stroke": true, "weight": 3}
273 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
274 |         
275 |     
276 |         var popup_d6be0fc069588e484265b8621d0364c2 = L.popup({
277 |   "maxWidth": "100%",
278 | });
279 | 
280 |         
281 |             
282 |                 var html_daa5ac16fb0f473b25f7d4fe218b1588 = $(`<div id="html_daa5ac16fb0f473b25f7d4fe218b1588" style="width: 100.0%; height: 100.0%;">HSBC - 24.2 CO2</div>`)[0];
283 |                 popup_d6be0fc069588e484265b8621d0364c2.setContent(html_daa5ac16fb0f473b25f7d4fe218b1588);
284 |             
285 |         
286 | 
287 |         circle_marker_7cb59119f791d16cde2f7b58c773a0e1.bindPopup(popup_d6be0fc069588e484265b8621d0364c2)
288 |         ;
289 | 
290 |         
291 |     
292 |     
293 |             var circle_marker_0a389d78d0cf42074c400b81d3c26577 = L.circleMarker(
294 |                 [38.3, -121.31666666666666],
295 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0154, "stroke": true, "weight": 3}
296 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
297 |         
298 |     
299 |         var popup_a6796347335801764e1b31db1873a26d = L.popup({
300 |   "maxWidth": "100%",
301 | });
302 | 
303 |         
304 |             
305 |                 var html_8b01fa5efdb8d067cda2500c658df691 = $(`<div id="html_8b01fa5efdb8d067cda2500c658df691" style="width: 100.0%; height: 100.0%;">Visa - 15.4 CO2</div>`)[0];
306 |                 popup_a6796347335801764e1b31db1873a26d.setContent(html_8b01fa5efdb8d067cda2500c658df691);
307 |             
308 |         
309 | 
310 |         circle_marker_0a389d78d0cf42074c400b81d3c26577.bindPopup(popup_a6796347335801764e1b31db1873a26d)
311 |         ;
312 | 
313 |         
314 |     
315 |     
316 |             var circle_marker_d2c6eaca981dd25b4fa2327e959cf7a3 = L.circleMarker(
317 |                 [37.75, -121.7],
318 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0327, "stroke": true, "weight": 3}
319 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
320 |         
321 |     
322 |         var popup_476233fe2b4cc4a4a9ed03a164bcc8f6 = L.popup({
323 |   "maxWidth": "100%",
324 | });
325 | 
326 |         
327 |             
328 |                 var html_c51b1e712ac450aae2161f9400b43cac = $(`<div id="html_c51b1e712ac450aae2161f9400b43cac" style="width: 100.0%; height: 100.0%;">Meta - 32.7 CO2</div>`)[0];
329 |                 popup_476233fe2b4cc4a4a9ed03a164bcc8f6.setContent(html_c51b1e712ac450aae2161f9400b43cac);
330 |             
331 |         
332 | 
333 |         circle_marker_d2c6eaca981dd25b4fa2327e959cf7a3.bindPopup(popup_476233fe2b4cc4a4a9ed03a164bcc8f6)
334 |         ;
335 | 
336 |         
337 |     
338 |     
339 |             var circle_marker_4ab322a1a83d27265bfca7b6be2ca8be = L.circleMarker(
340 |                 [30.366666666666667, -95.96666666666667],
341 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0247, "stroke": true, "weight": 3}
342 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
343 |         
344 |     
345 |         var popup_eb851943b34cf228c4a29e3307d8076b = L.popup({
346 |   "maxWidth": "100%",
347 | });
348 | 
349 |         
350 |             
351 |                 var html_96ae983299429eb20aa0271bfffc6c6d = $(`<div id="html_96ae983299429eb20aa0271bfffc6c6d" style="width: 100.0%; height: 100.0%;">Tesla  - 24.7 CO2</div>`)[0];
352 |                 popup_eb851943b34cf228c4a29e3307d8076b.setContent(html_96ae983299429eb20aa0271bfffc6c6d);
353 |             
354 |         
355 | 
356 |         circle_marker_4ab322a1a83d27265bfca7b6be2ca8be.bindPopup(popup_eb851943b34cf228c4a29e3307d8076b)
357 |         ;
358 | 
359 |         
360 |     
361 |     
362 |             var circle_marker_369b054545937e169fd60928e7905c24 = L.circleMarker(
363 |                 [37.56666666666667, -119.51666666666667],
364 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0192, "stroke": true, "weight": 3}
365 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
366 |         
367 |     
368 |         var popup_7f5bcee6a59e5aaa10234346c01838c4 = L.popup({
369 |   "maxWidth": "100%",
370 | });
371 | 
372 |         
373 |             
374 |                 var html_4023ebef175922873418aebc30452b3f = $(`<div id="html_4023ebef175922873418aebc30452b3f" style="width: 100.0%; height: 100.0%;">Broadcom - 19.2 CO2</div>`)[0];
375 |                 popup_7f5bcee6a59e5aaa10234346c01838c4.setContent(html_4023ebef175922873418aebc30452b3f);
376 |             
377 |         
378 | 
379 |         circle_marker_369b054545937e169fd60928e7905c24.bindPopup(popup_7f5bcee6a59e5aaa10234346c01838c4)
380 |         ;
381 | 
382 |         
383 |     
384 |     
385 |             var circle_marker_65ba241cb17fcf0e54a014af30f84bcf = L.circleMarker(
386 |                 [40.28333333333333, -85.73333333333333],
387 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0236, "stroke": true, "weight": 3}
388 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
389 |         
390 |     
391 |         var popup_487fbcb90f10712bcf8824bd0b20581b = L.popup({
392 |   "maxWidth": "100%",
393 | });
394 | 
395 |         
396 |             
397 |                 var html_c1f2d0881d368944a6d9c552091f3d63 = $(`<div id="html_c1f2d0881d368944a6d9c552091f3d63" style="width: 100.0%; height: 100.0%;">Eli Lilly - 23.6 CO2</div>`)[0];
398 |                 popup_487fbcb90f10712bcf8824bd0b20581b.setContent(html_c1f2d0881d368944a6d9c552091f3d63);
399 |             
400 |         
401 | 
402 |         circle_marker_65ba241cb17fcf0e54a014af30f84bcf.bindPopup(popup_487fbcb90f10712bcf8824bd0b20581b)
403 |         ;
404 | 
405 |         
406 |     
407 |     
408 |             var circle_marker_3db646b9255ce2c99b2903ba3d6fbce6 = L.circleMarker(
409 |                 [41.43333333333333, -93.45],
410 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0262, "stroke": true, "weight": 3}
411 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
412 |         
413 |     
414 |         var popup_5d8208d47170733ae5e69bc7faf68860 = L.popup({
415 |   "maxWidth": "100%",
416 | });
417 | 
418 |         
419 |             
420 |                 var html_52dad4f302d1cec05062bb4c0dc37f03 = $(`<div id="html_52dad4f302d1cec05062bb4c0dc37f03" style="width: 100.0%; height: 100.0%;">Berkshire Hathaway - 26.2 CO2</div>`)[0];
421 |                 popup_5d8208d47170733ae5e69bc7faf68860.setContent(html_52dad4f302d1cec05062bb4c0dc37f03);
422 |             
423 |         
424 | 
425 |         circle_marker_3db646b9255ce2c99b2903ba3d6fbce6.bindPopup(popup_5d8208d47170733ae5e69bc7faf68860)
426 |         ;
427 | 
428 |         
429 |     
430 |     
431 |             var circle_marker_b6bed7e6e8eb3e78e66a8c9f12d55b2b = L.circleMarker(
432 |                 [36.61666666666667, -93.65],
433 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.025, "stroke": true, "weight": 3}
434 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
435 |         
436 |     
437 |         var popup_96028b6850f4c486a615d443be058755 = L.popup({
438 |   "maxWidth": "100%",
439 | });
440 | 
441 |         
442 |             
443 |                 var html_1401ad6f14d8b335c0b55de626b3d1d7 = $(`<div id="html_1401ad6f14d8b335c0b55de626b3d1d7" style="width: 100.0%; height: 100.0%;">Walmart - 25.0 CO2</div>`)[0];
444 |                 popup_96028b6850f4c486a615d443be058755.setContent(html_1401ad6f14d8b335c0b55de626b3d1d7);
445 |             
446 |         
447 | 
448 |         circle_marker_b6bed7e6e8eb3e78e66a8c9f12d55b2b.bindPopup(popup_96028b6850f4c486a615d443be058755)
449 |         ;
450 | 
451 |         
452 |     
453 |     
454 |             var circle_marker_2fa07e6aa5fe396475e669afb0b4409e = L.circleMarker(
455 |                 [22.883333333333333, 114.55],
456 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0188, "stroke": true, "weight": 3}
457 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
458 |         
459 |     
460 |         var popup_59eec27a30a39607cc0d0fffb1529dd7 = L.popup({
461 |   "maxWidth": "100%",
462 | });
463 | 
464 |         
465 |             
466 |                 var html_992b016cf52de55d845d334d57b5ba23 = $(`<div id="html_992b016cf52de55d845d334d57b5ba23" style="width: 100.0%; height: 100.0%;">Tencent - 18.8 CO2</div>`)[0];
467 |                 popup_59eec27a30a39607cc0d0fffb1529dd7.setContent(html_992b016cf52de55d845d334d57b5ba23);
468 |             
469 |         
470 | 
471 |         circle_marker_2fa07e6aa5fe396475e669afb0b4409e.bindPopup(popup_59eec27a30a39607cc0d0fffb1529dd7)
472 |         ;
473 | 
474 |         
475 |     
476 |     
477 |             var circle_marker_76d9460c3cf78356d97eb2cad4463f6b = L.circleMarker(
478 |                 [37.88333333333333, -121.55],
479 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0149, "stroke": true, "weight": 3}
480 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
481 |         
482 |     
483 |         var popup_a84dcb9b89434afa69fb80db0f69700a = L.popup({
484 |   "maxWidth": "100%",
485 | });
486 | 
487 |         
488 |             
489 |                 var html_b72dc3c384be95d429d15d0c98dd02ef = $(`<div id="html_b72dc3c384be95d429d15d0c98dd02ef" style="width: 100.0%; height: 100.0%;">Oracle - 14.9 CO2</div>`)[0];
490 |                 popup_a84dcb9b89434afa69fb80db0f69700a.setContent(html_b72dc3c384be95d429d15d0c98dd02ef);
491 |             
492 |         
493 | 
494 |         circle_marker_76d9460c3cf78356d97eb2cad4463f6b.bindPopup(popup_a84dcb9b89434afa69fb80db0f69700a)
495 |         ;
496 | 
497 |         
498 |     
499 |     
500 |             var circle_marker_8972d3da70614618fb9949829aac7379 = L.circleMarker(
501 |                 [30.116666666666667, -94.3],
502 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0437, "stroke": true, "weight": 3}
503 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
504 |         
505 |     
506 |         var popup_d9b27a6edc65142a945f10ca5c9f98e7 = L.popup({
507 |   "maxWidth": "100%",
508 | });
509 | 
510 |         
511 |             
512 |                 var html_8c8bb491c9ba70c9ae10529cd8377c97 = $(`<div id="html_8c8bb491c9ba70c9ae10529cd8377c97" style="width: 100.0%; height: 100.0%;">Exxon Mobil  - 43.7 CO2</div>`)[0];
513 |                 popup_d9b27a6edc65142a945f10ca5c9f98e7.setContent(html_8c8bb491c9ba70c9ae10529cd8377c97);
514 |             
515 |         
516 | 
517 |         circle_marker_8972d3da70614618fb9949829aac7379.bindPopup(popup_d9b27a6edc65142a945f10ca5c9f98e7)
518 |         ;
519 | 
520 |         
521 |     
522 |     
523 |             var circle_marker_d01caa22e9de5d143e73345041a08051 = L.circleMarker(
524 |                 [34.45, -83.43333333333334],
525 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0126, "stroke": true, "weight": 3}
526 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
527 |         
528 |     
529 |         var popup_b1debb8de00ec5fd9efbee974ecc269e = L.popup({
530 |   "maxWidth": "100%",
531 | });
532 | 
533 |         
534 |             
535 |                 var html_bad1c540c9a74cfde1e2dc60196960f6 = $(`<div id="html_bad1c540c9a74cfde1e2dc60196960f6" style="width: 100.0%; height: 100.0%;">Home Depot - 12.6 CO2</div>`)[0];
536 |                 popup_b1debb8de00ec5fd9efbee974ecc269e.setContent(html_bad1c540c9a74cfde1e2dc60196960f6);
537 |             
538 |         
539 | 
540 |         circle_marker_d01caa22e9de5d143e73345041a08051.bindPopup(popup_b1debb8de00ec5fd9efbee974ecc269e)
541 |         ;
542 | 
543 |         
544 |     
545 |     
546 |             var circle_marker_ac97d03a1436f8f4c7f22827f202cd78 = L.circleMarker(
547 |                 [38.28333333333333, -121.3],
548 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0344, "stroke": true, "weight": 3}
549 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
550 |         
551 |     
552 |         var popup_94b8bd533b568891e909a175166d982e = L.popup({
553 |   "maxWidth": "100%",
554 | });
555 | 
556 |         
557 |             
558 |                 var html_fbffed55c86069255c5e2b1a9aef4e48 = $(`<div id="html_fbffed55c86069255c5e2b1a9aef4e48" style="width: 100.0%; height: 100.0%;">Wells Fargo - 34.4 CO2</div>`)[0];
559 |                 popup_94b8bd533b568891e909a175166d982e.setContent(html_fbffed55c86069255c5e2b1a9aef4e48);
560 |             
561 |         
562 | 
563 |         circle_marker_ac97d03a1436f8f4c7f22827f202cd78.bindPopup(popup_94b8bd533b568891e909a175166d982e)
564 |         ;
565 | 
566 |         
567 |     
568 |     
569 |             var circle_marker_3d7bb00c3b9f49a1250ada2e438dbc48 = L.circleMarker(
570 |                 [37.4, -119.4],
571 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0156, "stroke": true, "weight": 3}
572 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
573 |         
574 |     
575 |         var popup_39e21b21438e43abafc0077898de66ab = L.popup({
576 |   "maxWidth": "100%",
577 | });
578 | 
579 |         
580 |             
581 |                 var html_7e740bb149c44a6c9d32849ab0d81e58 = $(`<div id="html_7e740bb149c44a6c9d32849ab0d81e58" style="width: 100.0%; height: 100.0%;">Netflix  - 15.6 CO2</div>`)[0];
582 |                 popup_39e21b21438e43abafc0077898de66ab.setContent(html_7e740bb149c44a6c9d32849ab0d81e58);
583 |             
584 |         
585 | 
586 |         circle_marker_3d7bb00c3b9f49a1250ada2e438dbc48.bindPopup(popup_39e21b21438e43abafc0077898de66ab)
587 |         ;
588 | 
589 |         
590 |     
591 |     
592 |             var circle_marker_3c2fdfe43d952d1cf8d2c9a5800b4b03 = L.circleMarker(
593 |                 [37.833333333333336, 127.05],
594 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.015, "stroke": true, "weight": 3}
595 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
596 |         
597 |     
598 |         var popup_369566de65e9e115ec09218696189d4a = L.popup({
599 |   "maxWidth": "100%",
600 | });
601 | 
602 |         
603 |             
604 |                 var html_d95fa9400c5c92ab9d7bab81c20df69b = $(`<div id="html_d95fa9400c5c92ab9d7bab81c20df69b" style="width: 100.0%; height: 100.0%;">Samsung - 15.0 CO2</div>`)[0];
605 |                 popup_369566de65e9e115ec09218696189d4a.setContent(html_d95fa9400c5c92ab9d7bab81c20df69b);
606 |             
607 |         
608 | 
609 |         circle_marker_3c2fdfe43d952d1cf8d2c9a5800b4b03.bindPopup(popup_369566de65e9e115ec09218696189d4a)
610 |         ;
611 | 
612 |         
613 |     
614 |     
615 |             var circle_marker_b6bf365483868414fcefe6c6d55b4967 = L.circleMarker(
616 |                 [41.266666666666666, -71.36666666666666],
617 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0243, "stroke": true, "weight": 3}
618 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
619 |         
620 |     
621 |         var popup_c93c6b55cfc3bb27110db87a71150e13 = L.popup({
622 |   "maxWidth": "100%",
623 | });
624 | 
625 |         
626 |             
627 |                 var html_3b449678ed9b86b032e55e23b9032d14 = $(`<div id="html_3b449678ed9b86b032e55e23b9032d14" style="width: 100.0%; height: 100.0%;">Bank of America - 24.3 CO2</div>`)[0];
628 |                 popup_c93c6b55cfc3bb27110db87a71150e13.setContent(html_3b449678ed9b86b032e55e23b9032d14);
629 |             
630 |         
631 | 
632 |         circle_marker_b6bf365483868414fcefe6c6d55b4967.bindPopup(popup_c93c6b55cfc3bb27110db87a71150e13)
633 |         ;
634 | 
635 |         
636 |     
637 |     
638 |             var circle_marker_8330d1be19652a8d2b499c81c7773e4e = L.circleMarker(
639 |                 [41.266666666666666, 7.983333333333333],
640 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0238, "stroke": true, "weight": 3}
641 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
642 |         
643 |     
644 |         var popup_3e5b377d409f5fd2a620006eeb4d8585 = L.popup({
645 |   "maxWidth": "100%",
646 | });
647 | 
648 |         
649 |             
650 |                 var html_8081e7233a0c0a69baafbf4e8b8e0df7 = $(`<div id="html_8081e7233a0c0a69baafbf4e8b8e0df7" style="width: 100.0%; height: 100.0%;">Roche  - 23.8 CO2</div>`)[0];
651 |                 popup_3e5b377d409f5fd2a620006eeb4d8585.setContent(html_8081e7233a0c0a69baafbf4e8b8e0df7);
652 |             
653 |         
654 | 
655 |         circle_marker_8330d1be19652a8d2b499c81c7773e4e.bindPopup(popup_3e5b377d409f5fd2a620006eeb4d8585)
656 |         ;
657 | 
658 |         
659 |     
660 |     
661 |             var circle_marker_7bc5200ecdc1decf14552a5c1adb8858 = L.circleMarker(
662 |                 [34.25, -83.35],
663 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0242, "stroke": true, "weight": 3}
664 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
665 |         
666 |     
667 |         var popup_7ae58c45f83e9b7de4db5b19cf57d53a = L.popup({
668 |   "maxWidth": "100%",
669 | });
670 | 
671 |         
672 |             
673 |                 var html_8fdb9162fc22706766a74c4e38956773 = $(`<div id="html_8fdb9162fc22706766a74c4e38956773" style="width: 100.0%; height: 100.0%;">Coca Cola  - 24.2 CO2</div>`)[0];
674 |                 popup_7ae58c45f83e9b7de4db5b19cf57d53a.setContent(html_8fdb9162fc22706766a74c4e38956773);
675 |             
676 |         
677 | 
678 |         circle_marker_7bc5200ecdc1decf14552a5c1adb8858.bindPopup(popup_7ae58c45f83e9b7de4db5b19cf57d53a)
679 |         ;
680 | 
681 |         
682 |     
683 |     
684 |             var circle_marker_fd608d5c763ccc0e58fa903d826ad7cc = L.circleMarker(
685 |                 [51.68333333333333, 5.683333333333334],
686 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0085, "stroke": true, "weight": 3}
687 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
688 |         
689 |     
690 |         var popup_5e092e691977e7e928c9493b12dc91df = L.popup({
691 |   "maxWidth": "100%",
692 | });
693 | 
694 |         
695 |             
696 |                 var html_8ee7d47f0575b2b90d4b309818b4c74d = $(`<div id="html_8ee7d47f0575b2b90d4b309818b4c74d" style="width: 100.0%; height: 100.0%;">ASML - 8.5 CO2</div>`)[0];
697 |                 popup_5e092e691977e7e928c9493b12dc91df.setContent(html_8ee7d47f0575b2b90d4b309818b4c74d);
698 |             
699 |         
700 | 
701 |         circle_marker_fd608d5c763ccc0e58fa903d826ad7cc.bindPopup(popup_5e092e691977e7e928c9493b12dc91df)
702 |         ;
703 | 
704 |         
705 |     
706 |     
707 |             var circle_marker_a7d59023d540ac014185e37610b9ab38 = L.circleMarker(
708 |                 [49.483333333333334, 9.066666666666666],
709 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0144, "stroke": true, "weight": 3}
710 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
711 |         
712 |     
713 |         var popup_8479f9fcfb1a6eed2963a072458a62cc = L.popup({
714 |   "maxWidth": "100%",
715 | });
716 | 
717 |         
718 |             
719 |                 var html_75245c2d1b5f261efe5cea256615da1e = $(`<div id="html_75245c2d1b5f261efe5cea256615da1e" style="width: 100.0%; height: 100.0%;">SAP - 14.4 CO2</div>`)[0];
720 |                 popup_8479f9fcfb1a6eed2963a072458a62cc.setContent(html_75245c2d1b5f261efe5cea256615da1e);
721 |             
722 |         
723 | 
724 |         circle_marker_a7d59023d540ac014185e37610b9ab38.bindPopup(popup_8479f9fcfb1a6eed2963a072458a62cc)
725 |         ;
726 | 
727 |         
728 |     
729 |     
730 |             var circle_marker_1ced2bc656cfb8fe6ae163817cf0660c = L.circleMarker(
731 |                 [49.45, 2.5166666666666666],
732 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0139, "stroke": true, "weight": 3}
733 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
734 |         
735 |     
736 |         var popup_786e4e9b10506f16f427e04290f90a21 = L.popup({
737 |   "maxWidth": "100%",
738 | });
739 | 
740 |         
741 |             
742 |                 var html_cab10576333cae39b89f782781b610ab = $(`<div id="html_cab10576333cae39b89f782781b610ab" style="width: 100.0%; height: 100.0%;">LVMH - 13.9 CO2</div>`)[0];
743 |                 popup_786e4e9b10506f16f427e04290f90a21.setContent(html_cab10576333cae39b89f782781b610ab);
744 |             
745 |         
746 | 
747 |         circle_marker_1ced2bc656cfb8fe6ae163817cf0660c.bindPopup(popup_786e4e9b10506f16f427e04290f90a21)
748 |         ;
749 | 
750 |         
751 |     
752 |     
753 |             var circle_marker_1fcef5620c2182d7e7e8b2f5a55d8c6e = L.circleMarker(
754 |                 [56.266666666666666, 12.766666666666667],
755 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0232, "stroke": true, "weight": 3}
756 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
757 |         
758 |     
759 |         var popup_83b4d312d46c077bac8c49bec4a0a1ed = L.popup({
760 |   "maxWidth": "100%",
761 | });
762 | 
763 |         
764 |             
765 |                 var html_767d10e78c22d1f59cf44b19f35208cd = $(`<div id="html_767d10e78c22d1f59cf44b19f35208cd" style="width: 100.0%; height: 100.0%;">Novo Nordisk  - 23.2 CO2</div>`)[0];
766 |                 popup_83b4d312d46c077bac8c49bec4a0a1ed.setContent(html_767d10e78c22d1f59cf44b19f35208cd);
767 |             
768 |         
769 | 
770 |         circle_marker_1fcef5620c2182d7e7e8b2f5a55d8c6e.bindPopup(popup_83b4d312d46c077bac8c49bec4a0a1ed)
771 |         ;
772 | 
773 |         
774 |     
775 |     
776 |             var circle_marker_408bdf1c258dfc6543d1db737445b9d7 = L.circleMarker(
777 |                 [39.166666666666664, -83.15],
778 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0249, "stroke": true, "weight": 3}
779 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
780 |         
781 |     
782 |         var popup_37ff4bdc108e5cb55d10db440558c739 = L.popup({
783 |   "maxWidth": "100%",
784 | });
785 | 
786 |         
787 |             
788 |                 var html_c818e05b2ce26696f487b492c6e17c74 = $(`<div id="html_c818e05b2ce26696f487b492c6e17c74" style="width: 100.0%; height: 100.0%;">Procter & Gamble  - 24.9 CO2</div>`)[0];
789 |                 popup_37ff4bdc108e5cb55d10db440558c739.setContent(html_c818e05b2ce26696f487b492c6e17c74);
790 |             
791 |         
792 | 
793 |         circle_marker_408bdf1c258dfc6543d1db737445b9d7.bindPopup(popup_37ff4bdc108e5cb55d10db440558c739)
794 |         ;
795 | 
796 |         
797 |     
798 |     
799 |             var circle_marker_4a2c0524e66ddd8a6f2709b101bccaf8 = L.circleMarker(
800 |                 [47.916666666666664, -121.91666666666667],
801 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0291, "stroke": true, "weight": 3}
802 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
803 |         
804 |     
805 |         var popup_96f2bf35fe4afa5a697803bd130775c6 = L.popup({
806 |   "maxWidth": "100%",
807 | });
808 | 
809 |         
810 |             
811 |                 var html_e54aaf92261eab7a4eb2382afc50a70d = $(`<div id="html_e54aaf92261eab7a4eb2382afc50a70d" style="width: 100.0%; height: 100.0%;">Costco  - 29.1 CO2</div>`)[0];
812 |                 popup_96f2bf35fe4afa5a697803bd130775c6.setContent(html_e54aaf92261eab7a4eb2382afc50a70d);
813 |             
814 |         
815 | 
816 |         circle_marker_4a2c0524e66ddd8a6f2709b101bccaf8.bindPopup(popup_96f2bf35fe4afa5a697803bd130775c6)
817 |         ;
818 | 
819 |         
820 |     
821 |     
822 |             var circle_marker_a7cc2fb257663b0b4dd60a91f55607a7 = L.circleMarker(
823 |                 [41.05, -71.8],
824 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0161, "stroke": true, "weight": 3}
825 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
826 |         
827 |     
828 |         var popup_aab0bbd5f277014cc076deb901ba0746 = L.popup({
829 |   "maxWidth": "100%",
830 | });
831 | 
832 |         
833 |             
834 |                 var html_368649caaad2b3b9f6919977016ca042 = $(`<div id="html_368649caaad2b3b9f6919977016ca042" style="width: 100.0%; height: 100.0%;">Mastercard - 16.1 CO2</div>`)[0];
835 |                 popup_aab0bbd5f277014cc076deb901ba0746.setContent(html_368649caaad2b3b9f6919977016ca042);
836 |             
837 |         
838 | 
839 |         circle_marker_a7cc2fb257663b0b4dd60a91f55607a7.bindPopup(popup_aab0bbd5f277014cc076deb901ba0746)
840 |         ;
841 | 
842 |         
843 |     
844 |     
845 |             var circle_marker_a8350b8107f54477c068477064cd9d42 = L.circleMarker(
846 |                 [38.31666666666667, -121.33333333333333],
847 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0152, "stroke": true, "weight": 3}
848 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
849 |         
850 |     
851 |         var popup_4003c6eb668ed8e34b1350be494213fc = L.popup({
852 |   "maxWidth": "100%",
853 | });
854 | 
855 |         
856 |             
857 |                 var html_9b47d40d552b12abda9d8f1f511a9a1a = $(`<div id="html_9b47d40d552b12abda9d8f1f511a9a1a" style="width: 100.0%; height: 100.0%;">Salesforce - 15.2 CO2</div>`)[0];
858 |                 popup_4003c6eb668ed8e34b1350be494213fc.setContent(html_9b47d40d552b12abda9d8f1f511a9a1a);
859 |             
860 |         
861 | 
862 |         circle_marker_a8350b8107f54477c068477064cd9d42.bindPopup(popup_4003c6eb668ed8e34b1350be494213fc)
863 |         ;
864 | 
865 |         
866 |     
867 |     
868 |             var circle_marker_7fd894a68426804c63993a8490cc1830 = L.circleMarker(
869 |                 [41.266666666666666, -71.4],
870 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0273, "stroke": true, "weight": 3}
871 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
872 |         
873 |     
874 |         var popup_7c919e88496979412a786d567cc0857d = L.popup({
875 |   "maxWidth": "100%",
876 | });
877 | 
878 |         
879 |             
880 |                 var html_9ab9742a92d3e05ab7e819deb49bf805 = $(`<div id="html_9ab9742a92d3e05ab7e819deb49bf805" style="width: 100.0%; height: 100.0%;">JP Morgan Chase - 27.3 CO2</div>`)[0];
881 |                 popup_7c919e88496979412a786d567cc0857d.setContent(html_9ab9742a92d3e05ab7e819deb49bf805);
882 |             
883 |         
884 | 
885 |         circle_marker_7fd894a68426804c63993a8490cc1830.bindPopup(popup_7c919e88496979412a786d567cc0857d)
886 |         ;
887 | 
888 |         
889 |     
890 |     
891 |             var circle_marker_8e77b36c56cce57b7dec41e3f039c3d7 = L.circleMarker(
892 |                 [45.5, -92.33333333333333],
893 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0166, "stroke": true, "weight": 3}
894 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
895 |         
896 |     
897 |         var popup_3cf657954374f17d1465fcdbcc30766a = L.popup({
898 |   "maxWidth": "100%",
899 | });
900 | 
901 |         
902 |             
903 |                 var html_d35401bec638e8a5467209b07811a9f8 = $(`<div id="html_d35401bec638e8a5467209b07811a9f8" style="width: 100.0%; height: 100.0%;">UnitedHealth - 16.6 CO2</div>`)[0];
904 |                 popup_3cf657954374f17d1465fcdbcc30766a.setContent(html_d35401bec638e8a5467209b07811a9f8);
905 |             
906 |         
907 | 
908 |         circle_marker_8e77b36c56cce57b7dec41e3f039c3d7.bindPopup(popup_3cf657954374f17d1465fcdbcc30766a)
909 |         ;
910 | 
911 |         
912 |     
913 |     
914 |             var circle_marker_d818ee2b447f5f6abbace6fd824223aa = L.circleMarker(
915 |                 [40.81666666666667, -73.25],
916 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0201, "stroke": true, "weight": 3}
917 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
918 |         
919 |     
920 |         var popup_fda2f84d36e13e9b9eb69e8448c05f00 = L.popup({
921 |   "maxWidth": "100%",
922 | });
923 | 
924 |         
925 |             
926 |                 var html_c9c4534c4d2ed381f5f77955bc0a7c11 = $(`<div id="html_c9c4534c4d2ed381f5f77955bc0a7c11" style="width: 100.0%; height: 100.0%;">Johnson&Johnson  - 20.1 CO2</div>`)[0];
927 |                 popup_fda2f84d36e13e9b9eb69e8448c05f00.setContent(html_c9c4534c4d2ed381f5f77955bc0a7c11);
928 |             
929 |         
930 | 
931 |         circle_marker_d818ee2b447f5f6abbace6fd824223aa.bindPopup(popup_fda2f84d36e13e9b9eb69e8448c05f00)
932 |         ;
933 | 
934 |         
935 |     
936 |     
937 |             var circle_marker_af9a11974cc4a371478a61b50858c69c = L.circleMarker(
938 |                 [42.56666666666667, -85.61666666666666],
939 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0261, "stroke": true, "weight": 3}
940 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
941 |         
942 |     
943 |         var popup_a968587c88b86d35b2a9db10e2cb5155 = L.popup({
944 |   "maxWidth": "100%",
945 | });
946 | 
947 |         
948 |             
949 |                 var html_948af71d94a26bf023d47454f7e14d1c = $(`<div id="html_948af71d94a26bf023d47454f7e14d1c" style="width: 100.0%; height: 100.0%;">AbbVie - 26.1 CO2</div>`)[0];
950 |                 popup_a968587c88b86d35b2a9db10e2cb5155.setContent(html_948af71d94a26bf023d47454f7e14d1c);
951 |             
952 |         
953 | 
954 |         circle_marker_af9a11974cc4a371478a61b50858c69c.bindPopup(popup_a968587c88b86d35b2a9db10e2cb5155)
955 |         ;
956 | 
957 |         
958 |     
959 |     
960 |             var circle_marker_2615d9659958a5e52a408ae4bc10ca42 = L.circleMarker(
961 |                 [49.45, 2.5166666666666666],
962 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0166, "stroke": true, "weight": 3}
963 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
964 |         
965 |     
966 |         var popup_ca1bd868535a5f1ef8ed26373f328717 = L.popup({
967 |   "maxWidth": "100%",
968 | });
969 | 
970 |         
971 |             
972 |                 var html_1e2eebae5b0f1870e12226e184856a97 = $(`<div id="html_1e2eebae5b0f1870e12226e184856a97" style="width: 100.0%; height: 100.0%;">Hermes - 16.6 CO2</div>`)[0];
973 |                 popup_ca1bd868535a5f1ef8ed26373f328717.setContent(html_1e2eebae5b0f1870e12226e184856a97);
974 |             
975 |         
976 | 
977 |         circle_marker_2615d9659958a5e52a408ae4bc10ca42.bindPopup(popup_ca1bd868535a5f1ef8ed26373f328717)
978 |         ;
979 | 
980 |         
981 |     
982 | </script>
983 | </html>
```
