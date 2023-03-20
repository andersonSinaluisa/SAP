import { createStore, combineReducers, compose, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import {persistStore, persistReducer} from 'redux-persist';
import storage from 'redux-persist/lib/storage'
import {loadState} from './state'
import { authReducer } from "./auth";
import {libraryReducer } from "./library";
import {statsReducer } from "./stats";


const rootReducer = combineReducers({
  auth:authReducer,
  library: libraryReducer,
  stats: statsReducer
});

const persistConfig = {
  key: 'root',
  storage
}

const persistedReducer = persistReducer(persistConfig, rootReducer);
const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

export const generateStore = ()=> {
  const initialData = loadState()

  const store = createStore(
    persistedReducer,
    initialData,
    composeEnhancers(applyMiddleware(thunk))
  );
  
  const persistor = persistStore(store,['auth'])


  return {store,persistor}
}


