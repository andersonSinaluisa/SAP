<template>
    <v-app id="index" style="background: #fff;">
        
    <v-container >
            <v-row align="center" >
                <v-col cols="7" >
                    <v-card
                        elevation="2"
                        shaped>
                        <v-card-title class="red accent-4 white--text">
                            Examinar documento
                                
                        </v-card-title>
                        <v-card-text>
                            <v-tabs centered>
                                <v-tab class="red--text" @click="step=1">Examinar documento</v-tab>
                                <v-tab @click="step=2" class="red--text">Examinar parrrafo</v-tab>
                                <v-tab @click="step=3" class="red--text">Comparar documento</v-tab>
                            </v-tabs>
                            <v-window v-model="step">
                                <v-window-item :value="1">
                                    <v-form class="py-3">

                                        <v-file-input
                                            color="red accent-4"
                                            placeholder="Selecciona una documento a examinar"
                                            id="documento"
                                            prepend-icon="mdi-file"
                                            label="Documento a examinar">
                                        </v-file-input>

                                        
                                        
                                    </v-form>
                                </v-window-item>

                                <v-window-item :value="2">
                                    <v-form class="py-3"> 
                                        <v-textarea label="Selecciona un parrrafo" prepend-icon="mdi-text" color="rec accent-4" placeholder="Selecciona un parrafo "/>
                                        <v-textarea label="Escribe el origen" prepend-icon="mdi-text" color="rec accent-4" placeholder="Selecciona alguna referencia bibliografica o deje en blanco para buscar todas"/>
                                    </v-form>
                                </v-window-item>

                                <v-window-item :value="3">
                                        <v-form>

                                            <v-file-input
                                                color="red accent-4"
                                                placeholder="Selecciona una documento a examinar"
                                                id="documento"
                                                prepend-icon="mdi-file"
                                                label="Documento a examinar">
                                            </v-file-input>

                                            <v-select>
                                                <v-item>Ninguno</v-item>
                                            </v-select>
                                        </v-form>
                                </v-window-item>

                            </v-window>
                        </v-card-text>
                        <v-card-actions>
                             <v-btn color="green accent-4" class="white--text" v-if="step==1">Examinar documento</v-btn>
                             <v-btn color="green accent-4" class="white--text" v-if="step==2">Examinar parrafos</v-btn>
                             <v-btn color="green accent-4" class="white--text" v-if="step==3">Comparar documentos</v-btn>
                        </v-card-actions>

                        <v-card-subtitle>
                            <span v-if="step==1"> Selecciona un documento a examinar. Se reaiza una busqueda en google con los diferentes parrafos. </span>
                            <span v-if="step==2"> Compara solo un parrafo especifico con resultados en la red. </span>
                            <span v-if="step==3"> Compara los resultados con los documentos guardados en tu biblioteca </span>   
                        </v-card-subtitle>

                    </v-card>
                </v-col>
                <v-col cols="5">
                    <v-card
                        shaped>
                        <v-card-title class="red accent-4 white--text">Resultados</v-card-title>
                        <v-card-text>
                            <v-row justify="center">
                                <v-col cols="6">
                                    <v-img src="../../statics/img/red-file--v1.png" width="150"/>
                                    <br><h3>Resultados de archivo.pdf</h3>
                                </v-col>
                            </v-row>
                            
                        </v-card-text>
                    </v-card>
                </v-col>
            </v-row>
    </v-container>
   
    </v-app>
</template>

<script>
import menuPrincipal from './menuPrincipal'
export default {
    name: 'index',
    components: { menuPrincipal },
    data: () => ({
        step: 1,
    })

}
</script>

<style>
</style>