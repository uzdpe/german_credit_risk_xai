<template>
    <v-app>
        <div>
            <p class="header"> <u>Umfrage </u>
             </p>
        </div>

         <div>
            <p class="text"> Sie haben die Experiment - Phase abgeschlossen!</p>
            <br>
        </div>              
        <div>
            <p class="text">Zum Abschluss füllen Sie bitte die folgende Umfrage aus.</p>
            <br>      
        </div>
        
        <v-col class="text" cols="12" sm="15">
                    <p><a href="https://nicoboll.limequery.com/984266"  target="_blank"><b>LINK ZUR UMFRAGE</b></a> </p>
                    
                </v-col>
                     
        
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
            }
            
        }
    }

</script>

<style scoped>
    .button {
        float: top;
        background: rgba(255, 255, 255, 0.76);
        color: #000032;
        font-size: 20px;
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
    .datatable{
        float: center;
        margin-left: 100px;
        margin-right: 100px;
        margin-top: 100px;
        width: 50%;
    }


</style>