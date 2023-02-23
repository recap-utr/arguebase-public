# [Argumentative Microtexts](https://github.com/peldszus/arg-microtexts)

The arg-microtexts corpus features 112 short argumentative texts. All texts were originally written in German and have been professionally translated to English.

## List of the topics

- `allow_shops_to_open_on_holidays_and_sundays`

  - de: Sollte es Supermärkten und Einkaufszentren erlaubt werden an beliebigen Sonn- und Feiertagen zu öffnen?
  - en: Should shopping malls generally be allowed to open on holidays and Sundays?
  - nodeset6375, nodeset6410, nodeset6419, nodeset6449, nodeset6451, nodeset6457, nodeset6462, nodeset6466

- `health_insurance_cover_complementary_medicine`

  - de: Sollten die gesetzlichen Krankenkassen Behandlungen beim Natur- oder Heilpraktiker zahlen?
  - en: Should public health insurance cover treatments in complementary and alternative medicine?
  - nodeset6363, nodeset6370, nodeset6373, nodeset6378, nodeset6385, nodeset6386, nodeset6395, nodeset6412

- `higher_dog_poo_fines`

  - de: Sollte es höhere Geldstrafen für auf Gehwegen hinterlassene Hundehaufen geben?
  - en: Should the fine for leaving dog excrements on sideways be increased?
  - nodeset6362, nodeset6367, nodeset6371, nodeset6392, nodeset6400, nodeset6420, nodeset6452, nodeset6468

- `introduce_capital_punishment`

  - de: Sollte Deutschland die Todesstrafe einführen?
  - en: Should Germany introduce the death penalty?
  - nodeset6366, nodeset6383, nodeset6387, nodeset6391, nodeset6450, nodeset6453, nodeset6464, nodeset6469

- `public_broadcasting_fees_on_demand`

  - de: Sollte der Rundfunkbeitrag nur von denen eingefordert werden, die das Angebot der Öffentlich Rechtlichen Sender auch nutzen wollen?
  - en: Should only those viewers pay a TV licence fee who actually want to watch programs offered by public broadcasters?
  - nodeset6364, nodeset6374, nodeset6389, nodeset6446, nodeset6454, nodeset6463, nodeset6470

- `cap_rent_increases`

  - de: Sollte es eine Begrenzung für Mietpreiserhöhungen beim Wechsel des Mieters geben?
  - en: Should there be a cap on rent increases for a change of tenant?
  - nodeset6369, nodeset6377, nodeset6384, nodeset6418, nodeset6455, nodeset6465

- `charge_tuition_fees`

  - de: Sollten alle Universitäten in Deutschland Studiengebühren verlangen?
  - en: Should all universities in Germany charge tuition fees?
  - nodeset6381, nodeset6388, nodeset6394, nodeset6407, nodeset6447, nodeset6456

- `keep_retirement_at_63`

  - de: Sollte das Renteneintrittsalter auch in Zukunft bei 63 Jahren liegen?
  - en: Should the statutory retirement age remain at 63 years in the future?
  - nodeset6382, nodeset6409, nodeset6411, nodeset6416, nodeset6421, nodeset6461

- `over_the_counter_morning_after_pill`

  - de: Sollte die „Pille danach“ rezeptfrei in Apotheken erhältlich sein?
  - en: Should the the morning-after pill be sold over the counter at the pharmacy?
  - nodeset6368, nodeset6397, nodeset6402, nodeset6406, nodeset6414

- `increase_weight_of_BA_thesis_in_final_grade`

  - de: Sollte die Bachelorarbeit einen größeren Anteil an der Studien-Gesamtnote haben?
  - en: Should the weight of the BA thesis in the final grade be increased?
  - nodeset6376, nodeset6408, nodeset6448, nodeset6467

- `stricter_regulation_of_intelligence_services`

  - de: Sollten Geheimdienste stärker vom Parlament kontrolliert werden?
  - en: Should intelligence services be regulated more tightly by parliament?
  - nodeset6365, nodeset6401, nodeset6405, nodeset6458

- `EU_influence_on_political_events_in_Ukraine`

  - de: Sollte die EU auf politische Geschehen in der Ukraine Einfluss nehmen?
  - en: Should the EU exert influence on the political events in Ukraine?
  - nodeset6399, nodeset6415, nodeset6460

- `make_video_games_olympic`

  - de: Sollten Videospiele in den Reigen der Olympischen Disziplinen aufgenommen werden?
  - en: Should video games be made olympic?
  - nodeset6380, nodeset6396, nodeset6417

- `school_uniforms`

  - de: Sollten an unseren Schulen wieder Schul-Uniformen getragen werden?
  - en: Should school uniforms be worn again in our schools?
  - nodeset6372, nodeset6390, nodeset6398

- `TXL_airport_remain_operational_after_BER_opening`

  - de: Sollte der Flughafen Berlin Tegel auch nach Eröffnung vom Flughafen BER weiter in Betrieb bleiben?
  - en: Should the Berlin Tegel airport remain operational after the opening of the Berlin Brandenburg airport?
  - nodeset6403, nodeset6422, nodeset6459

- `buy_tax_evader_data_from_dubious_sources`

  - de: Sollte Deutschland CDs mit Daten von Steuersündern aus dubiosen Quellen ankaufen?
  - en: Should Germany buy CDs with tax evader data from dubious sources?
  - nodeset6379, nodeset6404

- `partial_housing_development_at_Tempelhofer_Feld`

  - de: Sollten Teile des Tempelhofer Felds für den Wohnungsbau zur Verfügung stehen?
  - en: Should parts of the Tempelhofer Feld be made available for residential construction?
  - nodeset6393, nodeset6413

- `waste_separation`

  - de: Sollte wir unseren Müll weiterhin für das Recycling trennen?
  - en: Should we continue to separate our waste for recycling?
  - nodeset6361

- `other`
  - nodeset6423, nodeset6424, nodeset6425, nodeset6426, nodeset6427, nodeset6428, nodeset6429, nodeset6430, nodeset6431, nodeset6432, nodeset6433, nodeset6434, nodeset6435, nodeset6436, nodeset6437, nodeset6438, nodeset6439, nodeset6440, nodeset6441, nodeset6442, nodeset6443, nodeset6444, nodeset6445

## Command to separate by topic (ArgGraph)

See [`split_by_topic.py`](./split_by_topic.py). Can also be used for `microtexts-v2`.

## Command to separate by topic (AIF, manually)

```python
import subprocess
from pathlib import Path

import typer

app = typer.Typer()


@app.command()
def main(source_folder: Path, target_folder: Path, case_names: str):
    source_cases = []

    for case_name in case_names.replace(" ", "").split(","):
        if case_name:
            case_name = case_name.strip()
            source_cases.append(source_folder / (case_name + ".json"))
            source_cases.append(source_folder / (case_name + ".pdf"))

    subprocess.run(["cp", *source_cases, target_folder])


if __name__ == "__main__":
    app()
```
