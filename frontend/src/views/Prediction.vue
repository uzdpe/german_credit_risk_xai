<template>
    <v-app>
        <v-container fluid>
            <div>
                
                <v-select
                        :items="possible_instances"
                        v-model="chosen_instance"
                        filled
                        required
                        label="INSTANCE"
                        @input="get_possible_instance()"
                ></v-select>

                <p> Data:  {{msg_local}} </p>

                
                <v-col cols="12" sm="15">
                    <p> . </p>
                    <img :src="forceplot_url"
                         
                         height="300px">
                </v-col>
                <v-btn class="button"
                   filled
                   
                   @click="initialize_backend(),return_trained_models_timeout()">
                Good Credit Risk
            </v-btn>
            <v-btn class="button"
                   filled
                   
                   @click="initialize_backend(),return_trained_models_timeout()">
                Bad Credit Risk
            </v-btn>

                
            </div>
        </v-container>
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
                forceplot_url: "",
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
            return_explore_training_data() {
                // get the existing experiments from the server
                axios.get('http://127.0.0.1:5000/explore_training_data', {
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
        }
    }

</script>

<style scoped>


</style>