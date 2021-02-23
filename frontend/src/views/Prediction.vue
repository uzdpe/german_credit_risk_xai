<template>
    <v-app>
     <div>
            <p class="header">  Vorhersage </p>
            <br>
        </div>

        <div>
            <p class="text">Für folgenden Bewerber wird eine Vorhersage getroffen.</p>
        </div> 
        <v-container fluid>
            <div>
                <v-select
                        :items="possible_instances"
                        v-model="chosen_instance"
                        filled
                        required
                        label="INSTANCE"
                        @input="data_table()"
                ></v-select>

                <p> Return message:  {{msg_local}} </p>

                <v-btn class="button"
                   filled
                   required
                   @click="data_table()">
                SHOW INSTANCE VALUES
                </v-btn>

                
                <v-col cols="12" sm="15">
                    <p> DATA </p>
                    <img :src="limeplot_url"
                         alt="no Image"
                         height="600px">
                </v-col>

            </div>
            
        </v-container>

        <div>
            <p class="header">  Vorhersage </p>
            <br>
        </div>

        <div>
            <p class="text">Für folgenden Bewerber wird eine Vorhersage getroffen.</p>
        </div> 

        
        <div>
            <img class="datatable" src="../assets/applicant1.png" alt="Data_Input"  >
            
        </div>

        <br>
        <br>
        <div>
            <p class="text">Der Algorithmus hat folgende Vorhersage getroffen:</p>
        </div> 
        <div>
            <img class="datatable" src="../assets/output.png" alt="Data_Input"  >
            
        </div>
        <br>
        <br>
         <div>
            <p class="text"> Schauen Sie sich die Erklärungsansätze unter <b>"3.1 Globale Explanation"</b> und <b>"3.2 Lokale Explanation"</b> an.
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
                datatable: "",
                datatable_url: "",
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
            
            data_table() {
                // initialize the data_table
                axios.post("http://127.0.0.1:5000/data_table", {
                    chosen_instance: this.chosen_instance,
                },{responseType: "blob"})
                    .then((response) => {
                        this.datatable = response.data
                        this.datatable_url = URL.createObjectURL(this.datatable)
                        console.log("response", response.data)
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