<template>
    <v-app>

        <div>
            <p class="header"> 1. Datengrundlage </p>
            <br>
        </div>

        <div>
            <p class="text"> Die folgende Tabelle beschreibt die Datengrundlage und gibt Aufschluss über die Variablen, die der Algorithmus verwendet und aus Diskrimierungsgründen ausgeschlossen werden.</p>
        </div> 

        
        <div>
            <img class="datatable" src="../assets/data_table.png" alt="Data_Input"  >
            <img class="datatable" src="../assets/data_table2.png" alt="Data_Input" >
        </div>
        <br>
        <div>
            <p class="header"> 2.Explorative Datenanalyse </p>
            <br>
        </div>
        <div>
            <p class="text"> Der folgende Graph zeigt, dass 70 % der Beobachtungen ein gutes Kreditrisiko aufweisen, während 30 % ein schlechtes Kreditrisiko haben:</p>
            <br>
        </div>
        <div>
            <img class="picture"  src="../assets/distribution.png" alt="Data_Input"  width=800, height=500, >
        </div>
        <div>
            <p class="text"> Der folgende Graph zeigt, dass die Dauer (Kreditlaufzeit) meist innerhalb von 40 Monaten seit der Kreditvergabe liegt:</p>
            <br>
        </div>
        <div>
            <img class="picture" src="../assets/duration.jpg" alt="Data_Input"  width=800, height=500, >
        </div>
        <div>
            <p class="text"> Der folgende Graph zeigt, dass die meisten Kredite für die Verwendungszwecke "Radio/TV", "Car (new)" und "Furniture/Equipment" beantragt werden:</p>
            <br>
        </div>
        
        <div>
            <img class="picture" src="../assets/purpose.jpg" alt="Data_Input"  width=800, height=500, >
        </div>
        <div>
            <p class="text"> Der folgende Graph zeigt, dass die meisten Antragsteller mit Eigenheim ein gutes Kreditrisiko besitzen:</p>
            <br>
        </div>
        <div>
            <img class="picture" src="../assets/housing.jpg" alt="Data_Input"  width=800, height=500, >
        </div>
        <div>
            <p class="text"> Der folgende Graph zeigt, dass die meisten Antragsteller zwischen 20 und 50 Jahre alt sind:</p>
            <br>
        </div>
        <div>
            <img class="picture" src="../assets/age.jpg" alt="Data_Input"  width=800, height=500, >
        </div>
        <div>
            <p class="text"> Der folgende Graph zeigt, dass die meisten Kreditbeträge unter 10.000€ bleiben :</p>
            <br>
        </div>
        <div>
            <img class="picture" src="../assets/creditamount.jpg" alt="Data_Input"  width=800, height=500, >
        </div>
        <div>
            <p class="text"> Der folgende Graph zeigt, dass die meisten Kreditbewerber weniger als 100 € Sparguthaben besitzen :</p>
            <br>
        </div>
        <div>
            <img class="picture" src="../assets/savingaccounts.jpg" alt="Data_Input"  width=800, height=500, >
        </div>
        <div>
            <p class="text"> Der folgende Graph zeigt, dass die meisten Kreditbewerber kein Girokonto besitzen :</p>
            <br>
        </div>
        <div>
            <img class="picture" src="../assets/checkingaccount.png" alt="Data_Input"  width=800, height=500, >
        </div>

        <br>
        <br>

        <div>
            <p class="header"> 2. Initialisierung </p>
            <br>
        </div> 
        <div>
            <p class="text"> Drücke auf den Button <b>INITALIZATION</b>, um das backend zu initialisieren. (Daten Preprocessing, Train und Test Split) </p>
            <br>
            <v-btn class="button"
                   filled
                   required
                   @click="initialize_backend(),return_trained_models_timeout()">
                INITIALIZATION
            </v-btn>
            <br>
            <p class="response_text"> {{msg_backend}} </p>
            <br>
        </div> 

        <div>
            <p class="header"> 3. Logistische Regression Trainieren </p>
            <br>
        </div> 
        <div>
            <p class="text"> Suche ein Modell aus, um es zu trainieren.</p>
            <br>
            <br>
            <v-select class="button"
                      :items="possible_models"
                      v-model="chosen_model"
                      filled
                      required
                      label="CHOOSE MODEL"
                      @input="train_model()"
            ></v-select>
            <br>
            <p class="response_text"> {{msg_model}} </p>
            <br>
            <br>
            

        </div>
        <br>
        
        <div>
            <p class="text">Nach Abschluss der Testphase gehen Sie weiter auf <b>"4. Training"</b>
            </p>
        </div>

    </v-app>
</template>

<script>
    import axios from "axios";

    export default {
        name: "Training",
        mounted() {
            this.return_trained_models()
        },

        data: () => {
            return {
                msg_backend: "",
                msg_model: "",
                trained_models:"",

                chosen_model: "",
                possible_models: ["Logistic Regression"],
            }
        },

        methods: {
            return_trained_models() {
                // get the existing experiments from the server
                axios.get('http://127.0.0.1:5000/return_trained_models', {
                    params: {
                        dataset: this.dataset
                    }
                })
                    .then(response => {
                        this.trained_models = response.data
                    })
            },
            return_trained_models_timeout(){
              setTimeout(this.return_trained_models(), 2000)
            },
            initialize_backend() {
                // initialize the backend
                this.msg_backend = "initializing..."
                axios.post("http://127.0.0.1:5000/initialize_backend", {})
                    .then(response => {
                        this.msg_backend = response.data
                    })
                this.return_trained_models();
            },
            train_model() {
                // training with model
                this.msg_model = "training..."
                axios.post("http://127.0.0.1:5000/train_new_model", {
                    chosen_model: this.chosen_model
                })
                    .then(response => {
                        this.msg_model= response.data
                    })
                this.return_trained_models_timeout()
            },
        }
    }

</script>

<style scoped>
    .button {
        float: top;
        background: rgba(255, 255, 255, 0.76);
        color: #000032;
        font-size: 15px;
        margin: 100px;
    }

    .text {
        float: left;
        background: rgba(255, 255, 255, 0.76);
        color: #000032;
        text-align: left;
        font-size: 20px;
        padding-top: 20px;
        padding-left: 50px;
    }

    .response_text {
        float: left;
        background: rgba(255, 255, 255, 0.76);
        color: #000032;
        font-size: 20px;
        padding-top: 10px;
        padding-left: 50px;
    }
    .datatable{
        float: left;
        margin-left: 150px;
        margin-right: 50px;
        margin-top: 20px;
        width: 30%;
    }
    .header{
        float:left;
        background: rgba(255, 255, 255, 0.76);
        color: #000032;
        text-align: left;
        font-size: 25px;
        font-weight: bold;
        padding-top: 0px;
        padding-left: 50px;
    }
    .picture{
        float: center;
        margin-left: 200px;
        margin-right: 200px;
        margin-top: 20px;
        width: 50%;
    }
    

</style>