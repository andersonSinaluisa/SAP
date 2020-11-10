<template>
<v-app id="biblioteca">
<menuPrincipal />
 <v-main>
   
 </v-main>
</v-app>
</template>

<script>
import index from "../principal_components/index"
import menuPrincipal from '../principal_components/menuPrincipal'
export default {
    name: 'biblioteca',
    components:{ index,menuPrincipal }

}
</script>

<style>

</style>