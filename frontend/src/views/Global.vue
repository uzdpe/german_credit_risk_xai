<template>
    <v-app>
    <div>
            <p class="header"><u>Globale Modellerklärung mithilfe von Shapley Values aus der Spieltheorie </u> </p>
        </div>
        <v-container fluid>
            <div>
                <v-select
                        :items="trained_models"
                        v-model="chosen_model"
                        filled
                        required
                        label="MODEL"
                        @input="get_shapplot()"
                ></v-select>


                <v-col cols="12" sm="15">
                    <p> SHAPPLOT </p>
                    <img :src="shapplot_url"
                         alt="no Image"
                         height="800px">
                </v-col>
                


            </div>
            

        </v-container>

        <div>  
             <p class="header"> Zusatzinformation:
             </p>
        </div>       
        <div>  
            <p class="text"> Interpretation: Ein hoher Wert für Checking Account (3 = hoch) führt zu einer Erhöhung der Zuordnung zur Klasse 1 ( = gutes Risiko).

            </p>
        </div>
        <div>
            <p class="text"> Der globale Feature-Impact identifiziert, welche Features in einem Datensatz den größten positiven oder negativen Effekt auf die Ergebnisse eines ML Modells haben.
            </p>
        </div>
        
        <div>
            <p class="text"> Shapley-Werte helfen bei der Zuordnung des marginalen "Beitrags" jedes der Merkmale und der “Richtung" des Merkmals, das die abhängige Variable beeinflusst
.
            </p>
        </div>
        <div>
            <img src="../assets/shapley.png" alt="Data_Input"   class="picture" >
        </div>
        <br><br>
        <div>
            <p class="text"> Gehen Sie <router-link to="/instance"><b>weiter zur lokalen Erklärung</b></router-link>
            </p>
            

        </div>
    </v-app>
</template>

<script>
    import axios from "axios";

    export default {
        name: "Global",
        mounted() {
            this.initialize_xai()
            // this.get_shapplot()
            // this.get_forceplot()
            this.return_trained_models()
        },

        components: {},
        data: () => {
            return {
                shapplot: "",
                shapplot_url: "",
                chosen_model: "",
                msg: "",
                trained_models: ["", ""]

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
            initialize_xai() {
                // initialize the xai plots and data
                axios.post("http://127.0.0.1:5000/model_explaining", {})
                    .then(response => {
                        this.msg = response.data
                    })
            },
            get_shapplot() {
                // Get the shapplot
                axios.post("http://127.0.0.1:5000/shapplot", {
                    chosen_model: this.chosen_model
                }, {responseType: "blob"})
                    .then((response) => {
                        this.shapplot = response.data
                        this.shapplot_url = URL.createObjectURL(this.shapplot)
                        console.log("response", response.data)
                    })
            },
        }
    }


</script>

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
    .picture {
        float: center;
        background: rgba(255, 255, 255, 0.76);
        color: #000032;
        text-align: left;
        font-size: 50px;
        padding-top: 20px;
        padding-left: 100px;
        
    }


</style>