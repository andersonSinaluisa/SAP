<template>
    <v-app id="index" style="background: #fff;">
        <menuPrincipal/>
        <v-main> 
            <template>
                <router-view />
            </template>
        </v-main>        
    </v-app>
</template>

<script>
import menuPrincipal from './menuPrincipal'
export default {
    name: 'index',
    components: { menuPrincipal }

}
</script>

<style>
</style>