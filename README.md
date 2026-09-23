# Inteli - Instituto de Tecnologia e Liderança

<p align="center">
<a href= "https://www.inteli.edu.br/"><img src="assets/inteli.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0"></a>
</p>

# FinSight - Default Risk Predictive Model

## Bill Hunters

## :student: Team Members:
- <a href="https://www.linkedin.com/in/bruno-martins-2b6742269/">Bruno Discacciati Vieiralves Martins</a>
- <a href="https://www.linkedin.com/in/bruno-gabriel-giordano-guilherme-kadayan-ab86762a0/">Bruno Gabriel Giordano Guilherme Kadayan
- <a href="http://www.linkedin.com/in/carlosicaro">Carlos Icaro Kauã Coelho Paiva
- <a href="http://www.linkedin.com/in/danilo-de-castro-neto">Danilo de Castro Neto
- <a href="https://www.linkedin.com/in/enzorezende/">Enzo de Araujo Rezende</a>
- <a href="https://www.linkedin.com/in/matheusscapolan/">Matheus Henrique Scapolan Silva</a>
- <a href="https://www.linkedin.com/in/victor-garcia-dos-santos/">Víctor Garcia dos Santos

## :teacher: Professors:
### Advisor
- <a href="https://www.linkedin.com/in/fabiana-martins-de-oliveira-8993b0b2/">Fabiana Martins de Oliveira</a>
### Instructors
- <a href="https://www.linkedin.com/in/rafaelwill/">Rafael Will Macedo de Araujo</a>
- <a href="https://www.linkedin.com/in/profclaudioandre/">Claudio Fernando André</a> 
- <a href="https://www.linkedin.com/in/gui-cestari/">Guilherme Henrique de Oliveira Cestari</a>
- <a href="https://www.linkedin.com/in/luciano-galdino-26191b36/">Luciano Galdino</a>
- <a href="https://www.linkedin.com/in/natalia-k-37a62052/">Natalia Varela da Rocha Kloeckner</a>

## About the Project

FinSight is a project developed in partnership with Finnet, a leading company in B2B financial connectivity solutions in Brazil, which processes over R$2.1 trillion in transactions annually and connects more than 3.2 million CNPJs (Brazilian corporate tax IDs). The project was developed as part of Module 3 of the Information Systems program at Inteli - Instituto de Tecnologia e Liderança, focused on "Logic for Prediction with Artificial Intelligence".

The core problem addressed is default management on Finnet's billing platform. Payment default poses a direct risk to the cash flow and financial health of client companies, making it a critical challenge in receivables management.

The proposed solution consists of a predictive system that can be integrated into Finnet's Luna platform, using machine learning techniques to anticipate default behavior. The model analyzes historical billing transaction data to identify patterns and provide predictive insights that enable preventive action.

The project's main objectives include:
- Developing classification models to predict payment trends (On Time, Late, Defaulted)
- Creating a probabilistic risk-scoring system to support collection decisions
- Implementing features to predict payment amounts and default rates by period

The machine learning technologies used include classification algorithms such as Random Forest, XGBoost, and Logistic Regression, implemented in Python with libraries such as Pandas, NumPy, Scikit-learn, and XGBoost. Development was carried out in Jupyter Notebooks to facilitate interactive data exploration and process documentation.

## Demo

Check out a demonstration of our solution in action:

**[Link to the Demo Video on YouTube](https://youtu.be/8iCDw3Zmq18)**

## Repository Structure

```
├── art_matematica/
│   ├── artefato_mat_pt1.ipynb
│   └── artefato_mat_pt2.ipynb
├── assets/
│   ├── Graficos de adequação de modelos.png
│   ├── JornadaUsuario-Alice.jpg
│   ├── JornadaUsuario-Cecilia.jpg
│   ├── Matriz de Risco.png
│   ├── Persona_Cecilia.png
│   ├── Persona_David.png
│   ├── SWOT.jpg
│   ├── canvaPropostaValor.png
│   ├── inteli.png
│   ├── persona_alice.jpg
│   ├── persona_marcelo.jpg
│   └── art_matematica/
├── notebooks/
│   ├── modelo_definitivo.ipynb
│   └── Notebooks Antigos/
│       ├── modelo_1_%_inadimplencia.ipynb
│       ├── modelo_2.ipynb
│       ├── modelo-3-predicao-valores.ipynb
│       ├── notebook-decision-tree-score.ipynb
│       ├── notebook-random-forest-regressor.ipynb
│       ├── notebook-xgboost-score.ipynb
│       └── notebook.ipynb
├── frontend/
│   ├── documentacao.md
│   ├── assets/
│   │   ├── finnet.png
│   │   ├── lua.png
│   │   └── modelo_preditivo.png
│   ├── app.py
│   ├── README.md
│   ├── requirements.txt
│   └── run.py
├── dados/
│   └── [CSV data files]
├── documents/
│   ├── documentacao.md
│   └── extras/
├── .gitattributes
├── .gitignore
└── README.md
```

## How to Run

### Prerequisites

- Python 3.10 or higher
- Jupyter Lab or Jupyter Notebook

### Installing Dependencies

1. Clone the repository:
```bash
git clone [REPOSITORY_URL]
cd [REPOSITORY_NAME]
```

2. Install the required dependencies:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost openpyxl jupyterlab
```

### Running the Notebooks

1. Start Jupyter Lab:
```bash
jupyter lab
```

2. Navigate to the `notebooks/` folder and open the main notebook:
   - `modelo_definitivo.ipynb` - Final model

3. Run the cells sequentially using `Shift + Enter` or use "Run All Cells" from the Cell menu.

### Data

The required data is located in the `notebooks/` and `dados/` folders. Make sure the CSV files are in the correct location before running the notebooks.

## Release History

### Sprint 1 - 08/15/2025
- **Business Understanding**: Sector context + Porter's Five Forces
- **SWOT Analysis**: Assessment of strengths, weaknesses, opportunities, and threats
- **Overall Solution Planning**: Architecture and scope definition
- **Value Proposition Canvas**: Value proposition mapping
- **Risk Matrix**: Identification and mitigation of project risks
- **Privacy Policy – LGPD**: Compliance with Brazilian data protection regulations
- **Understanding the User Experience I**: Persona development

### Sprint 2 - 08/29/2025
- **Development**: Data exploration, preprocessing, and hypothesis generation
- **Understanding the User Experience II**: User journey creation
- **Mathematics Artifact**: Normality analysis and testing of quantitative variables
- **Scaling**: Standardization/normalization of quantitative variables

### Sprint 3 - 09/12/2025
- **First Candidate Model Delivery**: Data preparation and initial modeling

### Sprint 4 - 09/26/2025
- **Model Comparison Notebook Presentation**: Comparative evaluation of different algorithms

### Sprint 5 - 10/09/2025
- **Final Model Delivery**: Full solution implementation
- **Project Compliance with Publication Criteria**: Documentation finalization
- **Final Pitch Presentation**: Presentation of results and impact

## License

This project is licensed under the Creative Commons Attribution 4.0 International License.

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/Inteli-College/2025-1B-T18-IN02-G03.git">Finsight</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/Inteli-College/2025-1B-T18-IN02-G03.git">INTELI, BRUNO DISCACCIATI VIEIRALVES MARTINS, BRUNO GABRIEL GIORDANO GUILHERME KADAYAN, CARLOS ICARO KAUÃ COELHO PAIVA, DANILO DE CASTRO NETO, ENZO ARAUJO DE REZENDE, MATHEUS HENRIQUE SCAPOLAN SILVA, VÍCTOR GARCIA DOS SANTOS</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Creative Commons Attribution 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>
