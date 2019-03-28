import { TestBed } from '@angular/core/testing';

import { ExpService } from './exp.service';

describe('ExpService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ExpService = TestBed.get(ExpService);
    expect(service).toBeTruthy();
  });
});
