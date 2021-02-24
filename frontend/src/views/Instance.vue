<template>
    <v-app>
         <div>
            <p class="header"> <u>Lokale Erklärung mithilfe von Lokal interpretierbaren model-agnostischen Erklärungen (LIME) </u>
             </p>
        </div>
        <div>
            <p class="text"> Wähle das trainierte Modell, sowie den ausgesuchten Kreditbewerber aus:
             </p>
        </div>
        <v-container fluid>
        
            <div>
                <v-select
                        :items="trained_models"
                        v-model="chosen_model"
                        filled
                        required
                        label="MODEL"
                        @input="local_explanation()"
                ></v-select>
                <v-select
                        :items="possible_instances"
                        v-model="chosen_instance"
                        filled
                        required
                        label="INSTANCE"
                        @input="local_explanation()"
                ></v-select>

                <p>  {{msg_local}} </p><br>

                <v-btn class="button"
                   filled
                   required
                   @click="get_limeplot()">
                SHOW LOCAL EXPLANATION
                </v-btn><br>

                <v-col cols="12" sm="15">
                    <p> FORCEPLOT </p>
                    <img :src="forceplot_url"
                         alt="no Image"
                         height="300px">
                </v-col>

                <v-col cols="12" sm="15">
                    <p> LIMEPLOT </p>
                    <img :src="limeplot_url"
                         alt="no Image"
                         height="600px">
                </v-col>

            </div>
        </v-container>

        <div>  
             <p class="header"> Zusatzinformation:
             </p>
        </div>       
        <div>  
            <p class="text"> LIME approximiert das Black Box Modell an einem Datenpunkt (ausgewählte Instanz) mit einem Surrogatmodell, welches lokal linear und somit interpretbierbar ist. 
            </p>
        </div>
        
        <div>
            <img src="../assets/lime.png" alt="Data_Input"   class="picture" >
        </div>
       <div>
            <p class="text"> Gehen Sie weiter zum <router-link to="/survey"><b>Ende des Experiment</b></router-link>
            </p>
             

        </div>
        <br>
        <br>
    </v-app>
</template>

<script>
    import axios from "axios";

    export default {
        mounted() {
            //this.initialize_xai()
            //this.get_shapplot()
            //this.get_limeplot()
            this.get_possible_instance()
            this.return_trained_models()
        },

        components: {},
        data: () => {
            return {
                limeplot: "",
                limeplot_url: "",
                forceplot: "",
                // forceplot_url: "",
                possible_instances: ["xxx"],
                chosen_instance: "",
                dataset:"german_credit_dataset",
                msg: "",
                msg_local:"",
                trained_models:"",
                chosen_model: "",

            }
        },
        methods: {
            return_trained_models() {
                // get the existing experiments from the server
                axios.get('http://127.0.0.1:5000/return_trained_models', {
                    params: {
                    }
                })
                    .then(response => {
                        this.trained_models = response.data
                    })
            },
            get_possible_instance() {
                // get the existing experiments from the server
                axios.get('http://127.0.0.1:5000/get_instances', {
                    params: {
                    }
                })
                    .then(response => {
                        this.possible_instances = response.data
                    })
            },
            initialize_xai() {
                // initialize the xai plots and data
                axios.post("http://127.0.0.1:5000/model_explaining", {})
                    .then(response => {
                        this.msg = response.data
                    })
            },
            local_explanation() {
                // initialize the local xai plots and data
                axios.post("http://127.0.0.1:5000/local_explanation", {
                    chosen_model: this.chosen_model,
                    chosen_instance: this.chosen_instance,
                })
                    .then(response => {
                        this.msg_local = response.data
                    })
            },
            get_limeplot() {
                // Get the lime plot
                axios.post("http://127.0.0.1:5000/limeplot", {
                    chosen_model: this.chosen_model,
                    chosen_instance: this.chosen_instance
                }, {responseType: "blob"})
                    .then((response) => {
                        this.limeplot = response.data
                        this.limeplot_url = URL.createObjectURL(this.limeplot)
                        console.log("response", response.data)
                    })
            },
            get_forceplot() {
                // Get the forceplot
                axios.post("http://127.0.0.1:5000/forceplot", {
                    chosen_model: this.chosen_model,
                    chosen_instance: this.chosen_instance
                }, {responseType: "blob"})
                    .then((response) => {
                        this.forceplot = response.data
                        this.forceplot_url = URL.createObjectURL(this.forceplot)
                        console.log("response", response.data)
                    })
            }
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