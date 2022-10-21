def show_pacient_syntax():
    print("\nSintaxis: mainPacientes.py <opcion> <texto/número>")
    print("<opcion>: Distintas opciones relativas a pacientes\n")
    print("- showAll")
    print("------------------------")
    print("- searchBySeveralDNI")
    print("- searchByDNI")
    print("- searchByHistory")
    print("- searchByName")
    print("- searchBySurnames")
    print("- searchByBirthdate")
    print("- searchByNacionality")
    print("- searchBySex")
    print("- searchBySocialSecurity")
    print("- searchByPhone")
    print("- searchByAddress")
    print("- searchByStatus")
    print("------------------------")
    print("- add")
    print("------------------------")
    print("- update")
    print("------------------------")
    print("- delete")
    print("- deleteDeadPacients")
    print("\n<texto/número>: valor a buscar")
    quit()


def show_medic_syntax():
    print("\nSintaxis: mainMédicos.py <opcion> <texto/número>")
    print("<opcion>: Distintas opciones relativas a médicos\n")
    print("- showAll")
    print("------------------------")
    print("- searchByNPC")
    print("- searchByName")
    print("- searchBySurnames")
    print("- searchBySpecialty")
    print("------------------------")
    print("- add")
    print("------------------------")
    print("- update")
    print("------------------------")
    print("- delete")
    print("\n<texto/número>: valor a buscar")
    quit()


def show_urgency_syntax():
    print("\nSintaxis: mainUrgencias.py <opcion> <texto/número>")
    print("<opcion>: Distintas opciones relativas a urgencias\n")
    print("- showAll")
    print("------------------------")
    print("- searchBySeveralEpisodes")
    print("- searchByEpisode")
    print("- searchByPacient")
    print("- searchByMedic")
    print("- searchByStatus")
    print("- searchByEntry")
    print("- searchByReason")
    print("- searchByExploration")
    print("- searchByRecomendation")
    print("- searchByExit")
    print("------------------------")
    print("- add")
    print("------------------------")
    print("- update")
    print("------------------------")
    print("- delete")
    print("- deleteExitus")
    print("- deleteHospitalization")
    print("- deleteDischarge")
    print("\n<texto/número>: valor a buscar")
    quit()


def show_actuation_syntax():
    print("\nSintaxis: mainActuaciones.py <opcion> <texto/número>")
    print("<opcion>: Distintas opciones relativas a actuaciones\n")
    print("- showAllAnaylisis")
    print("- searchAnalysisBy[SeveralUrgency/Urgency/Petition]")
    print("- searchAnalysis[Above/Below/Equal]Hemoglobine")
    print("- searchAnalysis[Above/Below/Equal]Oxygen")
    print("- [add/update/delete]Anaylisis")
    print("------------------------")
    print("- showAllCPR")
    print("- searchCPRBy[SeveralUrgency/Urgency/Type]")
    print("- [add/update/delete]CPR")
    print("------------------------")
    print("- showAllImmobilizations")
    print("- searchImmobilizationsBy[SeveralUrgency/Urgency/Type/Place]")
    print("- [add/update/delete]Immobilization")
    print("------------------------")
    print("- showAllMedications")
    print("- searchMedicationsBy[SeveralUrgency/Urgency/Name/Dosage]")
    print("- [add/update/delete]Medication")
    print("------------------------")
    print("- showAllOxygenTherapy")
    print("- searchOxygenTherapyBy[SeveralUrgency/Urgency/Therapy]")
    print("- [add/update/delete]OxygenTherapy")
    print("------------------------")
    print("- showAllRadiology")
    print(
        "- searchRadiologyBy[SeveralUrgency/Urgency/Petition/Pregnancy/Contrast/Consent]")
    print("- [add/update/delete]Radiology")
    print("------------------------")
    print("- showAllTransfusion")
    print(
        "- searchTransfusionsBy[SeveralUrgency/Urgency/Petition/BloodGroup/IRH/")
    print("  /PreviousTransfusion/Religion/Consent]")
    print("- [add/update/delete]Transfusion")
    print("------------------------")
    print("- showAllTreatment")
    print(
        "- searchTreatmentsBy[SeveralUrgency/Urgency/Type/Antitetanus/Anesthesia]")
    print("- [add/update/delete]Treatment")
    print("------------------------")
    print("\n<texto/número>: valor a buscar")
    quit()


def show_main_syntax():
    print("\nSintaxis: main.py <programa> <opción> <texto/número>")
    print("\n<programa>: Programa a llamar: \n")
    print("- pacients")
    print("- urgency")
    print("- medics")
    print("- actuations")
    print("\n<opcion>: Distintas opciones relativas al programa llamado\n")
    print("\n<texto/número>: valor a buscar")
    quit()