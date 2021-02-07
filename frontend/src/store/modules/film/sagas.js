import { all } from 'redux-saga/effects';

import { getFilmSaga } from './sagas/getFilm';
import { getFilmsSaga } from './sagas/getFilms';

export default function* combinedSagas() {
  yield all([
    getFilmSaga(),
    getFilmsSaga(),
  ]);
}
