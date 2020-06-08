<template>
    <div class="pt-5">
        <form @submit.prevent="update" method="post">
            <div class="form-group">
                <label for="first_name">First name</label>
                <input
                        type="text"
                        class="form-control"
                        id="first_name"
                        v-model="client.first_name"
                        name="first_name"
                        placeholder="Please enter your first name"
                >
            </div>
            <div class="form-group">
                <label for="last_name">Last name</label>
                <input
                        type="text"
                        class="form-control"
                        id="last_name"
                        v-model="client.last_name"
                        name="last_name"
                        placeholder="Please enter your last name"
                >
            </div>
            <div class="form-group">
                <label for="phone_number">Phone number</label>
                <input
                        type="text"
                        class="form-control"
                        name="phone_number"
                        id="phone_number"
                        v-model="client.phone_number"
                        placeholder="Enter your phone number"
                >
            </div>
            <div class="form-group">
                <label for="onboarding_date">Onboarding date</label>
                <input
                        type="datetime-local"
                        class="form-control"
                        name="onboarding_date"
                        id="onboarding_date"
                        v-model="client.onboarding_date"
                >
            </div>
            <button type="submit" class="btn btn-primary">Update</button>
        </form>
    </div>
</template>

<script>

    import axios from 'axios';

    export default {
        name: "EditClient.vue",
        data() {
            return {
                client: {
                    first_name: '',
                    last_name: '',
                    phone_number: '',
                    onboarding_date: '',
                },
                submitted: false
            }
        },
        mounted() {
            axios.get('http://127.0.0.1:8000/olivier_petit_crud_nixa_app/' + this.$route.params.id)
                .then(response => {
                    this.client = response.data
                });
        },
        methods: {
            update: function (e) {
                axios
                    .put(`http://127.0.0.1:8000/olivier_petit_crud_nixa_app/${client.id}`,
                        this.client
                    )
                    .then(response => {
                        this.$router.push('/');
                    })
            }
        },
    }
</script>

<style scoped>

</style>