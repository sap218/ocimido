#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 16:21:04 2019
@author: samantha
"""
from owlready2 import *
import owlready2

#onto_path.append(DIRECTORY HERE) # uncomment when first load, then comment again
onto = get_ontology("uveitis.owl")
onto.load()

################## CLASSES
with onto:
    class Uveitis(Thing): pass

##################
##################
##################

with onto:
    class Signs_Symptoms(Uveitis): pass
    class Infectious(Signs_Symptoms): pass
    class Non_Infectious(Signs_Symptoms): pass
    class Masquerade(Signs_Symptoms): pass
    class Undifferentiated(Signs_Symptoms): pass

##################
################## INFECTIOUS
##################
    
################## BACTERIAL
with onto:
    class Bacterial(Infectious): pass
with onto:
    class Mycobacterium_Tuberculosis(Bacterial): pass
    class Ocular_ONLY(Mycobacterium_Tuberculosis): pass
    class With_Extraocular_Involvement(Mycobacterium_Tuberculosis): pass
with onto:
    class Treponema_Pallidum(Bacterial): pass
    class Ocular_ONLY(Treponema_Pallidum): pass 
    class With_Extraocular_Involvement(Treponema_Pallidum): pass
with onto:
    class Bartonella_Henselae(Bacterial): pass
    class Ocular_ONLY(Bartonella_Henselae): pass 
    class With_Extraocular_Involvement(Bartonella_Henselae): pass
with onto:
    class Borrelia_Burgdorferi(Bacterial): pass
    class Ocular_ONLY(Borrelia_Burgdorferi): pass 
    class With_Extraocular_Involvement(Borrelia_Burgdorferi): pass
with onto:
    class Other_Bacterial(Bacterial): pass
    class Specify(Other_Bacterial): pass

################## VIRAL
with onto:
    class Viral(Infectious): pass
with onto:
    class HSV1(Viral): pass
    class Anterior_Uveitis(HSV1): pass
    class Keratouveitis(HSV1): pass
    class Acute_Retinal_Necrosis(HSV1): pass
    class Progressive_Outer(HSV1): pass
    class Retinal_Necrosis(HSV1): pass
with onto:
    class HSV2(Viral): pass
    class Anterior_Uveitis(HSV2): pass
    class Keratouveitis(HSV2): pass
    class Acute_Retinal_Necrosis(HSV2): pass
    class Progressive_Outer(HSV2): pass
    class Retinal_Necrosis(HSV2): pass
with onto:
    class VZV(Viral): pass
    class Anterior_Uveitis(VZV): pass
    class Keratouveitis(VZV): pass
    class Acute_Retinal_Necrosis(VZV): pass
    class Progressive_Outer(VZV): pass
    class Retinal_Necrosis(VZV): pass
with onto:
    class CMV(Viral): pass
    class Anterior_Uveitis(CMV): pass
    class Keratouveitis(CMV): pass
    class Acute_Retinal_Necrosis(CMV): pass
    class Progressive_Outer(CMV): pass
    class Retinal_Necrosis(CMV): pass
with onto:
    class Viral_Syndrome_UNDIFFERENTIATED(Viral): pass
    class Anterior_Uveitis(Viral_Syndrome_UNDIFFERENTIATED): pass
    class Keratouveitis(Viral_Syndrome_UNDIFFERENTIATED): pass
    class Acute_Retinal_Necrosis(Viral_Syndrome_UNDIFFERENTIATED): pass
    class Progressive_Outer(Viral_Syndrome_UNDIFFERENTIATED): pass
    class Retinal_Necrosis(Viral_Syndrome_UNDIFFERENTIATED): pass
with onto:
    class Other_Viral(Viral): pass
    class Specify(Other_Viral): pass

################## FUNGAL
with onto:
    class Fungal(Infectious): pass
with onto:
    class Candida_sp(Fungal): pass
    class Aspergillus_sp(Fungal): pass
with onto:
    class Other_Fungal(Fungal): pass
    class Specify(Other_Fungal): pass

################## PARASITIC
with onto:
    class Parasitic(Infectious): pass
with onto:
    class Toxoplasma_Gondil(Parasitic): pass
    class Toxoplasma_Canis(Parasitic): pass
    class Onchocerca_Volvulus(Parasitic): pass
    class Diffuse_Unilateral_Subacute_Necrosis(Parasitic): pass
with onto:
    class Other_Parasitic(Parasitic): pass
    class Specify(Other_Parasitic): pass

################## OTHER
with onto:
    class Other(Infectious): pass
    class Specify(Other): pass

##################
################## NON_INFECTIOUS
##################
    
################## NO_SYSTEMIC
with onto:
    class No_Systemic_Disease(Non_Infectious): pass
with onto:
    class Acute_OR_Recurrant_Anterior_Uveitis(No_Systemic_Disease): pass
    class HLA_B27_positive(Acute_OR_Recurrant_Anterior_Uveitis): pass
    class HLA_B27_negative(Acute_OR_Recurrant_Anterior_Uveitis): pass
    class HLA_B27_unknown(Acute_OR_Recurrant_Anterior_Uveitis): pass
with onto:
    class Chronic_Anterior_Uveitis(No_Systemic_Disease): pass
    class Fuchs_Uveitis_Syndrome(No_Systemic_Disease): pass
with onto:
    class Intermediate_Uveitis(No_Systemic_Disease): pass
    class Pars_Planitis(Intermediate_Uveitis): pass
    class Non_Pars_Planitis(Intermediate_Uveitis): pass
with onto:
    class Acute_Posterior_Multifocal_Placoid_Pigment_Epitheliopathy(No_Systemic_Disease): pass
    class Multiple_Evanescent_White_Dot_Syndrome(No_Systemic_Disease): pass
    class Multifocal_Choroiditis_WITH_Panuveitis(No_Systemic_Disease): pass
    class Punctate_Inner_Choroidopathy(No_Systemic_Disease): pass
    class Ampiginous_Choroiditis(No_Systemic_Disease): pass
    class Birdshot_Chorioretinopathy(No_Systemic_Disease): pass
    class Serpiginous_Choroiditis(No_Systemic_Disease): pass
with onto:
    class Other_Non_Infectious_AND_No_Systemic_Disease(No_Systemic_Disease): pass
    class Specify(Other_Non_Infectious_AND_No_Systemic_Disease): pass

################## SYSTEMIC
with onto:
    class Systemic(Non_Infectious): pass
with onto:
    class Ankylosing_Spondylitis(Systemic): pass
    class Sarcoidosis(Systemic): pass
    class Multiple_Sclerosis(Systemic): pass
    class Behcet_Disease(Systemic): pass
    class Sympathetic_Ophthalmia(Systemic): pass
    class Vogt_Koyanagi_Harada_Disease(Systemic): pass
    class Tubulointerstitial_Nephritis_AND_Uveitis(Systemic): pass
    class Juvenile_Idiopathic_Arthritis(Systemic): pass
with onto:
    class Other_Non_Infectious_AND_Systemic_Disease(Systemic): pass
    class Specify(Other_Non_Infectious_AND_Systemic_Disease): pass

##################
################## MASQUERADE
##################

with onto:
    class Neoplastic(Masquerade): pass
    class Specify(Neoplastic): pass
with onto:
    class Non_Neoplastic(Masquerade): pass 

##################
##################
##################
################## LOCATIONS
##################    
##################
##################

with onto:
    class Location(Uveitis): pass
with onto:
    class Anterior(Location): pass
    class Anterior_Chamber(Anterior): pass
with onto:
    class Immediate(Location): pass
    class Vitreous(Immediate): pass
    class Pars_Planitis(Vitreous): pass
    class Non_Pars_Planitis(Vitreous): pass
with onto:
    class Posterior(Location): pass
    class Choroid_OR_Retina(Posterior): pass
    class Choroiditis(Choroid_OR_Retina): pass
    class Chorioretinitis(Choroid_OR_Retina): pass
    class Retinochoroiditis(Choroid_OR_Retina): pass
    class Retinitis(Choroid_OR_Retina): pass
    class Neuroretinitis(Choroid_OR_Retina): pass
with onto:
    class Panuveitis(Location): pass
    class Anterior_Chamber(Panuveitis): pass
    class Vitreous(Panuveitis): pass
    class Choroid_OR_Retina(Panuveitis): pass

##################
##################
##################
################## COMPLICATIONS
##################
##################
##################

with onto:
    class Complications(Uveitis): pass
with onto:
    class Cataract(Complications): pass
    class Present(Cataract): pass
    class Previous(Cataract): pass
    class Absent(Cataract): pass
with onto:
    class Glaucoma_OR_OHT(Complications): pass
    class Present(Glaucoma_OR_OHT): pass
    class Previous(Glaucoma_OR_OHT): pass
    class Absent(Glaucoma_OR_OHT): pass
with onto:
    class Macular_Oedema(Complications): pass
    class Present(Macular_Oedema): pass
    class Previous(Macular_Oedema): pass
    class Absent(Macular_Oedema): pass
with onto:
    class Epiretinal_Membrane(Complications): pass
    class Present(Epiretinal_Membrane): pass
    class Previous(Epiretinal_Membrane): pass
    class Absent(Epiretinal_Membrane): pass
with onto:
    class Other_Visual_Significant_Complication(Complications): pass
    class Present(Other_Visual_Significant_Complication): pass
    class Previous(Other_Visual_Significant_Complication): pass
    class Absent(Other_Visual_Significant_Complication): pass

with onto:
    class Visually_Significant(Present): pass
    class Visually_Insignificant(Present): pass

##################
##################
##################
################## THERAPY
##################
##################
##################

with onto:
    class Therapy(Uveitis): pass
with onto:
    class Each_Eye(Therapy): pass
with onto:
    class Topical_Corticosteroid_Therapy(Each_Eye): pass
    class Present(Topical_Corticosteroid_Therapy): pass
    class Absent(Topical_Corticosteroid_Therapy): pass
with onto:
    class Local_Therapy_within_last2yrs(Each_Eye): pass
    class Present(Local_Therapy_within_last2yrs): pass
    class Absent(Local_Therapy_within_last2yrs): pass
############
with onto:
    class Patient(Therapy): pass
with onto:
    class Oral_Corticosteroid(Patient): pass
    class Present(Oral_Corticosteroid): pass
    class Absent(Oral_Corticosteroid): pass
with onto:
    class Intravenous_Corticosteroid(Patient): pass
    class Present(Intravenous_Corticosteroid): pass
    class Absent(Intravenous_Corticosteroid): pass
with onto:
    class Intramuscular_Corticosteroid(Patient): pass
    class Present(Intramuscular_Corticosteroid): pass
    class Absent(Intramuscular_Corticosteroid): pass
with onto:
    class Other_Immunosuppressant(Patient): pass
    class Present(Other_Immunosuppressant): pass
    class Absent(Other_Immunosuppressant): pass
############
with onto:
    class Surgical(Therapy): pass
with onto:
    class Cataract(Surgical): pass
    class Present(Cataract): pass
    class Absent(Cataract): pass
with onto:
    class Glaucoma(Surgical): pass
    class Present(Glaucoma): pass
    class Absent(Glaucoma): pass
with onto:
    class Vitreo_Retinal(Surgical): pass
    class Present(Vitreo_Retinal): pass
    class Absent(Vitreo_Retinal): pass
with onto: 
    class Other_Ocular(Surgical): pass
    class Present(Other_Ocular): pass

############
with onto:
    class Specify(Present): pass
    class Dose(Present): pass
    class Frequency(Present): pass
    class Operations(Present): pass # SURGICAL
    class Dates(Present): pass

##################

onto.save()
