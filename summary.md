
### We are used to writing our reports in LaTeX in Overleaf, so we can will include the .zip file and also the summary in a .md file as we are asked to do.
### The .zip file will have our references in bibtex format

\section{Introduction}

Skin diseases and skin cancer are more common than many of us realize. Take melanoma, for example, the most deadly type of skin cancer, which affects hundreds of thousands of people worldwide. \cite{cancer_statistics} Spotting a dangerous skin lesion is not easy for the untrained eye. It might look like just a regular mole or a harmless rash, leading many to ignore these signs until it is potentially too late.

Technology has advanced exponentially in the recent years, which leads us to the question -  could we find a way to accurately analyze skin lesions and identify key features that would aid in the treatment and prevention of skin diseases and skin cancer? This could not only assist dermatologists in making more accurate diagnose, but also help individuals worried about new or changing spots on their skin, possibly in the form of a phone app. 

In our project, we started by examining our dataset \cite{dataset} by reading about it from the source and segmenting around 100 images manually with LabelStudio. We will use various Python libraries to explore manual segmentation and thresholding techniques and then compare these findings to our observations, aiming to identify common features and indicators of dangerous skin lesions. Ultimately, the goal is to develop a classifier algorithm that can automate this process.

\section{Our dataset}

\subsection{Introduction}

The PAD-UFES-20 dataset consists of 2298 samples of 6 different types of skin lesions. Each lesion sample has a number of features, we will list some of them here:

\begin{itemize}
\item Information about the lesion:
    \begin{itemize}
    \item lesion ID, location of the lesion, measurements, the diagnosis, symptoms, image
    \end{itemize}
\item Information about the patient:
    \begin{itemize}
    \item patient ID, age, gender, (skin) cancer history, whether the patient smokes or drinks
    \item the patient’s parents’ background
    \end{itemize}
\end{itemize}

As mentioned above, the data set contains samples of 6 different types of skin lesions - 3 of them skin cancer, and 3 of them being skin diseases. We will briefly introduce each of these and try to relate them to each other.

\begin{table}[h]
\centering
\begin{tabular}{p{0.5\textwidth} p{0.5\textwidth}}
\hline
\textbf{Skin Cancers} & \textbf{Skin Diseases} \\ \hline
Basal Cell Carcinoma (BCC) & Seborrheic Keratosis (SEK) \\
Squamous Cell Carcinoma (SCC) & Melanoma (MEL) \\
\textit{+ Bowen’s disease (BOD) - clustered with SCC} & Nevus (NEV) \\
Actinic Keratosis (ACK) &  \\
\hline
\end{tabular}
\caption{Types of samples in our dataset}
\label{tab:skin_conditions}
\end{table}

\subsection{Skin cancers}

\subsubsection{Basal Cell Carcinoma (BCC)} % Lucie
\label{sec:BCC}

Basal cell carcinoma is the most common malignant tumor, making up about 70\% of non-melanoma skin cancers. Fortunately, in most cases it is curable when diagnosed in the early stages, leading to a relatively low mortality rate. It is often described as the least aggressive form of skin cancer. However, patients who had BCC in the past are at an increased risk of developing more severe forms of skin cancer, such as \hyperref[sec:MEL]{MEL} or \hyperref[sec:SCC]{SCC}. \cite{BCC_2} 

The biggest risk factor associated with BCC is UV light exposure. This makes lighter skin phenotypes more susceptible to developing this type of cancer. \cite{BCC_1} It can arise anywhere on the body, including on scarred or burn wounds. \cite{BCC_3} BCC often has no symptoms and is characterized by its slow growth and the fact that it rarely metastasizes. It can look like a pearly lump that is shiny and pale or bright pink, which can easily go unnoticed or be mistaken for a rash or non-cancerous skin disease.

\subsubsection{Melanoma (MEL)} % Lucie
\label{sec:MEL}

\subsubsection{Squamous Cell Carcinoma (SCC)}
\label{sec:SCC}

\subsection{Skin diseases}

\subsubsection{Seborrheic Keratosis (SEK)}

\subsubsection{Actinic Keratosis (ACK)}

\subsubsection{Nevus (NEV)}



\section{Appendix}

\bibliographystyle{unsrt}
\bibliography{references}

\end{document}