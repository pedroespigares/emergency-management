import os
import sys
sys.path.append(os.path.abspath('..'))

from Clases.oxygenTherapy import OxygenTherapy
from Clases.analysis import Analysis
from Clases.transfusion import Transfusion
from Clases.medication import Medication
from Clases.radiology import Radiology
from Clases.immobilization import Immobilization
from Clases.treatment import Treatment
from Clases.cpr import Cpr


class ActuationsColection():
    '''
    Gestiona los objetos de actuaciones
    '''

    def newAnalysis(self, connection, urgency, petition, hemoglobine=None, oxygen=None):
        '''
        Crea un nuevo análisis con los parámetros del
        método como atributos del mismo.
        '''
        created_analysis = Analysis(
            connection, urgency,
            petition, hemoglobine, oxygen)

        return created_analysis

    def newCpr(self, connection, urgency, cpr_type=None):
        '''
        Crea una nueva CPR con los parámetros del
        método como atributos del mismo.
        '''
        created_cpr = Cpr(connection, urgency, cpr_type)

        return created_cpr

    def newImmobilization(self, connection, urgency, imm_type=None, place=None):
        '''
        Crea una nueva Inmobilización con los parámetros
        del método como atributos del mismo.
        '''
        created_immobilization = Immobilization(
        connection, urgency, imm_type, place)

        return created_immobilization

    def newMedication(self, connection, urgency, name=None, dosage=None):
            '''
            Crea una nueva Inmobilización con los parámetros
            del método como atributos del mismo.
            '''
            created_medication = Medication(connection, urgency, name, dosage)

            return created_medication

    def newOxygenTherapy(self, connection, urgency, therapy=None):
            '''
            Crea una nueva oxigenoterapia con los parámetros
            del método como atributos del mismo.
            '''
            created_therapy = OxygenTherapy(connection, urgency, therapy)

            return created_therapy

    def newRadiology(self,
            connection,
            urgency,
            petition,
            pregnancy=None,
            contrast=None,
            informed_consent=None):
            '''
            Crea una nueva radiología con los parámetros
            del método como atributos del mismo.
            '''
            created_radiology = Radiology(
            connection,
            urgency,
            petition,
            pregnancy,
            contrast,
            informed_consent)

            return created_radiology

    def newTransfusion(self,
            connection,
            urgency,
            petition,
            blood_group=None,
            irh=None,
            previous_transfusion=None,
            religion=None,
            informed_consent=None):
            '''
            Crea una nueva transfusión con los parámetros
            del método como atributos del mismo.
            '''
            created_transfusion = Transfusion(
            connection,
            urgency,
            petition,
            blood_group,
            irh,
            previous_transfusion,
            religion,
            informed_consent)

            return created_transfusion

    def newTreatment(self, connection, urgency,
    treatment_type=None, antitetanus=None, anesthesia=None):
            '''
            Crea un nuevo tratamiento con los parámetros
            del método como atributos del mismo.
            '''
            created_treatment = Treatment(connection, urgency,
            treatment_type, antitetanus, anesthesia)

            return created_treatment
