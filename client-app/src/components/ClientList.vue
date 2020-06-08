<template>
    <div class="pt-5">
        <h5>Client list vue</h5>
        <div v-if="clients && clients.length">
            <div class="card mb-3" v-for="client of clients" v-bind:key="client.id">
                <div class="row no-gutters">
                    <div class="col-md-4">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <p class="card-title">{{ client.first_name }}</p>
                            <p class="card-text">{{ client.last_name }}</p>
                            <p class="card-text">{{ client.phone_number }}</p>
                            <p class="card-text">{{ client.onboarding_date }}</p>
                            <router-link :to="{name: 'edit', params: { id: client.id }}" class="btn btn-sm btn-primary">Edit</router-link>
                            <button class="btn btn-danger btn-sm ml-1" v-on:click="deleteClient(client)">Delete</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "ClientList.vue",
        data() {
            return {
                clients: []
            }
        },
        created() {
            this.getallClients();
        },
        methods: {
            getallClients: function () {
                axios.get('http://127.0.0.1:8000/olivier_petit_crud_nixa_app/')
                    .then(response => {
                        this.clients = response.data
                    });
            },
            deleteClient:  function(client){
                if (confirm('Delete ' + client.first_name + '' + client.last_name)) {
                    axios.delete(`http://127.0.0.1:8000/olivier_petit_crud_nixa_app/${client.id}`)
                    .then( response => {
                        this.all();
                    });
            }
            },
        }

    }
</script>

<style scoped>

</style>