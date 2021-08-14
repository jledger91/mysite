import { all } from 'redux-saga/effects';

import { getFilmSaga } from './_sagas/getFilm';
import { getFilmsSaga } from './_sagas/getFilms';

export default function* combinedSagas() {
  yield all([
    getFilmSaga(),
    getFilmsSaga(),
  ]);
}
