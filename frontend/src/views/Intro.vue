<template>
    <v-app>
        <div>
            <p class="header">  <u>Intro </u> </p>
        </div>
        
        
        <div>
            <p class="text"> Sehr geehrte Damen und Herren,  <br> <br> vielen Dank, dass Sie sich die Zeit für dieses Experiment nehmen.  <br>
              In Kooperation mit der Consileon Business Consultancy GmbH führe ich eine Studie im Rahmen meiner Masterarbeit zum Thema <b> Explainable Artificial Intelligence (XAI)</b>  mit der Anwendung in der <b>Kreditrisikobewertung von Privatkreditnehmern</b> durch. <br>
              <br> 
             Ich danke Ihnen recht herzlich für Ihre Zeit und Mühe,  <br> <br>
             Nico Boll</p>
            
        </div><br><br>

        <div>
            <p class="header"> 1. Einführung: Problemstellung und Ziel des Vorhabens </p>
            <br>
        </div>
        
        <div>
            <p class="text"> Aufgrund des enormen Potentials wird der Einsatz von KI auch im Bankenbereich immer bedeutsamer.<br>
            Gesetze erfordern jedoch in einigen Anwendungen Erklärbarkeit der Vorhersagen und Nachvollziehbarkeit der Modelle, weshalb "Black Box" KI-Modelle in der Kreditvergabe vor regulatorischen Hindernissen stehen und Vertrauen in solche Systeme nicht verbreitet ist.<br>
            <br>Um diese Algorithmen erklärbar zu machen, verfolgt <b>"Explainable AI"</b> das Ziel, mithilfe verschiedener post-hoc Ansätze, das Modell als Ganzes (global) oder Einzelentscheidungen (lokal) nachvollziehbar abzubilden.<br>
              
            <br>In diesem Experiment werden ein Modell des maschinellen Lernens (ML) mit einem klassischen logistisches Regressionsmodell verglichen, um das Kreditrisiko eines Bewerbers zu ermitteln. 20 Eigenschaften eines Bewerbers werden hierzu erfasst anhand derer die Risikoeinschätzung getroffen werden soll. <br>
            <br>Verschiedene Erklärungsansätze sollen dabei unterstützen, die Entscheidung des KI Modell nachvollziehbar zu machen:<br>
            
            <br>Als <b>globaler</b> Ansatz dienen <b> Shapley-Werte</b> aus der kooperativen Spieltheorie. Dieser Shapley-Wert ist der durchschnittliche Beitrag eines Attributes zur Vorhersage in verschiedenen Koalitionen für das Gesamtmodell.
            <br><br> Als <b>lokaler</b> Ansatz werden <b>Lokal interpretierbaren model-agnostischen Erklärungen (LIME)</b> genutzt.
             LIME approximiert das Black Box Modell an einem ausgewählten Datenpunkt (Instanz) mit einem Surrogatmodell, welches lokal linear und somit als interpretbierbar gilt.
            <br><br> Im Anschluss des Tests der beiden Modelle, sollen diese im Hinblick auf ihre Nützlichkeit und Verständlichkeit bewertet werden. 
            <br>


            </p>
            
        </div>
        <div>
            <p class="header"> 2. Experimentablauf </p>
            <br>
        </div>

        <div>
            <p class="text"> In der Studie betrachten Sie die Risikoeinschätzung eines Kreditbewerbers, die ein Algorithmus getroffen hat.<br>
            Sie testen verschiedene Algorithmen mithilfe globaler und lokaler Erklärungen. 
            <br>Nach dem Testdurchlauf erfolgt eine Umfrage. 
            
            <br>
            </p>
            
            <br>
        </div> 
        <div>   
            <p class="text"><u>Ablauf:</u><br>
            1. Kennenlernen der Datengrundlage  und Vertrautmachen mit der Ausgangslage<br>
            2. Training eines KI Modells<br>
            3. Vorhersage des Modells (Prediction)<br>
            4. Untersuchung der Erklärungsansätze  (global und lokal)<br>
            5. Evaluierung der Erklärungsansätze in einer Umfrage (externer Link)<br><br>
            </p>
             
            <br>

            
        </div>
        <div>
            <p class="header"> 3. Einverständnis </p>
            <br>
        </div>
        
        <div>
            <p class="text">- Bei Fragen oder Problemen sprechen Sie bitte Nico Boll  (<a href="mailto:nico.boll@consileon.de">nico.boll@consileon.de</a>) an. <br>
            - Ich bestätige, dass ich mindestens 18 Jahre alt bin.<br>
            - Ich bestätige die Einführung gelesen zu haben und bin mit der Teilnahme einverstanden. <br>
            - Meine Teilnahme erfolgt freiwillig. Ich weiß, dass ich die Möglichkeit habe, meine Teilnahme an dieser Studie jederzeit und ohne Angabe von Gründen abzubrechen, ohne dass mir daraus Nachteile entstehen.<br>
            
            <br> Wenn Sie die Einführung gelesen haben und damit einverstanden sind, klicken Sie <router-link to="/testphase"><b>weiter zur Testphase</b></router-link>
             
            </p>

        </div>
        <br><br><br>
    </v-app>
</template>



<style scoped>
   
    .text {
        float: left;
        background: rgba(255, 255, 255, 0.76);
        color: #000032;
        text-align: left;
        font-size: 20px;
        padding-top: 20px;
        padding-left: 50px;
    }
    .header{
        float:left;
        background: rgba(255, 255, 255, 0.76);
        color: #000032;
        text-align: center;
        font-size: 25px;
        font-weight: bold;
        padding-top: 0px;
        padding-left: 50px;
    }
    


</style>