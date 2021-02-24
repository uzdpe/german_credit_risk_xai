<template>
    <v-app>

        <div>
            <p class="header">  <u>Training </u> </p>
        </div>

        <div>
            <p class="header"> 1. Initialisierung </p>
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
            <p class="header"> 2. Modell Trainieren </p>
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
            <p class="response_text"> Die folgenden Modelle wurden trainiert: {{trained_models}} </p>

        </div>
        <br>
        
        <div>
            <p class="text"> Gehen Sie weiter auf <a href="http://localhost:8080/prediction" ><b>weiter zur Modellvorhersage (Prediction)</b></a>
            </p>
            

        </div>
        <br>
        <br>

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
                possible_models: ["Extreme Gradient Boosting", "Logistic Regression", "Decision Tree",
                "Random Forest", "Support Vector Machine"],
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
    

</style>