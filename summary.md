# Introduction
Skin diseases and skin cancer are more common than many of us realize. Take melanoma, for example, the most deadly type of skin cancer, which affects hundreds of thousands of people worldwide. \cite{cancer_statistics} Spotting a dangerous skin lesion is not easy for the untrained eye. It might look like just a regular mole or a harmless rash, leading many to ignore these signs until it is potentially too late.

Technology has advanced exponentially in the recent years, which leads us to the question -  could we find a way to accurately analyze skin lesions and identify key features that would aid in the treatment and prevention of skin diseases and skin cancer? This could not only assist dermatologists in making more accurate diagnose, but also help individuals worried about new or changing spots on their skin, possibly in the form of a phone app. 

In our project, we started by examining our dataset \cite{dataset} by reading about it from the source and segmenting around 100 images manually with LabelStudio. We will use various Python libraries to explore manual segmentation and thresholding techniques and then compare these findings to our observations, aiming to identify common features and indicators of dangerous skin lesions. Ultimately, the goal is to develop a classifier algorithm that can automate this process.

# Our Dataset
## Introduction
The PAD-UFES-20 dataset consists of 2298 samples of 6 different types of skin lesions. Each lesion sample has a number of features, we will list some of them here:

- **Information about the lesion:**
  - lesion ID, location of the lesion, measurements, the diagnosis, symptoms, image
- **Information about the patient:**
  - patient ID, age, gender, (skin) cancer history, whether the patient smokes or drinks
  - the patient’s parents’ background

As mentioned above, the data set contains samples of 6 different types of skin lesions - 3 of them skin cancer, and 3 of them being skin diseases. We will briefly introduce each of these and try to relate them to each other.

| **Skin Cancers** | **Skin Diseases** |
| ---------------- | ----------------- |
| Basal Cell Carcinoma (BCC) | Seborrheic Keratosis (SEK) |
| Squamous Cell Carcinoma (SCC) | Actinic Keratosis (ACK) |
| _+ Bowen’s disease (BOD) - clustered with SCC_ | Nevus (NEV) |
| Melanoma (MEL) |  |


## Skin cancers
### Basal Cell Carcinoma (BCC)
Basal cell carcinoma is the most common malignant tumor, making up about 70\% of non-melanoma skin cancers. Fortunately, in most cases it is curable when diagnosed in the early stages, leading to a relatively low mortality rate. It is often described as the least aggressive form of skin cancer. However, patients who had BCC in the past are at an increased risk of developing more severe forms of skin cancer, such as MEL or SCC. \cite{BCC_2} 

The biggest risk factor associated with BCC is UV light exposure. This makes lighter skin phenotypes more susceptible to developing this type of cancer. \cite{BCC_1} It can arise anywhere on the body, including on scarred or burn wounds. \cite{BCC_3} BCC often has no symptoms and is characterized by its slow growth and the fact that it rarely metastasizes. It can look like a pearly lump that is shiny and pale or bright pink, which can easily go unnoticed or be mistaken for a rash or non-cancerous skin disease.Basal cell carcinoma is the most common malignant tumor, making up about 70\% of non-melanoma skin cancers. Fortunately, in most cases it is curable when diagnosed in the early stages, leading to a relatively low mortality rate. It is often described as the least aggressive form of skin cancer. However, patients who had BCC in the past are at an increased risk of developing more severe forms of skin cancer, such as \hyperref[sec:MEL]{MEL} or \hyperref[sec:SCC]{SCC}. \cite{BCC_2} 

The biggest risk factor associated with BCC is UV light exposure. This makes lighter skin phenotypes more susceptible to developing this type of cancer. \cite{BCC_1} It can arise anywhere on the body, including on scarred or burn wounds. \cite{BCC_3} BCC often has no symptoms and is characterized by its slow growth and the fact that it rarely metastasizes. It can look like a pearly lump that is shiny and pale or bright pink, which can easily go unnoticed or be mistaken for a rash or non-cancerous skin disease.

### Melanoma (MEL)
Melanoma is the most dangerous type of skin cancer. It metastasizes rapidly throughout the body, and if not treated at an early stage, it is likely to be fatal. Only 14\% of patients with metastatic melanoma survive for five years. \cite{MEL_1}

This cancer typically presents as a change in an existing mole or the appearance of a new spot. These changes can include variations in color, shape, size, elevation, and the presence of itching or bleeding. \cite{BCC_3} The most significant risk factor for developing melanoma is UV exposure, especially from sunburn, along with a family history of melanoma. The most effective prevention against melanoma is doing regular skin checks and minimize UV exposure by using sunscreen daily. Early detection of MEL is crucial as it significantly enhances the chances of successful treatment and survival. 

### Squamous Cell Carcinoma (SCC)

## Skin diseases

### Seborrheic Keratosis (SEK)

### Actinic Keratosis (ACK)
Primarily caused by cumulative sun exposure, leading to damage in the outermost layer of the skin. AK lesions are often red or brown, with a rough, dry, or scaly texture. They may be flat or slightly raised. Various treatment options exist, including topical creams, cryotherapy (freezing), laser therapy, or surgical removal. The choice of treatment depends on the extent and characteristics of the lesions. Sun protection measures, such as using sunscreen, wearing protective clothing, and avoiding excessive sun exposure, are essential to prevent the development of ACK and reduce the risk of skin cancer.

