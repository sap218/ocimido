#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 16:21:04 2019
@author: samantha
"""
from owlready2 import *
import owlready2

option = input("Do you need to load in path?\t(y/n)\t")
if option == "y":
    directory = input("Paste directory:\t") 
    onto_path.append(directory) # uncomment when first load, then comment again
    pass

onto = get_ontology("uveitis.owl")
onto.load()

################## CLASSES
#with onto:
#    class Uveitis(Thing): pass

##################
##################
##################

with onto:
    class Signs_Symptoms(Thing): pass
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
    class Location(Thing): pass
with onto:
    class Anterior(Location): pass
    class Acute_Anterior(Anterior): pass
    class Idiopathic(Anterior): pass
    class Anterior_Chamber(Anterior): pass
    class Iridocyclitis(Anterior_Chamber): pass
    class Chronic_Iridocyclitis(Iridocyclitis): pass
    class Lens_Induced(Iridocyclitis): pass
    class Glaucomatocyclitic(Iridocyclitis): pass
    class Infectious_Iridocyclitis(Iridocyclitis): pass
    class Gonococcal_Iridocyclitis(Infectious_Iridocyclitis): pass
    class Hypopyon(Infectious_Iridocyclitis): pass
    class Hypopyon_Ulcer(Hypopyon): pass
with onto:
    class Chorioretinitis(Location): pass
    class Pars_Planitis(Chorioretinitis): pass
with onto:
    class Immediate(Location): pass
    class Vitreous(Immediate): pass
    class Pars_Planitis(Vitreous): pass
    class Non_Pars_Planitis(Vitreous): pass
with onto:
    class Posterior(Location): pass

    class Choroiditis(Posterior): pass
    class Chorioretinitis(Choroiditis): pass

    class Retinitis(Posterior): pass
    class Retinochoroiditis(Retinitis): pass
    class Optic_Papillitis(Retinitis): pass
    class Neuroretinitis(Optic_Papillitis): pass
with onto:
    class Panuveitis(Location): pass
    class Anterior_Chamber(Panuveitis): pass
    class Iridocyclitis(Anterior_Chamber): pass
    class Lens_Induced(Iridocyclitis): pass
    class Glaucomatocyclitic(Iridocyclitis): pass
    class Infectious_Iridocyclitis(Iridocyclitis): pass
    class Gonococcal_Iridocyclitis(Infectious_Iridocyclitis): pass
    class Hypopyon(Infectious_Iridocyclitis): pass
    class Hypopyon_Ulcer(Hypopyon): pass
    class Behcet_Syndrome(Anterior_Chamber): pass
    class Iritis(Anterior_Chamber): pass
    class Posterior_Chamber(Panuveitis): pass
    class Birdshot_Chorioretinopathy(Posterior_Chamber): pass
    class Choroiditis(Posterior_Chamber): pass
    class Chorioretinitis(Choroiditis): pass
    class Pars_Plantis(Choroiditis): pass
    class Vitreous(Panuveitis): pass
    class Choroid_OR_Retina(Panuveitis): pass
    class Ophthalmia_Sympathetic(Panuveitis): pass
with onto:
    class Suppurative(Location): pass
    class Panophthalmitis(Suppurative): pass
with onto:
    class Uveomeningoencephalitic_Syndrome(Location): pass
    class Nongranulomatous(Location): pass

##################
##################
##################
################## COMPLICATIONS
##################
##################
##################

with onto:
    class Complications(Thing): pass
with onto:
    class Cataract(Complications): pass
    class Status(Cataract): pass
with onto:
    class Glaucoma_OR_OHT(Complications): pass
    class Status(Glaucoma_OR_OHT): pass
with onto:
    class Macular_Oedema(Complications): pass
    class Status(Macular_Oedema): pass
with onto:
    class Epiretinal_Membrane(Complications): pass
    class Status(Epiretinal_Membrane): pass
with onto:
    class Other_Visual_Significant_Complication(Complications): pass
    class Status(Other_Visual_Significant_Complication): pass

with onto:
    class Visually_Significant(Status): pass
    class Visually_Insignificant(Status): pass

##################
##################
##################
################## THERAPY
##################
##################
##################

with onto:
    class Therapy(Thing): pass
with onto:
    class Each_Eye(Therapy): pass
with onto:
    class Topical_Corticosteroid_Therapy(Each_Eye): pass
    class Status(Topical_Corticosteroid_Therapy): pass
with onto:
    class Local_Therapy_within_last2yrs(Each_Eye): pass
    class Status(Local_Therapy_within_last2yrs): pass
############
with onto:
    class Patient(Therapy): pass
with onto:
    class Oral_Corticosteroid(Patient): pass
    class Status(Oral_Corticosteroid): pass
with onto:
    class Intravenous_Corticosteroid(Patient): pass
    class Status(Intravenous_Corticosteroid): pass
with onto:
    class Intramuscular_Corticosteroid(Patient): pass
    class Status(Intramuscular_Corticosteroid): pass
with onto:
    class Other_Immunosuppressant(Patient): pass
    class Status(Other_Immunosuppressant): pass
############
with onto:
    class Surgical(Therapy): pass
with onto:
    class Cataract(Surgical): pass
    class Status(Cataract): pass
with onto:
    class Glaucoma(Surgical): pass
    class Status(Glaucoma): pass
with onto:
    class Vitreo_Retinal(Surgical): pass
    class Status(Vitreo_Retinal): pass
with onto: 
    class Other_Ocular(Surgical): pass
    class Status(Other_Ocular): pass

############
with onto:
    class Specify(Status): pass
    class Dose(Status): pass
    class Frequency(Status): pass
    class Operations(Status): pass # SURGICAL
    class Dates(Status): pass

##################

onto.save()
