
CREATETABLE product(
idSERIAL primarykey','
category varchar(255)','
market varchar(255)','
brand varchar(255)','
product_name varchar(255)','
importer varchar(255)','
quantity_per_unit varchar(255)','
price_per_unit varchar(255)','
price_per_ml varchar(255)
    );

ALTER TABLE product
ALTER COLUMN quantity_per_unit TYPE integer USING (quantity_per_unit::integer)','
ALTER COLUMN price_per_unit TYPE float4 USING (price_per_unit::real)','
ALTER COLUMN price_per_ml TYPE float4 USING (price_per_ml::real);

ALTER TABLE product RENAME COLUMN category TO product_type;

--DELETE FROM product WHERE id < 6

INSERT INTO product (product_type','market','brand','product_name','importer','quantity_per_unit','price_per_unit','price_per_ml)
VALUES
('SPF'',''DE'',''ROSSMAN'',''SunOZoneAlgenExtractSPF50'',''LocalDrugstore'','200','4.9','0.02)','
('SPF'',''DE'',''ROSSMAN'',''SunOzoneMedGelSPF20'',''LocalDrugstore'',' 200','4.99','0.02)','
('SPF'',''DE'',''DM'',''SunDanceUltrasensitiveGelcremeSPF50'',''LocalDrugstore'','150','5.95','0.04)','
('SPF'',''AU'',''BondiSands'',''FragranceFreeBodylotionSPF50'',''LookFantastic'','150','6.9','0.05)','
('SPF'',''DE'',''Nivea'',''SensitiveprotectSPF30'',''LocalDrugstore'','200','10.00','0.05)','
('SPF'',''DE'',''Nivea'',''BeruhigendeTagespflege24HLSF15'',''LocalDrugstore'','50','3.65','0.07)','
('SPF'',''JP'',''NiveaJapan'',''AquaGel'',''Stylevana'','140','11.00','0.08)','
('SPF'',''JP'',''RothoMentolatum'',''SkinAquaSuperMoistureGelSPF50'',''Stylevana'','110','9.20','0.08)','
('SPF'',''DE'',''ROSSMAN'',''SunOZoneAntiAgingSPF50'',''LocalDrugstore'','50','4.49','0.09)','
('SPF'',''JP'',''Kose'',''SuncutUVPerfectGelSuperwaterproofspf50'',''Stylevana'','100','9.70','0.10)','
('SPF'',''DE'',''DM'',''BaleaNiacinamide10%moisturizerSPF30'',''LocalDrugstore'','50','4.95','0.10)','
('SPF'',''DE'',''ROSSMAN'',''SunOZoneMedfluidSPF30'',''LocalDrugstore'','50','4.99','0.10)','
('SPF'',''DE'',''ROSSMAN'',''ISANAHAMoisturizerSPF30'',''LocalDrugstore'','50','5.00','0.10)','
('SPF'',''KR'',''BLab'',''MatchaSPF'',''Stylevana'','50','5.48','0.11)','
('SPF'',''US'',''Neutrogena'',''ClearFaceSPF30'',''Amazon'','90','10.00','0.11)','
('SPF'',''FR'',''Garnier'',''BBoily/comboskintintedSPF25'',''LocalDrugstore'','50','5.95','0.12)','
('SPF'',''JP'',''OmiVerdio'',''GelMoisturizerSPF50'',''YesStyle'','80','10.00','0.13)','
('SPF'',''DE'',''DM'',''AlverdeClearBeautyGetontetagescreme'',''LocalDrugstore'','30','3.95','0.13)','
('SPF'',''JP'',''KissMeMommy'',''MildSPFGel'',''LittleWonderland'','100','15.00','0.15)','
('SPF'',''JP'',''kao'',''BioreUVAquaRichLightupessence'',''Stylevana'','70','10.90','0.16)','
('SPF'',''US'',''Aveeno'',''DailyCalmingSPF19'',''Amazon'','120','20.00','0.17)','
('SPF'',''DE'',''Nivea'',''SensitiveFaceSPF50'',''LocalDrugstore'','50','9.00','0.18)','
('SPF'',''DE'',''Nivea'',''SensitiveShineControlFaceSPF50'',''LocalDrugstore'','50','9.00','0.18)','
('SPF'',''DE'',''Nivea'',''AntiFaltenQ10PorenLSF15'',''LocalDrugstore'','50','9.95','0.20)','
('SPF'',''DE'',''JeanLen'',''SensitiveFaceSPF50'',''LocalDrugstore'','50','10.00','0.20)','
('SPF'',''FR'',''Garnier'',''AmbreSolaireAntiAgingSPF'',''LocalDrugstore'','50','10.00','0.20)','
('SPF'',''FR'',''Garnier'',''AmbreSolaireSUperUVFluid'',''LocalDrugstore'','50','10.00','0.20)','
('SPF'',''FR'',''Garnier'',''VitaminCSerumcremeSPF25'',''LocalDrugstore'','50','10.00','0.20)','
('SPF'',''US'',''Neutrogena'',''SheerZincSPF50'',''Amazon'','90','18.00','0.20)','
('SPF'',''KR'',''Mary&May'',''CicaSoothingSPF50'',''Stylevana'','50','10.42','0.21)','
('SPF'',''KR'',''COSRX'',''AloeSPF50'',''Amazon'','50','11.00','0.22)','
('SPF'',''KR'',''BeautyofJoseon'',''RiceProbioticsSPF50'',''Stylevana'','50','11.00','0.22)','
('SPF'',''JP'',''RothoMentolatum'',''HadaLaboWhitegelSPF50'',''Stylevana'','90','20.00','0.22)','
('SPF'',''JP'',''RothoMentolatum'',''SkinAquaUVSuperMoistureEssenceGold'',''Littlewonderland'','80','18.00','0.23)','
('SPF'',''KR'',''Rovectin'',''RovectinSPF'',''Stylevana'','50','12.00','0.24)','
('SPF'',''JP'',''Canmake'',''MermaidSPF50'',''YesStyle'','40','10.00','0.25)','
('SPF'',''KR'',''Coxir'',''CeramidesUVblockSPF50'',''YesStyle'','80','20.00','0.25)','
('SPF'',''KR'',''Benton'',''AirfitSPF'',''Stylevana'','50','12.77','0.26)','
('SPF'',''KR'',''ISNTREE'',''WaterGelSPF50'',''Stylevana'','50','13.00','0.26)','
('SPF'',''US'',''Cerave'',''LotionsPF25'',''Amazon'','50','13.17','0.26)','
('SPF'',''US'',''AustralianGold'',''TintedSPF50MediumtoTan'',''Amazon'','90','24.00','0.27)','
('SPF'',''DE'',''Sebamed'',''AntiRotungLSF20'',''amazon'','50','13.90','0.28)','
('SPF'',''KR'',''DRG'',''MildGreenSPF'',''Stylevana'','50','14.65','0.29)','
('SPF'',''KR'',''Misha'',''AquaGELspf50PA++++'',''Amazon'','50','15.59','0.31)','
('SPF'',''FR'',''LaRochePosay'',''AntheliosInvisibleFluid'',''docmorris'','50','16.49','0.33)','
('SPF'',''KR'',''Higgee'',''VeganSPF50'',''Stylevana'','50','16.50','0.33)','
('SPF'',''FR'',''LaRochePosay'',''AntheliosSPF50'',''Lookfantastic'','50','16.95','0.34)','
('SPF'',''KR'',''Purito'',''DailyGoSPF'',''Cosibella'','60','21.50','0.36)','
('SPF'',''JP'',''RothoMentolatum'',''SkinAquaUVMoistureMilkSPF50'',''LittleWonderland'','40','15.00','0.38)','
('SPF'',''DE'',''Eucerin'',''SunOilControl'',''Makeup.de'','50','20.00','0.40)','
('SPF'',''FR'',''LaRochePosay'',''AntheliosShakaFluidsensitiveTintedSPF50'',''Amazon'','50','21.00','0.42)','
('SPF'',''US'',''EltaMD'',''ClearSPF46'',''Amazon'','50','35.99','0.72);