### Nevus (NEV)
A nevus, more commonly known as a mole, is a benign (non-cancerous) cluster of pigmented cells that often appears as a small, dark brown spot on the skin.  Nevi are incredibly common, and most adults have a few of them. While generally harmless, it's important to be aware of changes in existing moles or the appearance of new ones. Some atypical nevi, known as dysplastic nevi, can have a higher risk of developing into melanoma, a type of skin cancer.

#### Key points about nevi:

 - Appearance: Nevi are usually round or oval-shaped, with a defined border.
 - Size: Most are smaller than a pencil eraser.
 - Changes: Monitor your moles for changes in size, shape, color, or if they begin bleeding or itching.
 - Medical attention: Consult a dermatologist if you notice any concerning changes to your moles or develop new, unusual-looking ones.


# Appendix
## References

@misc{cancer_statistics,
  title = {Melanoma: Statistics},
  author = {{Cancer.Net Editorial Board}},
  year = {2023},
  month = {March},
  howpublished = {\url{https://www.cancer.net/cancer-types/melanoma/statistics}},
  note = {Accessed: 26th February, 2024}
}

@data{dataset,
  author = {Pacheco, Andre G. C. and Lima, Gustavo R. and Salomão, Amanda S. and Krohling, Breno and Biral, Igor P. and de Angelo, Gabriel G. and Alves Jr, Fábio C. R. and Esgario, José G. M. and Simora, Alana C. and Castro, Pedro B. C. and Rodrigues, Felipe B. and Frasson, Patricia H. L. and Krohling, Renato A. and Knidel, Helder and Santos, Maria C. S. and Espírito Santo, Rachel B. and Macedo, Telma L. S. G. and Canuto, Tania R. P. and de Barros, Luíz F. S.},
  title = {{PAD-UFES-20: a skin lesion dataset composed of patient data and clinical images collected from smartphones}},
  year = {2020},
  publisher = {Mendeley Data},
  version = {1},
  doi = {10.17632/zr7vgbcyr2.1},
  url = {https://data.mendeley.com/datasets/zr7vgbcyr2/1}
}

@article{BCC_1,
  title={Basal cell carcinoma: biology, morphology and clinical implications},
  author={Crowson, A Neil},
  journal={Modern pathology},
  volume={19},
  pages={S127--S147},
  year={2006},
  publisher={Elsevier}
}

@article{BCC_2,
    author = {Lear, J T and Smith, A G},
    title = "{Basal cell carcinoma}",
    journal = {Postgraduate Medical Journal},
    volume = {73},
    number = {863},
    pages = {538-542},
    year = {1997},
    month = {09},
    abstract = "{Basal cell carcinoma is the commonest malignancy in Caucasians with incidence rates of 300 per 100,000 reported in the USA. Rates are increasing at over 10\\% per year leading to a lifetime risk of 30\\%. Although mortality is low, the disease is responsible for considerable morbidity and places a substantial burden on health service provision in the UK. Furthermore, lesions may recur and patients often develop multiple tumours giving major implications for treatment and follow-up. Four main types of basal cell carcinoma are seen: nodulo-ulcerative; pigmented; morpheaform and superficial. Diagnosis is by histological evaluation although many tumours have a characteristic clinical appearance. The differential diagnosis is large. Identified risk factors include male gender, skin type 1, red/blonde hair and increasing age. Patients with basal cell carcinoma are more likely to develop malignant melanoma and squamous cell carcinoma but it is still unclear whether there is a link with internal malignancy. The main treatment modalities are surgery and radiotherapy. Each has advantages and disadvantages. The choice of treatment depends on many factors. Principles of treatment include identification of high-risk patients to enable early detection, complete removal of the lesion, and careful follow-up to detect recurrence or new lesions. Approximately 10\\% of tumours recur, depending on site, size and treatment modality. Metastatic basal cell carcinoma and the association of ultraviolet radiation to basal cell carcinoma risk are reviewed.}",
    issn = {0032-5473},
    doi = {10.1136/pgmj.73.863.538},
    url = {https://doi.org/10.1136/pgmj.73.863.538},
    eprint = {https://academic.oup.com/pmj/article-pdf/73/863/538/50221088/postgradmedj-73-538.pdf},
}

@misc{BCC_3,
  title = {{Non-melanoma skin cancer}},
  organization = {Cancer Council Australia},
  year = {2023},
  url = {https://www.cancer.org.au/cancer-information/types-of-cancer/non-melanoma-skin-cancer},
  note = {Accessed: 2024-02-26}
}

@article{MEL_1,
  title={Melanoma},
  author={Miller, Arlo J and Mihm Jr, Martin C},
  journal={New England Journal of Medicine},
  volume={355},
  number={1},
  pages={51--65},
  year={2006},
  publisher={Mass Medical Soc}
}

@article{SCC1,
    title = {Squamous Cell Carcinoma},
    Website = {Healthdirect Australia},
    url = {https://www.healthdirect.gov.au/squamous-cell-carcinoma},
    note = {February 28, 2024}
}
