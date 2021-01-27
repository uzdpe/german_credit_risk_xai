<template>
    <v-app>
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


</style>